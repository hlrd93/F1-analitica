import io
import os
from pathlib import Path
from datetime import date

import pandas as pd
import plotly.express as px
import streamlit as st

# Optional ClickHouse client (used if environment and connectivity exist)
try:
    from clickhouse_connect import get_client
except Exception:
    get_client = None


ROOT = Path(__file__).resolve().parents[1]
# Streamlit extracts directory (renamed from tableau_extracts)
EXTRACT_DIR = ROOT / "docs" / "streamlit_extracts"
METRICS_CSV = EXTRACT_DIR / "constructor_metrics_full.csv"
TS_CSV = EXTRACT_DIR / "constructor_time_series_full.csv"
DATASETS_DIR = ROOT / ".." / "datasets"
RESULTS_CSV = DATASETS_DIR / "results.csv"


@st.cache_data
def load_metrics(path: Path):
    return pd.read_csv(path)


@st.cache_data
def load_time_series(path: Path):
    df = pd.read_csv(path, parse_dates=["race_date"])
    # ensure race_date is datetime
    if df["race_date"].dtype == object:
        df["race_date"] = pd.to_datetime(df["race_date"])
    return df


def csv_download_button(df: pd.DataFrame, filename: str, label: str = "Download CSV"):
    buf = io.StringIO()
    df.to_csv(buf, index=False)
    b = buf.getvalue().encode("utf-8")
    st.download_button(label, data=b, file_name=filename, mime="text/csv")


def main():
    st.set_page_config(page_title="Constructor ROI Explorer", layout="wide")
    st.title("Constructor ROI Explorer")

    if not METRICS_CSV.exists() or not TS_CSV.exists():
        st.error(f"Missing CSVs in {EXTRACT_DIR}. Make sure files exist: {METRICS_CSV.name}, {TS_CSV.name}")
        return

    metrics = load_metrics(METRICS_CSV)
    ts = load_time_series(TS_CSV)

    # Left: controls
    with st.sidebar:
        st.header("Filters")
        min_cost = float(metrics["cost_proxy_score"].min()) if "cost_proxy_score" in metrics.columns else 0.0
        max_cost = float(metrics["cost_proxy_score"].max()) if "cost_proxy_score" in metrics.columns else 1.0
        cost_range = st.slider("Cost proxy range", min_value=0.0, max_value=1.0, value=(0.0, 0.6), step=0.01)

        constructors = sorted(metrics["constructor_name"].unique())
        selected_cons = st.multiselect("Constructor(s)", options=constructors, default=constructors[:6])

        st.markdown("---")
        st.write("Download data")
        csv_download_button(metrics, "constructor_metrics_full.csv", "Download metrics CSV")
        csv_download_button(ts, "constructor_time_series_full.csv", "Download time-series CSV")

    # Main layout: three charts
    col1, col2 = st.columns([2, 1])

    # Scatter: cost_proxy_score vs podium_rate
    with col1:
        st.subheader("Cost proxy vs Podium rate")
        df_scatter = metrics.copy()
        if "cost_proxy_score" in df_scatter.columns:
            df_scatter = df_scatter[(df_scatter["cost_proxy_score"] >= cost_range[0]) & (df_scatter["cost_proxy_score"] <= cost_range[1])]
        if selected_cons:
            df_scatter = df_scatter[df_scatter["constructor_name"].isin(selected_cons)]

        if df_scatter.empty:
            st.info("No constructors match the filters.")
        else:
            size_col = "total_races" if "total_races" in df_scatter.columns else None
            fig = px.scatter(
                df_scatter,
                x="cost_proxy_score",
                y="podium_rate",
                color="recent_podium_rate" if "recent_podium_rate" in df_scatter.columns else None,
                size=size_col,
                hover_name="constructor_name",
                labels={"cost_proxy_score": "Cost proxy (normalized)", "podium_rate": "Podium rate"},
                title="Cost proxy vs Podium rate (bubble=size total races)",
            )
            st.plotly_chart(fig, use_container_width=True)

    # Right: mid-tier bar and top list
    with col2:
        st.subheader("Mid-tier (cost band) overview")
        low, high = 0.2, 0.6
        mid_band = metrics[(metrics["cost_proxy_score"] >= low) & (metrics["cost_proxy_score"] <= high)]
        mid_band = mid_band.sort_values("recent_podium_rate", ascending=False)
        st.write(f"Showing constructors with cost_proxy_score in [{low}, {high}] (mid-tier). Count: {len(mid_band)}")
        if not mid_band.empty:
            st.dataframe(mid_band[["constructor_name", "cost_proxy_score", "podium_rate", "recent_podium_rate", "total_races"]].head(50))
            csv_download_button(mid_band, "mid_tier_constructors.csv", "Download mid-tier CSV")
        else:
            st.info("No mid-tier constructors found in the chosen band.")

    st.markdown("---")

    st.subheader("Time series — recent podium rate per race")
    pick_cons = st.multiselect("Pick constructors for time series", options=constructors, default=selected_cons)
    ts_plot = ts.copy()
    if pick_cons:
        ts_plot = ts_plot[ts_plot["constructor_name"].isin(pick_cons)]

    if ts_plot.empty:
        st.info("No time series rows available for selected constructors.")
    else:
        fig_ts = px.line(
            ts_plot,
            x="race_date",
            y="recent_podium_rate",
            color="constructor_name",
            labels={"race_date": "Race date", "recent_podium_rate": "Recent podium rate"},
            title="Recent podium rate over time (rolling last-12 races)",
        )
        st.plotly_chart(fig_ts, use_container_width=True)

    st.markdown("---")
    st.header("Drivers with fewest constructor changes — last 5 years")

    @st.cache_data
    def compute_top10_least_changes_from_csv(path: Path):
        # Fallback logic using datasets/results.csv
        df = pd.read_csv(path, parse_dates=["date"], infer_datetime_format=True)
        # results.csv has race-level date in `date` column, and columns driverId, constructorId
        # Filter last 5 years
        cutoff = pd.to_datetime(date.today()) - pd.DateOffset(years=5)
        if "date" in df.columns:
            df = df[pd.to_datetime(df["date"]) >= cutoff]

        # Ensure we have the necessary columns
        if not set(["driverId", "constructorId", "date"]).issubset(df.columns):
            return pd.DataFrame(columns=["driverId", "driver_name", "n_changes"])

        # Sort by driver and date
        df = df.sort_values(["driverId", "date", "raceId"]) if "raceId" in df.columns else df.sort_values(["driverId", "date"])

        # Compute changes per driver as number of transitions where constructorId changes between consecutive races
        def count_transitions(sub):
            # keep only constructorId sequence
            seq = sub["constructorId"].astype(str).tolist()
            if not seq:
                return 0
            transitions = sum(1 for a, b in zip(seq, seq[1:]) if a != b)
            return transitions

        grouped = df.groupby("driverId").apply(count_transitions).reset_index(name="n_changes")

        # Attach driver names if available in drivers.csv (datasets)
        drivers_path = path.parent / "drivers.csv"
        if drivers_path.exists():
            ddf = pd.read_csv(drivers_path, usecols=["driverId", "forename", "surname"], dtype={"driverId": object})
            ddf["driver_name"] = ddf["forename"].fillna("") + " " + ddf["surname"].fillna("")
            grouped = grouped.merge(ddf[["driverId", "driver_name"]], on="driverId", how="left")
        else:
            grouped["driver_name"] = grouped["driverId"].astype(str)

        grouped = grouped.sort_values(["n_changes", "driverId"]).head(10)
        return grouped[["driverId", "driver_name", "n_changes"]]

    def try_clickhouse_snapshot_top10():
        # Try to query ClickHouse snapshot table created by dbt snapshot.
        # env vars follow scripts/.env usage: CH_HOST, CH_PORT, CH_USER, CH_PASS, CH_DB_ANALYTICS
        if get_client is None:
            return None

        ch_host = os.getenv("CH_HOST", "localhost")
        ch_port = int(os.getenv("CH_PORT", 8123))
        ch_user = os.getenv("CH_USER", "default")
        ch_pass = os.getenv("CH_PASS", "") or None
        db = os.getenv("CH_DB_ANALYTICS", "analytics")

        try:
            client = get_client(host=ch_host, port=ch_port, username=ch_user, password=ch_pass)
        except Exception:
            return None

        # Common dbt snapshot relation name: analytics.driver_constructors_snapshot
        snapshot_table = f"{db}.driver_constructors_snapshot"

        # Build SQL to compute number of distinct constructors or transitions per driver in last 5 years.
        # We'll count distinct constructor periods in the snapshot rows within the timeframe.
        sql = f"""
        SELECT
            driverId,
            countDistinct(constructorId) AS n_teams
        FROM {snapshot_table}
        WHERE dbt_valid_from >= subtractYears(today(), 5)
        GROUP BY driverId
        ORDER BY n_teams ASC
        LIMIT 10
        """
        try:
            res = client.query(sql)
            # clickhouse-connect returns .result_rows or .dictresult depending on API
            rows = []
            try:
                rows = res.result_rows
            except Exception:
                try:
                    rows = res.result_set
                except Exception:
                    rows = list(res)

            # Normalize to DataFrame
            df = pd.DataFrame(rows, columns=[c[0] for c in res.columns]) if hasattr(res, "columns") else pd.DataFrame(rows)
            # Try to attach names if `analytics.drivers` exists
            try:
                drv = client.query(f"SELECT driverId, forename, surname FROM {db}.drivers")
                drv_rows = drv.result_rows if hasattr(drv, 'result_rows') else list(drv)
                drv_df = pd.DataFrame(drv_rows, columns=[c[0] for c in drv.columns])
                drv_df["driver_name"] = drv_df["forename"].fillna("") + " " + drv_df["surname"].fillna("")
                df = df.merge(drv_df[["driverId", "driver_name"]], on="driverId", how="left")
            except Exception:
                df["driver_name"] = df["driverId"].astype(str)

            # Ensure columns
            if "n_teams" in df.columns:
                df = df.rename(columns={"n_teams": "n_changes"})
            df = df[["driverId", "driver_name", "n_changes"]]
            return df
        except Exception:
            return None

    def try_clickhouse_results_top10():
        """Query ClickHouse `fact_race_results` joined with `stg_races` to compute
        distinct constructors per active driver in the last 5 years.
        """
        if get_client is None:
            return None

        ch_host = os.getenv("CH_HOST", "localhost")
        ch_port = int(os.getenv("CH_PORT", 8123))
        ch_user = os.getenv("CH_USER", "default")
        ch_pass = os.getenv("CH_PASS", "") or None
        db = os.getenv("CH_DB_ANALYTICS", "analytics")

        try:
            client = get_client(host=ch_host, port=ch_port, username=ch_user, password=ch_pass)
        except Exception:
            return None

        sql = f'''
        SELECT r.driverId, countDistinct(r.constructorId) AS n_teams
        FROM {db}.fact_race_results AS r
        JOIN {db}.stg_races AS ra USING (raceId)
        WHERE ra.fecha >= subtractYears(today(), 5)
        GROUP BY r.driverId
        ORDER BY n_teams ASC, r.driverId ASC
        LIMIT 10
        '''
        try:
            res = client.query(sql)
            rows = []
            try:
                rows = res.result_rows
            except Exception:
                try:
                    rows = res.result_set
                except Exception:
                    rows = list(res)

            # Normalize to DataFrame
            df = pd.DataFrame(rows, columns=[c[0] for c in res.columns]) if hasattr(res, 'columns') else pd.DataFrame(rows)

            # Map driver names: try analytics.drivers table first
            try:
                drv = client.query(f"SELECT driverId, forename, surname FROM {db}.drivers")
                drv_rows = drv.result_rows if hasattr(drv, 'result_rows') else list(drv)
                drv_df = pd.DataFrame(drv_rows, columns=[c[0] for c in drv.columns])
                drv_df['driver_name'] = drv_df['forename'].fillna('') + ' ' + drv_df['surname'].fillna('')
                df = df.merge(drv_df[['driverId', 'driver_name']], on='driverId', how='left')
            except Exception:
                # Fallback to local CSV in repo
                try:
                    drv_csv = ROOT / 'datasets' / 'drivers.csv'
                    if drv_csv.exists():
                        ddf = pd.read_csv(drv_csv, usecols=['driverId', 'forename', 'surname'])
                        ddf['driverId'] = ddf['driverId'].astype(str)
                        ddf['driver_name'] = ddf['forename'].fillna('') + ' ' + ddf['surname'].fillna('')
                        df['driverId'] = df['driverId'].astype(str)
                        df = df.merge(ddf[['driverId', 'driver_name']], on='driverId', how='left')
                    else:
                        df['driver_name'] = df['driverId'].astype(str)
                except Exception:
                    df['driver_name'] = df['driverId'].astype(str)

            # Normalize column names
            if 'n_teams' in df.columns:
                df = df.rename(columns={'n_teams': 'n_changes'})

            df = df[['driverId', 'driver_name', 'n_changes']]
            return df
        except Exception:
            return None

    def try_docker_results_top10():
        """Run `docker exec clickhouse clickhouse-client` to get the same results.
        This avoids ClickHouse client library auth/port issues by executing the
        query inside the container where it runs as the server user.
        """
        import subprocess
        sql = (
            "SELECT r.driverId, countDistinct(r.constructorId) AS n_teams "
            "FROM analytics.fact_race_results AS r "
            "JOIN analytics.stg_races AS ra USING (raceId) "
            "WHERE ra.fecha >= subtractYears(today(), 5) "
            "GROUP BY r.driverId "
            "ORDER BY n_teams ASC, r.driverId ASC "
            "LIMIT 10"
        )
        cmd = [
            "docker",
            "exec",
            "-i",
            "clickhouse",
            "clickhouse-client",
            "--format",
            "CSVWithNames",
            "--query",
            sql,
        ]
        try:
            print('DEBUG: running docker exec for ClickHouse query', cmd)
            out = subprocess.check_output(cmd, stderr=subprocess.STDOUT)
            print('DEBUG: docker exec completed, bytes=', len(out))
            s = out.decode("utf-8")
            # Use pandas to parse CSV output
            from io import StringIO

            df = pd.read_csv(StringIO(s))
            print('DEBUG: Parsed dataframe shape:', df.shape)
            print('DEBUG: Dataframe columns:', df.columns.tolist())
            print('DEBUG: First few rows:\n', df.head())
            
            # ensure columns driverId and n_teams present
            if "driverId" in df.columns and "n_teams" in df.columns:
                # Map driver names from local CSV
                drv_csv = ROOT / "datasets" / "drivers.csv"
                if drv_csv.exists():
                    print(f'DEBUG: Loading driver names from {drv_csv}')
                    ddf = pd.read_csv(drv_csv, usecols=["driverId", "forename", "surname"]) 
                    ddf['driverId'] = ddf['driverId'].astype(str)
                    ddf['driver_name'] = ddf['forename'].fillna('').astype(str).str.strip() + ' ' + ddf['surname'].fillna('').astype(str).str.strip()
                    ddf['driver_name'] = ddf['driver_name'].str.strip()
                    
                    # Convert driverId to string for merging
                    df['driverId'] = df['driverId'].astype(str)
                    df = df.merge(ddf[['driverId', 'driver_name']], on='driverId', how='left')
                    print('DEBUG: After merge, dataframe shape:', df.shape)
                    print('DEBUG: After merge, first few rows:\n', df.head())
                else:
                    print(f'DEBUG: Driver CSV not found at {drv_csv}, using IDs as names')
                    df['driver_name'] = df['driverId'].astype(str)
                
                df['driverId'] = df['driverId'].astype(int)
                df = df.rename(columns={'n_teams': 'n_changes'})
                result = df[['driverId', 'driver_name', 'n_changes']]
                print('DEBUG: Final result:\n', result)
                return result
            print('DEBUG: Missing required columns driverId or n_teams')
            return None
        except Exception as e:
            print(f'DEBUG: Error in try_docker_results_top10: {e}')
            import traceback
            traceback.print_exc()
            return None
            return None
        except Exception as e:
            print(f'DEBUG: Error in try_docker_results_top10: {e}')
            return None

    # Try ClickHouse first
    ch_df = try_clickhouse_snapshot_top10()
    if ch_df is not None and not ch_df.empty:
        st.write("Data source: ClickHouse dbt snapshot `driver_constructors_snapshot` (last 5 years)")
        ch_df_display = ch_df.copy()
        ch_df_display.columns = ['Driver ID', 'Driver Name', 'Constructor Changes']
        st.dataframe(ch_df_display, use_container_width=True)
        csv_download_button(ch_df, "top10_least_changes_clickhouse.csv", "Download CSV")
    else:
        # If snapshot is not available, try computing from ClickHouse results (active drivers)
        ch_results_df = try_clickhouse_results_top10()
        if ch_results_df is not None and not ch_results_df.empty:
            st.write("Data source: ClickHouse `fact_race_results` joined with `stg_races` (active drivers, last 5 years)")
            ch_results_display = ch_results_df.copy()
            ch_results_display.columns = ['Driver ID', 'Driver Name', 'Constructor Changes']
            st.dataframe(ch_results_display, use_container_width=True)
            csv_download_button(ch_results_df, "top10_least_changes_clickhouse_results.csv", "Download CSV")
        else:
            # If ClickHouse Python client failed, try running `docker exec` in the
            # host to query the ClickHouse server from inside the container.
            ch_docker_df = try_docker_results_top10()
            if ch_docker_df is not None and not ch_docker_df.empty:
                st.write("Data source: ClickHouse (via docker exec clickhouse-client)")
                
                # Create a nice display with custom formatting
                ch_docker_display = ch_docker_df.copy()
                ch_docker_display.columns = ['Driver ID', 'Driver Name', 'Constructor Changes']
                
                # Display as a nice table
                st.dataframe(ch_docker_display, use_container_width=True)
                
                # Add a bar chart for visual comparison
                fig = px.bar(
                    ch_docker_df,
                    x='driver_name',
                    y='n_changes',
                    title='Drivers with Fewest Constructor Changes (Last 5 Years)',
                    labels={'driver_name': 'Driver', 'n_changes': 'Number of Constructor Changes'},
                    color='n_changes',
                    color_continuous_scale='RdYlGn_r'
                )
                fig.update_layout(
                    xaxis_tickangle=-45,
                    height=400,
                    showlegend=False
                )
                st.plotly_chart(fig, use_container_width=True)
                
                csv_download_button(ch_docker_df, "top10_least_changes_clickhouse_docker.csv", "Download CSV")
            else:
                # Fallback to datasets/results.csv
                results_path = (ROOT / ".." / "datasets" / "results.csv").resolve()
                if results_path.exists():
                    df_top10 = compute_top10_least_changes_from_csv(results_path)
                    st.write("Data source: fallback from local `datasets/results.csv` (last 5 years)")
                    if df_top10.empty:
                        st.info("Not enough data in results.csv to compute driver changes.")
                    else:
                        df_display = df_top10.copy()
                        df_display.columns = ['Driver ID', 'Driver Name', 'Constructor Changes']
                        st.dataframe(df_display, use_container_width=True)
                        csv_download_button(df_top10, "top10_least_changes_fallback.csv", "Download CSV")
                else:
                    st.warning("No ClickHouse snapshot found and `datasets/results.csv` is missing. Cannot compute top-10 drivers with fewest constructor changes.")
        


if __name__ == "__main__":
    main()

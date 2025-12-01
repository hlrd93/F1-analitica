import io
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


ROOT = Path(__file__).resolve().parents[1]
EXTRACT_DIR = ROOT / "docs" / "tableau_extracts"
METRICS_CSV = EXTRACT_DIR / "constructor_metrics_full.csv"
TS_CSV = EXTRACT_DIR / "constructor_time_series_full.csv"


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


if __name__ == "__main__":
    main()

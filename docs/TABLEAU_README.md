## Connect Tableau to ClickHouse (quick guide)

This short README shows how to connect Tableau Desktop to the ClickHouse server in this project and includes a suggested dashboard wireframe to identify "mid-tier" teams with high sponsorship ROI potential.

Prerequisites
- Docker Compose running the project (ClickHouse available and ports mapped to the host).
- Tableau Desktop (or Tableau Server) installed on the same machine or network that can reach the ClickHouse host/ports.
- ClickHouse ODBC driver installed on the machine running Tableau (recommended for Tableau Desktop).

1) Ensure ClickHouse is reachable from Tableau

- If you're running Tableau on the same macOS host, confirm the ClickHouse service maps ports 8123 (HTTP) and/or 9000 (native TCP) to the host in `docker-compose.yml`.
- From your mac, test connectivity (example):

```bash
curl -sS "http://localhost:8123/" --data-binary "SELECT 1"
# or native client (if installed):
clickhouse-client --host localhost --port 9000 --user loader --password 'loaderpass' -q "SELECT 1"
```

2) Install ClickHouse ODBC driver (macOS)

- Official driver: https://clickhouse.com/docs/en/integrations/odbc/
- On macOS you may use a packaged driver or compile the driver; alternatively, use an ODBC manager like iODBC or unixODBC with the driver configured.
- Configure a DSN named `clickhouse_analytics` (or any name you like) pointing to host=localhost, port=9000 (native) or 8123 (HTTP—driver-dependent), user=loader, password=loaderpass, database=analytics.

3) Connect from Tableau Desktop

- Open Tableau Desktop.
- Choose "Other Databases (ODBC)".
- Select the DSN you created (`clickhouse_analytics`) and connect.
- In the connection dialog, set the default database/schema to `analytics`.

If you prefer not to use ODBC, you can:
- Use Tableau's generic "Web Data Connector" and a small intermediary service that exposes ClickHouse results (advanced).
- Use JDBC via a third-party Tableau connector if available.

Example query to load the constructor metrics table (Tableau SQL connection or Custom SQL):

```sql
SELECT *
FROM analytics.constructor_metrics
```

Notes on permissions and networking
- Do not commit real credentials into source control. `profiles.compose.yml` in this repo is intended for the Compose-run environment; change credentials per-site.
- If Tableau runs on a different machine, use the host's IP (not `localhost`) and ensure Docker Compose maps the port to the host and firewall rules allow access.

Dashboard wireframe: Sponsorship ROI — detecting high-ROI mid-tier teams

Goal: find constructors that are not the absolute top spenders but deliver high podium rate or recent performance relative to a cost proxy (a cheap proxy for team budget).

Core KPIs (one per calculated field in Tableau)
- Podium Rate = total_podiums / total_races
- Recent Podium Rate = recent_podium_rate (already computed in the table)
- Avg Points Per Race = avg_points_per_race
- Cost Proxy Score = cost_proxy_score (0..1 heuristic; higher => likely more expensive)

Suggested visuals
- Scatter: Cost Proxy Score (x) vs Podium Rate (y)
  - Size bubble by total_races, color by recent_podium_rate.
  - Add reference lines at cost_proxy_score = 0.2 and 0.6 to define "mid-tier" band.
  - Quadrants highlight: High ROI (moderate cost, high podium rate), Low ROI (high cost, low podium rate), etc.

- Bar chart: Top 10 mid-tier teams by Recent Podium Rate
  - Filter Cost Proxy Score between 0.2 and 0.6 and sort by recent_podium_rate desc.

- Time series: Recent Podium Rate (rolling window) per constructor
  - Use the underlying race timeline (if you pull the race-level metrics) to show trends for selected teams.

- Table: Detailed metrics (constructor_name, seasons_active, total_races, total_podiums, podium_rate, recent_podium_rate, avg_points_per_race, cost_proxy_score)
  - Allow sorting and filtering by season range and minimum races (e.g., show teams with at least 5 races).

Filters and interactivity
- Season range (first_year..last_year)
- Minimum races (exclude tiny sample sizes)
- Constructor search / ranking

How to interpret the results
- Focus on mid-tier constructors (cost_proxy_score between ~0.2 and ~0.6) with above-median recent_podium_rate and a positive trend in the time series.
- These are the teams likely to provide better ROI for sponsorship budgets: not the most expensive teams, but performing well lately.

Sample: top 10 rows from `analytics.constructor_metrics` (ordered by cost_proxy_score desc)

```
"constructor_id","constructor_name","total_races","total_podiums","podium_rate","avg_points_per_race","podiums_last_12","races_last_12","recent_podium_rate","cost_proxy_score"
6,"Ferrari",1100,841,0.764545,0,8,12,0.666667,0.4
191,"Brabham-Repco",33,25,0.757576,0,7,12,0.583333,0.35
170,"Cooper-Climax",67,44,0.656716,0,6,12,0.5,0.3
196,"Matra-Ford",23,15,0.652174,0,5,12,0.416667,0.25
108,"Epperly",5,5,1,0,5,12,0.416667,0.25
211,"Racing Point",38,4,0.105263,0,3,12,0.25,0.15
150,"Deidt",3,2,0.666667,0,2,8,0.25,0.15
23,"Brawn",17,15,0.882353,0,3,12,0.25,0.15
107,"Watson",9,5,0.555556,0,3,12,0.25,0.15
9,"Red Bull",394,282,0.715736,0,3,12,0.25,0.15
```

Next steps (recommended)
- Tweak the `cost_proxy_score` definition in `dbt_project/models/marts/constructor_metrics.sql` if you have real cost/budget data: replace the heuristic with a real cost column or sponsorship amount.
- Add a small materialized `marts/constructor_time_series` model that computes rolling recent_podium_rate for better time-series visuals in Tableau.
- Build the Tableau workbook using the visuals above and export to a packaged workbook (`.twbx`) for sharing.

If you want, I can:
- Produce a packaged Tableau workbook skeleton (CSV extracts + workbook) with the suggested visuals populated from this dataset.
- Add the `constructor_time_series` dbt model and materialize it.

---
Generated on: 2025-12-01

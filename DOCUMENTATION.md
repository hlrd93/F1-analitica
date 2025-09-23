_key (PK)
circuit_id (Natural Key)
circuit_name
location
country
latitude
longitude
geom (PostGIS geometry)

-- dim_constructors
constructor_key (PK)
constructor_id (Natural Key)
constructor_name
nationality
first_season
last_season

-- dim_seasons
season_key (PK)
season_year
total_rounds
champion_driver_id
champion_constructor_id
era (Classic, Turbo, V10, Hybrid)

-- dim_status
status_key (PK)
status_id
status_description
status_category (Finished, Mechanical, Accident, Disqualified)
```

### Fact Tables

```sql
-- fact_race_results
result_key (PK)
driver_key (FK)
circuit_key (FK)
constructor_key (FK)
season_key (FK)
status_key (FK)
race_date_key (FK)

-- Degenerate Dimensions
race_id
result_id

-- Measures
points
laps_completed
grid_position
final_position
position_change
fastest_lap_time_ms
fastest_lap_speed
milliseconds

-- Flags
is_fastest_lap
is_podium
is_points_finish
is_dnf
```

---

## 🗓️ 12-Week Sprint Plan

### Sprint 1-2: Foundation (Weeks 1-2)

**User Stories:**

1. **US-001: Conda Environment Setup**
   - Create reproducible environment
   - Install all dependencies
   - Document setup process
   - **Estimation**: 2 story points

2. **US-002: Data Exploration with Polars**
   - Download Kaggle F1 dataset
   - EDA notebooks
   - Compare Polars vs pandas performance
   - **Estimation**: 5 story points

3. **US-003: PostgreSQL Setup**
   - Docker containerized database
   - Create schemas (raw, staging, marts)
   - Initialize tables
   - **Estimation**: 3 story points

### Sprint 3-4: dbt Implementation (Weeks 3-4)

**User Stories:**

4. **US-004: dbt Project Setup**
   - Initialize dbt project
   - Configure profiles.yml
   - Create sources
   - **Estimation**: 3 story points

5. **US-005: Star Schema Implementation**
   - Design dimensional model
   - Create dim_* tables
   - Create fact_race_results
   - Implement SCD Type 1/2
   - **Estimation**: 8 story points

6. **US-006: Data Quality Tests**
   - dbt tests (uniqueness, not_null, relationships)
   - Custom business rules tests
   - 100% test coverage
   - **Estimation**: 5 story points

### Sprint 5-6: Airflow Orchestration (Weeks 5-6)

**User Stories:**

7. **US-007: Airflow DAG Implementation**
   - Create f1_pipeline DAG
   - Extract, Load, Transform tasks
   - Dependencies and scheduling
   - **Estimation**: 8 story points

8. **US-008: Error Handling & Monitoring**
   - Retry logic
   - Alerting (email/Slack)
   - SLA monitoring
   - **Estimation**: 5 story points

### Sprint 7-8: Advanced Processing (Weeks 7-8)

**User Stories:**

9. **US-009: Polars Feature Engineering**
   - Rolling statistics
   - Driver consistency metrics
   - Circuit difficulty index
   - Lazy evaluation optimization
   - **Estimation**: 8 story points

10. **US-010: Spark Cluster Setup**
    - Spark master + workers
    - PySpark integration
    - Performance benchmarks
    - **Estimation**: 5 story points

### Sprint 9-10: Machine Learning (Weeks 9-10)

**User Stories:**

11. **US-011: MLflow Experiment Tracking**
    - MLflow server setup
    - Model 1: Position Classifier
    - Model 2: Points Regressor
    - Model 3: Fastest Lap Probability
    - **Estimation**: 13 story points

12. **US-012: Model Deployment API**
    - FastAPI application
    - Prediction endpoints
    - Model versioning
    - **Estimation**: 8 story points

### Sprint 11-12: Apps & Documentation (Weeks 11-12)

**User Stories:**

13. **US-013: Streamlit Interactive Apps**
    - Championship Explorer
    - Driver Performance Analyzer
    - Race Predictor
    - Circuit Analytics
    - Deploy to Streamlit Cloud
    - **Estimation**: 13 story points

14. **US-014: Project Documentation**
    - README comprehensive
    - Architecture diagrams
    - Video demo 10 minutes
    - Presentation slides
    - **Estimation**: 8 story points

---

## 🎯 Success Criteria

### Minimum Viable (Pass Course)
- ✅ Star schema implemented
- ✅ dbt models working
- ✅ 1 Streamlit dashboard
- ✅ Basic documentation
- ✅ Coherent presentation

### Target (Excellent Grade)
- ✅ Complete Airflow pipeline
- ✅ 3+ ML models
- ✅ 4 Streamlit apps
- ✅ Complete documentation
- ✅ Public deployment
- ✅ Performance benchmarks

### Stretch Goals (Portfolio Star)
- ✅ Apache Spark integration
- ✅ FastAPI deployed
- ✅ CI/CD with GitHub Actions
- ✅ Medium article published
- ✅ LinkedIn showcase
- ✅ 100+ GitHub stars

---

## 🚀 Getting Started - Next Steps

### This Week (Sprint 1 Start)

**Day 1: Environment Setup**
```bash
# Create Conda environment
conda env create -f environment.yml
conda activate f1_analytics

# Verify installation
python -c "import polars; print(polars.__version__)"
```

**Day 2: Download Data**
```bash
# Install Kaggle CLI
pip install kaggle

# Configure Kaggle credentials
mkdir -p ~/.kaggle
# Copy your kaggle.json to ~/.kaggle/

# Download F1 dataset
kaggle datasets download -d rohanrao/formula-1-world-championship-1950-2020
unzip formula-1-world-championship-1950-2020.zip -d data/raw/
```

**Day 3: Docker Setup**
```bash
# Start all services
docker-compose up -d

# Verify services
docker ps
curl http://localhost:8080  # Airflow
curl http://localhost:5000  # MLflow
```

**Day 4-5: First EDA**
```python
# notebooks/01_eda_polars.ipynb
import polars as pl

# Load data
df = pl.read_csv('data/raw/results.csv')

# Basic exploration
print(df.head())
print(df.describe())

# Performance benchmark
%timeit pl.read_csv('data/raw/results.csv')
%timeit pd.read_csv('data/raw/results.csv')
```

---

## 📚 Learning Resources

### Essential Reading
- [Kimball Data Warehouse Toolkit](https://www.kimballgroup.com/)
- [dbt Best Practices](https://docs.getdbt.com/best-practices)
- [Polars User Guide](https://pola-rs.github.io/polars-book/)

### Tutorials
- [dbt Learn](https://courses.getdbt.com/)
- [Airflow Tutorial](https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html)
- [Streamlit Gallery](https://streamlit.io/gallery)

### Community
- PyData Montevideo
- AWS User Group Uruguay
- Data Engineering UY (LinkedIn)

---

## 🎓 Deliverables for UCU

### Final Submission (Dec 5, 2025)
1. **Source Code** (GitHub ZIP)
2. **Documentation** (PDF)
   - Architecture diagrams
   - ER diagrams
   - Design decisions
3. **Dashboards** (Screenshots + Links)
4. **Video Demo** (10 minutes)
5. **Presentation** (PPT for defense)

### Defense (Dec 8, 2025)
- 15-minute presentation
- Q&A session
- Live demo

---

## 🏆 Expected Outcomes

### Academic
- Excellent grade in Data Analytics course
- Deep understanding of BI and DWH concepts
- Real-world project experience

### Professional
- Impressive GitHub portfolio
- Skills matching EverPass job posting
- Modern stack experience (dbt, Polars, Airflow)
- Publicly deployed applications

### Personal
- Confidence for technical interviews
- Data Engineering community network
- Deep knowledge of data lifecycle

---

## 📊 Performance Benchmarks

### Polars vs pandas (Expected Results)

| Operation | pandas | Polars | Speedup |
|-----------|--------|--------|---------|
| Read CSV (1M rows) | 3.5s | 0.4s | 8.8x |
| GroupBy aggregation | 2.1s | 0.3s | 7x |
| Join operations | 1.8s | 0.2s | 9x |
| Filter + transform | 1.2s | 0.15s | 8x |

### Pipeline Metrics

| Metric | Target |
|--------|--------|
| DAG success rate | >95% |
| dbt test pass rate | 100% |
| Data freshness | <24h |
| Model accuracy | >80% |
| Query performance | <2s |

---

## 🔧 Troubleshooting

### Common Issues

**1. Conda Environment Conflicts**
```bash
conda deactivate
conda env remove -n f1_analytics
conda clean --all
conda env create -f environment.yml
```

**2. Docker PostgreSQL Connection**
```bash
docker logs f1_postgres
docker-compose down -v
docker-compose up -d
```

**3. dbt Execution Errors**
```bash
dbt compile --models stg_drivers
dbt run --models stg_drivers --debug
```

**4. Polars Memory Issues**
```python
# Use lazy evaluation
df = pl.scan_csv('large_file.csv')
result = df.filter(pl.col('year') > 2000).collect()
```

---

## 📞 Support & Resources

### Course Support
- **Webasignatura UCU**: Forums and materials
- **Professors**:
  - Ing. Bernardo Rychtenberg: bernardo.rychtenberg@ucu.edu.uy
  - Mag. Héctor Cotelo: hector.cotelo@ucu.edu.uy

### Community
- PyData Montevideo Meetup
- AWS User Group Uruguay
- Data Engineering UY (LinkedIn)

### Stack Overflow
- Tags: `polars`, `dbt`, `apache-airflow`, `mlflow`, `streamlit`

---

## 🙏 Acknowledgments

- **UCU** - Masters in Data Science program
- **Kaggle** - F1 dataset
- **Open Source Community** - Amazing tools
- **Classmates** - Mutual support

---

## 📝 Final Notes

This project is your opportunity to:
- 🎓 Excel academically
- 💼 Launch your data engineering career
- 🚀 Build an impressive portfolio
- 📚 Master modern technologies

**Remember the 3 Golden Rules:**
1. **Iteration over Perfection** - Working prototype beats perfect design
2. **Documentation is Code** - If it's not documented, it doesn't exist
3. **Test Everything** - Bad data → Bad analysis → Bad decisions

---

## 🏁 Let's Go!

**Week 1 starts TODAY.**  
**Your future in Data Engineering begins NOW.**

Don't wait for the perfect moment. The perfect moment is **THIS**.

**Ready to build something incredible?**

## **¡VAMOS! 🏎️💨**

---

*Document created with ❤️ for success in UCU Data Science Masters*  
*Last updated: September 2024*

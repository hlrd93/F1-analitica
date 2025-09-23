# 🚀 F1 Analytics Project - Setup Complete!

## ✅ What Has Been Created

### Core Configuration Files
- ✅ `environment.yml` - Conda environment with all dependencies
- ✅ `docker-compose.yml` - Complete Docker stack (PostgreSQL, Airflow, MLflow, Streamlit, FastAPI)
- ✅ `.gitignore` - Git configuration
- ✅ `.env.example` - Environment variables template
- ✅ `README.md` - Professional project documentation
- ✅ `DOCUMENTATION.md` - Complete technical documentation

### Directory Structure
```
F1/
├── api/                    # FastAPI application
│   ├── Dockerfile
│   └── requirements.txt
├── dags/                   # Airflow DAGs
├── data/
│   ├── raw/               # Raw CSV files
│   └── processed/         # Parquet files
├── dbt_project/           # dbt transformations
├── init-scripts/          # Database initialization
│   └── init.sql
├── mlflow/                # MLflow Docker config
│   └── Dockerfile
├── notebooks/             # Jupyter notebooks
├── src/                   # Python source code
├── streamlit_app/         # Streamlit applications
│   ├── Dockerfile
│   └── requirements.txt
└── tests/                 # pytest tests
```

### Dataset
- ✅ Already downloaded in `/datasets` folder with 15 CSV files

---

## 🎯 Next Steps - Week 1 Sprint

### Day 1: Environment Setup (TODAY!)

```bash
# 1. Create Conda environment
cd /Users/herwin/Desktop/F1
conda env create -f environment.yml
conda activate f1_analytics

# 2. Verify installation
python -c "import polars; print('Polars version:', polars.__version__)"
python -c "import pandas; print('Pandas version:', pandas.__version__)"

# 3. Copy environment variables
cp .env.example .env
# Edit .env with your Kaggle credentials
```

### Day 2: Move Data to Correct Location

```bash
# Move CSV files from datasets/ to data/raw/
mv datasets/*.csv data/raw/
mv datasets/*.zip data/raw/

# Verify data is in place
ls -la data/raw/
```

### Day 3: Start Docker Services

```bash
# Start all services
docker-compose up -d

# Check if services are running
docker ps

# Access points:
# - Airflow: http://localhost:8080 (admin/admin)
# - MLflow: http://localhost:5000
# - Jupyter: http://localhost:8888
```

### Day 4-5: First Data Exploration

Create your first Jupyter notebook:

```bash
# Start Jupyter (if not using Docker)
jupyter lab

# Or access Docker Jupyter at http://localhost:8888
```

**Notebook: `notebooks/01_eda_polars.ipynb`**

```python
import polars as pl
import pandas as pd
import time

# Load data with Polars
df_polars = pl.read_csv('data/raw/results.csv')

# Basic exploration
print("Shape:", df_polars.shape)
print("\nFirst rows:")
print(df_polars.head())

print("\nData types:")
print(df_polars.dtypes)

print("\nNull counts:")
print(df_polars.null_count())

# Performance benchmark: Polars vs pandas
print("\n📊 Performance Comparison:")

# Polars
start = time.time()
df_pl = pl.read_csv('data/raw/results.csv')
result_pl = df_pl.group_by('driverId').agg(pl.col('points').sum())
polars_time = time.time() - start

# pandas
start = time.time()
df_pd = pd.read_csv('data/raw/results.csv')
result_pd = df_pd.groupby('driverId')['points'].sum()
pandas_time = time.time() - start

print(f"Polars time: {polars_time:.4f}s")
print(f"pandas time: {pandas_time:.4f}s")
print(f"Speedup: {pandas_time/polars_time:.1f}x")
```

---

## 📋 Sprint 1 Checklist

### Week 1 Tasks
- [ ] **Day 1**: Create Conda environment
- [ ] **Day 1**: Install all dependencies
- [ ] **Day 2**: Organize data files
- [ ] **Day 2**: Create .env with credentials
- [ ] **Day 3**: Start Docker services
- [ ] **Day 3**: Verify all containers running
- [ ] **Day 4**: First EDA notebook with Polars
- [ ] **Day 5**: Performance benchmarks documented

### Week 2 Tasks
- [ ] **Day 1**: PostgreSQL schema creation
- [ ] **Day 2**: Load raw data to database
- [ ] **Day 3**: Data quality assessment
- [ ] **Day 4**: Document findings
- [ ] **Day 5**: Sprint 1 review

---

## 🔍 Quick Commands Reference

### Conda
```bash
# Activate environment
conda activate f1_analytics

# Deactivate
conda deactivate

# Update environment
conda env update -f environment.yml --prune

# Export current environment
conda env export --no-builds > environment_lock.yml
```

### Docker
```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f postgres
docker-compose logs -f airflow-webserver

# Restart specific service
docker-compose restart postgres

# Remove all volumes (careful!)
docker-compose down -v
```

### Git
```bash
# Add files to staging
git add .

# Commit changes
git commit -m "Initial project setup"

# Push to remote
git push origin main

# Check status
git status

# View changes
git diff
```

---

## 🐛 Troubleshooting

### Issue: Conda environment creation fails
**Solution:**
```bash
# Clean conda cache
conda clean --all

# Try with mamba (faster)
conda install mamba -c conda-forge
mamba env create -f environment.yml
```

### Issue: Docker containers won't start
**Solution:**
```bash
# Check Docker is running
docker info

# Remove old containers
docker-compose down -v

# Rebuild images
docker-compose build --no-cache

# Start fresh
docker-compose up -d
```

### Issue: PostgreSQL connection refused
**Solution:**
```bash
# Check container logs
docker logs f1_postgres

# Restart container
docker-compose restart postgres

# Wait for health check
docker ps  # Check STATUS shows "healthy"
```

---

## 📚 Resources Available

### Documentation
- `README.md` - Project overview and quick start
- `DOCUMENTATION.md` - Complete technical documentation with:
  - Technology stack matrix
  - 12-week sprint plan
  - User stories
  - Star schema design
  - Learning resources

### Configuration Files
- `environment.yml` - All Python dependencies
- `docker-compose.yml` - Full infrastructure setup
- `.env.example` - Environment variables template
- `init.sql` - Database initialization

### Ready to Code
- Project structure created
- All directories in place
- Docker configs ready
- Dataset downloaded

---

## 🎯 Success Metrics - Week 1

By end of Week 1, you should have:

1. ✅ Working Conda environment
2. ✅ All Docker services running
3. ✅ Data loaded and explored
4. ✅ First Polars notebook completed
5. ✅ Performance benchmarks documented
6. ✅ Git commits with progress

---

## 💡 Pro Tips

1. **Keep a daily log** - Document what you learn each day
2. **Commit often** - Small, frequent commits are better
3. **Test early** - Don't wait until the end to test integrations
4. **Ask for help** - Use Stack Overflow, course forums, or reach out to professors
5. **Stay organized** - Follow the sprint plan, but adapt as needed

---

## 🚀 Let's Start!

**Your project is 100% ready to go!**

Open your terminal and run:

```bash
cd /Users/herwin/Desktop/F1
conda env create -f environment.yml
conda activate f1_analytics
jupyter lab
```

---

## 📞 Need Help?

- **Webasignatura UCU**: Course forums
- **Professors**:
  - Ing. Bernardo Rychtenberg: bernardo.rychtenberg@ucu.edu.uy
  - Mag. Héctor Cotelo: hector.cotelo@ucu.edu.uy
- **Stack Overflow**: Tag your questions with `polars`, `dbt`, `apache-airflow`

---

## 🎉 You've Got This!

Everything is set up and ready. The hardest part (getting started) is done!

**Week 1 Sprint starts NOW!**

**¡Vamos! 🏎️💨**

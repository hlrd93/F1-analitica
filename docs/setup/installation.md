# 🚀 Installation Guide

## Prerequisites

Before starting, ensure you have:

- [x] **Python 3.10+**
- [x] **Conda/Miniconda** ([Download here](https://docs.conda.io/en/latest/miniconda.html))
- [x] **Docker & Docker Compose** ([Download here](https://www.docker.com/products/docker-desktop))
- [x] **Git**

---

## Quick Setup (5 Minutes)

### Step 1: Clone Repository

```bash
git clone https://github.com/herwin/f1-analytics.git
cd f1-analytics
```

### Step 2: Create Conda Environment

```bash
# Create environment from file
conda env create -f environment.yml

# Activate environment
conda activate f1_analytics

# Verify installation
python -c "import polars; print('✅ Polars:', polars.__version__)"
python -c "import pandas; print('✅ pandas:', pandas.__version__)"
```

### Step 3: Configure Environment Variables

```bash
# Copy example env file
cp .env.example .env

# Edit with your credentials (optional for local development)
# nano .env
```

### Step 4: Start Docker Services

```bash
# Start all services
docker-compose up -d

# Wait for services to be healthy
docker-compose ps

# Check logs if needed
docker-compose logs -f postgres
```

---

## Verify Installation

### Check Services

Access these URLs in your browser:

| Service | URL | Credentials |
|---------|-----|-------------|
| **Airflow** | http://localhost:8080 | admin/admin |
| **MLflow** | http://localhost:5000 | - |
| **Jupyter Lab** | http://localhost:8888 | Check terminal for token |
| **Streamlit** | http://localhost:8501 | - |

### Run Test Script

```python
# test_setup.py
import polars as pl
import pandas as pd
from sqlalchemy import create_engine

print("✅ All imports successful!")

# Test Polars
df = pl.DataFrame({"a": [1, 2, 3]})
print(f"✅ Polars working: {df.shape}")

# Test database connection
engine = create_engine("postgresql://f1user:f1pass@localhost:5432/f1_analytics")
with engine.connect() as conn:
    result = conn.execute("SELECT 1")
    print("✅ Database connection successful!")
```

```bash
python test_setup.py
```

---

## Data Setup

### Option 1: Use Existing Data (Recommended)

The F1 dataset is already in `/datasets` folder:

```bash
# Verify data exists
ls -lh datasets/*.csv

# Expected files:
# circuits.csv
# drivers.csv  
# races.csv
# results.csv
# ... (15 CSV files total)
```

### Option 2: Download Fresh Data

```bash
# Install Kaggle CLI (if not already)
pip install kaggle

# Configure Kaggle credentials
mkdir -p ~/.kaggle
# Copy your kaggle.json to ~/.kaggle/

# Download dataset
kaggle datasets download -d rohanrao/formula-1-world-championship-1950-2020

# Unzip to datasets folder
unzip formula-1-world-championship-1950-2020.zip -d datasets/
```

---

## Troubleshooting

### Issue: Conda environment creation fails

```bash
# Solution: Clean conda cache
conda clean --all

# Try with mamba (faster)
conda install mamba -c conda-forge
mamba env create -f environment.yml
```

### Issue: Docker containers won't start

```bash
# Solution: Check Docker is running
docker info

# Remove old containers
docker-compose down -v

# Start fresh
docker-compose up -d
```

### Issue: Port already in use

```bash
# Solution: Find process using port
lsof -i :8080  # Example for port 8080

# Kill process or change port in docker-compose.yml
```

### Issue: Permission denied (macOS)

```bash
# Solution: Grant Docker access to folders
# System Preferences → Privacy & Security → Files and Folders
# Enable Docker Desktop access
```

---

## Next Steps

Once installation is complete:

1. **[First Steps Guide](../setup/first-steps.md)** - Your first data exploration
2. **[Architecture Overview](../architecture/overview.md)** - Understand the system
3. **[Sprint 1 Tasks](../sprints/sprint-01-02.md)** - Start building!

---

## Uninstall

If you need to remove everything:

```bash
# Remove conda environment
conda deactivate
conda env remove -n f1_analytics

# Stop and remove Docker containers
docker-compose down -v

# Remove Docker images
docker-compose down --rmi all

# Remove project folder
cd ..
rm -rf f1-analytics
```

---

## Support

Having issues? Check:

- 📚 [Troubleshooting Guide](../resources/troubleshooting.md)
- 🐛 [GitHub Issues](https://github.com/herwin/f1-analytics/issues)
- 💬 Course Forums on Webasignatura UCU

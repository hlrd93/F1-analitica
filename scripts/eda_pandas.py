#!/usr/bin/env python3
"""
Small EDA script using pandas that:
- Iterates CSVs in `datasets/`
- For each file: computes shape, dtypes, missing value summary, numeric stats, top value counts for categorical cols
- Saves per-file markdown sections and plots (histograms, missingness bar) into `datasets/figures/`
- Writes a consolidated `datasets/eda_report.md`

Notes:
- For large files (>200k rows) it uses a sample (n=200k) to compute stats to avoid memory spikes.
- Requires: pandas, matplotlib, seaborn (all commonly in env). If not present, install with pip/conda.
"""
import os
import pandas as pd

# Optional plotting libs. If unavailable (numpy/matplotlib mismatch), we skip plots
HAVE_PLOT = True
try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import seaborn as sns
except Exception as err:
    HAVE_PLOT = False
    plt = None
    sns = None
    print(f"[WARN] plotting disabled: {err}")

BASE = os.path.join(os.getcwd(), 'datasets')
OUT_MD = os.path.join(BASE, 'eda_report.md')
FIG_DIR = os.path.join(BASE, 'figures')
os.makedirs(FIG_DIR, exist_ok=True)

CSV_FILES = sorted([f for f in os.listdir(BASE) if f.lower().endswith('.csv')])

# thresholds
FULL_THRESHOLD = 200_000  # filas por debajo de las cuales se carga completo
SAMPLE_N = 200_000
CAT_TOP = 10

md_lines = []
md_lines.append('# EDA con pandas — datasets/')
md_lines.append('> Reporte generado automáticamente por `scripts/eda_pandas.py`.')
md_lines.append('')

for fname in CSV_FILES:
    path = os.path.join(BASE, fname)
    md_lines.append(f'## {fname}')
    md_lines.append(f'- Ruta: `{path}`')
    size = os.path.getsize(path)
    md_lines.append(f'- Tamaño en disco: {size:,} bytes')

    # count rows by streaming
    try:
        with open(path, 'rb') as f:
            row_count = sum(1 for _ in f) - 1
            if row_count < 0:
                row_count = 0
    except Exception:
        row_count = None
    md_lines.append(f'- Filas (conteo líneas): {row_count if row_count is not None else "desconocido"}')

    # Decide read mode
    read_full = row_count is not None and row_count <= FULL_THRESHOLD
    try:
        if read_full:
            df = pd.read_csv(path)
            sampled = df
            md_lines.append('- Lectura: completa')
        else:
            sampled = pd.read_csv(path, nrows=SAMPLE_N)
            df = None
            md_lines.append(f'- Lectura: muestra (nrows={SAMPLE_N}) para estimaciones')
    except Exception as e:
        md_lines.append(f'- ERROR al leer: {e}')
        md_lines.append('')
        continue

    # Basic shape / columns
    md_lines.append(f'- Columnas detectadas: {len(sampled.columns)}')
    md_lines.append(f'- Columnas (primeras 20): {", ".join(list(sampled.columns[:20]))}{"..." if len(sampled.columns)>20 else ""}')

    # Dtypes
    md_lines.append('### Tipos de datos (muestra)')
    dtypes = sampled.dtypes.astype(str).to_dict()
    for c, t in dtypes.items():
        md_lines.append(f'- `{c}`: `{t}`')

    # Missingness summary
    md_lines.append('### Valores faltantes')
    nulls = sampled.isna().sum()
    nulls_pct = (nulls / len(sampled)).sort_values(ascending=False)
    top_nulls = nulls_pct[nulls_pct > 0].head(10)
    if top_nulls.empty:
        md_lines.append('- No se detectaron nulos en la muestra.')
    else:
        for col, pct in top_nulls.items():
            md_lines.append(f'- `{col}`: {int(nulls[col])} nulos — {pct:.2%} de la muestra')

    # Save missingness bar plot for top null cols (if plotting available)
    if not top_nulls.empty and HAVE_PLOT:
        try:
            plt.figure(figsize=(8, max(2, len(top_nulls)*0.5)))
            sns.barplot(x=top_nulls.values, y=list(top_nulls.index))
            plt.xlabel('Porcentaje de nulos (muestra)')
            plt.tight_layout()
            fig_path = os.path.join(FIG_DIR, f'{fname}_missing.png')
            plt.savefig(fig_path)
            plt.close()
            md_lines.append(f'![missing]({os.path.relpath(fig_path, BASE)})')
        except Exception as err:
            md_lines.append(f'- [WARN] No fue posible generar figura de nulos: {err}')
    elif not top_nulls.empty:
        md_lines.append('- [INFO] matplotlib/seaborn no disponible — figura de nulos omitida.')

    # Numeric summary
    num_cols = sampled.select_dtypes(include=['number']).columns.tolist()
    md_lines.append('### Estadísticas numéricas (muestra)')
    if num_cols:
        desc = sampled[num_cols].describe().T
        # write as markdown table (limited)
        md_lines.append('| columna | count | mean | std | min | 25% | 50% | 75% | max |')
        md_lines.append('|---:|---:|---:|---:|---:|---:|---:|---:|---:|')
        for col in desc.index:
            r = desc.loc[col]
            md_lines.append(f'| `{col}` | {int(r["count"]):,} | {r["mean"]:.3f} | {r["std"]:.3f} | {r["min"]:.3f} | {r["25%"]:.3f} | {r["50%"]:.3f} | {r["75%"]:.3f} | {r["max"]:.3f} |')

        # Save histogram for first up to 6 numeric cols
        plot_cols = num_cols[:6]
        if plot_cols:
            if HAVE_PLOT:
                try:
                    n = len(plot_cols)
                    cols = min(3, n)
                    rows = (n + cols - 1) // cols
                    fig, axes = plt.subplots(rows, cols, figsize=(4*cols, 3*rows))
                    axes = axes.flatten() if hasattr(axes, 'flatten') else [axes]
                    for i, c in enumerate(plot_cols):
                        sns.histplot(sampled[c].dropna(), ax=axes[i], kde=False, bins=30)
                        axes[i].set_title(c)
                    for j in range(i+1, len(axes)):
                        fig.delaxes(axes[j])
                    plt.tight_layout()
                    fig_path = os.path.join(FIG_DIR, f'{fname}_numeric_hist.png')
                    fig.savefig(fig_path)
                    plt.close(fig)
                    md_lines.append(f'![numeric hist]({os.path.relpath(fig_path, BASE)})')
                except Exception as err:
                    md_lines.append(f'- [WARN] No fue posible generar histogramas: {err}')
            else:
                md_lines.append('- [INFO] matplotlib/seaborn no disponible — histogramas omitidos.')
    else:
        md_lines.append('- No se detectaron columnas numéricas en la muestra.')

    # Categorical top values
    cat_cols = sampled.select_dtypes(include=['object', 'category']).columns.tolist()
    md_lines.append('### Top valores en columnas categóricas (muestra)')
    if cat_cols:
        for c in cat_cols[:10]:
            vc = sampled[c].value_counts(dropna=False).head(CAT_TOP)
            md_lines.append(f'- `{c}`:')
            for v, cnt in vc.items():
                md_lines.append(f'  - `{str(v)[:80]}`: {int(cnt)}')
    else:
        md_lines.append('- No se detectaron columnas categóricas en la muestra.')

    # Correlation matrix for numeric (if enough cols)
    if len(num_cols) >= 2:
        if HAVE_PLOT:
            try:
                corr = sampled[num_cols].corr()
                corr_path = os.path.join(FIG_DIR, f'{fname}_corr.png')
                plt.figure(figsize=(max(6, len(num_cols)*0.3), max(6, len(num_cols)*0.3)))
                sns.heatmap(corr, cmap='vlag', center=0, annot=False)
                plt.title('Correlation matrix (muestra)')
                plt.tight_layout()
                plt.savefig(corr_path)
                plt.close()
                md_lines.append(f'![corr]({os.path.relpath(corr_path, BASE)})')
            except Exception as err:
                md_lines.append(f'- [WARN] No fue posible generar matriz de correlación: {err}')
        else:
            md_lines.append('- [INFO] matplotlib/seaborn no disponible — matriz de correlación omitida.')

    # If we read full df, add some exact checks for candidate keys
    if df is not None:
        md_lines.append('### Chequeos exactos (archivo completo)')
        # Try detect id-like columns (ending with id or _id)
        id_candidates = [c for c in df.columns if c.lower().endswith('id') or c.lower().endswith('_id')]
        if id_candidates:
            for c in id_candidates:
                unique = df[c].nunique()
                rows = len(df)
                md_lines.append(f'- `{c}`: {unique} únicos en {rows} filas — unicidad: {unique==rows}')
        else:
            md_lines.append('- No se detectaron columnas con patrón `id` o `_id`.')

    md_lines.append('\n---\n')

# Overall notes
md_lines.append('## Notas generales')
md_lines.append('- El script usa muestras para archivos grandes; para análisis exactos, carga los archivos completos si tu máquina tiene memoria suficiente.')
md_lines.append('- Las figuras se guardaron en `datasets/figures/` (rutas relativas en el informe).')

# Write the report
with open(OUT_MD, 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines))

print(f'EDA completado — reporte: {OUT_MD} — figuras en: {FIG_DIR}')

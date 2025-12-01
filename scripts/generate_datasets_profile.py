#!/usr/bin/env python3
import os
import pandas as pd

BASE = os.path.join(os.getcwd(), 'datasets')
OUT = os.path.join(BASE, 'README.md')
files = [f for f in os.listdir(BASE) if f.lower().endswith('.csv')]

md = []
md.append('# Profiling rápido de los datos en `datasets/`')
md.append('> Informe automático: resumen por archivo con conteos, dtypes, nulos y muestras.\n')

for fname in sorted(files):
    path = os.path.join(BASE, fname)
    size = os.path.getsize(path)

    # Cuenta eficiente de filas (sin cargar todo en memoria)
    try:
        with open(path, 'rb') as f:
            row_count = sum(1 for _ in f) - 1  # resta header
            if row_count < 0:
                row_count = 0
    except Exception as e:
        row_count = None

    # Leer una muestra razonable para dtypes y primeras filas
    sample_n = 1000
    try:
        sample = pd.read_csv(path, nrows=sample_n)
    except Exception as e:
        sample = None

    # Si el archivo es pequeño, leer todo para conteos exactos de nulos y únicos
    full_threshold = 200_000
    exact = False
    try:
        if row_count is not None and row_count <= full_threshold:
            df = pd.read_csv(path)
            exact = True
        else:
            df = None
    except Exception:
        df = None

    md.append(f'## {fname}')
    md.append(f'- Ruta: `{path}`')
    md.append(f'- Tamaño en disco: {size:,} bytes')
    md.append(f'- Filas (conteo por líneas): {row_count if row_count is not None else "desconocido"}')

    if sample is not None:
        cols = list(sample.columns)
        md.append(f'- Columnas (muestra): {len(cols)} — {", ".join(cols[:10])}{"..." if len(cols)>10 else ""}')
        dtypes = sample.dtypes.astype(str).to_dict()
        md.append('- Tipos (muestra):')
        for c, t in dtypes.items():
            md.append(f'  - `{c}`: `{t}`')
    else:
        md.append('- Columnas: (no se pudo leer muestra)')

    if exact and df is not None:
        md.append('- Estadísticas (exactas):')
        total_cells = df.size
        total_nulls = int(df.isna().sum().sum())
        md.append(f'  - Celdas totales: {total_cells:,}, Nulos totales: {total_nulls:,} ({total_nulls/total_cells:.2%})')

        nulls = df.isna().sum().sort_values(ascending=False)
        top_nulls = nulls[nulls>0].head(10)
        if not top_nulls.empty:
            md.append('  - Columnas con más nulos:')
            for col, n in top_nulls.items():
                md.append(f'    - `{col}`: {int(n)} ({n/len(df):.2%} filas)')
        else:
            md.append('  - No se detectaron nulos en el dataset (muestra completa).')

        md.append('  - Valores únicos (top cols):')
        nunique = df.nunique().sort_values()
        top_nunique = nunique.tail(10)
        for col, u in top_nunique.items():
            md.append(f'    - `{col}`: {int(u)} valores únicos')

        mem = int(df.memory_usage(deep=True).sum())
        md.append(f'  - Memoria aproximada en RAM (pandas): {mem:,} bytes')

        md.append('  - Muestra (primeras 3 filas):')
        md.append('')
        md.append('```csv')
        md.append(df.head(3).to_csv(index=False))
        md.append('```')
    else:
        if sample is not None:
            md.append('- Estadísticas (estimadas sobre muestra):')
            total_cells = sample.size
            total_nulls = int(sample.isna().sum().sum())
            md.append(f'  - Celdas en muestra: {total_cells:,}, Nulos en muestra: {total_nulls:,} ({total_nulls/total_cells:.2%})')

            nulls = sample.isna().sum().sort_values(ascending=False)
            top_nulls = nulls[nulls>0].head(10)
            if not top_nulls.empty:
                md.append('  - Columnas con más nulos en la muestra:')
                for col, n in top_nulls.items():
                    md.append(f'    - `{col}`: {int(n)} ({n/len(sample):.2%} filas)')
            else:
                md.append('  - No se detectaron nulos en la muestra.')

            nunique = sample.nunique()
            small_uniques = {c: int(u) for c, u in nunique.items() if u <= 50}
            if small_uniques:
                md.append('  - Columnas con pocos valores únicos en la muestra (<=50):')
                for c, u in small_uniques.items():
                    md.append(f'    - `{c}`: {u} valores únicos')

            md.append('  - Muestra (primeras filas):')
            md.append('')
            md.append('```csv')
            md.append(sample.head(3).to_csv(index=False))
            md.append('```')
        else:
            md.append('- No fue posible extraer estadísticas para este archivo.')

    md.append('')

md.append('---')
md.append('## Recomendaciones rápidas')
md.append('- Revisar las columnas con alto porcentaje de nulos para decidir imputación o eliminación.')
md.append('- Verificar tipos de datos numéricos que vienen como strings (fechas, tiempos).')
md.append('- Para archivos grandes, usar procesamiento por chunks o Polars para EDA y transformaciones eficientes.')

output = '\n'.join(md)

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(output)

print(f'Perfil generado en: {OUT}')

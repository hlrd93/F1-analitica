CREATE TABLE IF NOT EXISTS analytics.dim_fecha (
  sk_fecha UInt32,
  fecha Date,
  dia UInt8,
  mes UInt8,
  anio UInt16,
  es_fin_de_semana UInt8,
  nombre_mes String,
  nombre_dia String
) ENGINE = MergeTree()
PARTITION BY toYYYYMM(fecha)
ORDER BY (sk_fecha)

-- sk_fecha convention: YYYYMMDD as UInt32, e.g. 20220530

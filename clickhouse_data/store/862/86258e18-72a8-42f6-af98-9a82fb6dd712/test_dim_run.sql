ATTACH TABLE _ UUID '317eb269-aace-4392-ad90-6b57f9d24394'
(
    `sk_fecha` UInt32,
    `fecha` Date,
    `dia` UInt8,
    `mes` UInt8,
    `anio` UInt16,
    `es_fin_de_semana` UInt8,
    `nombre_mes` String,
    `nombre_dia` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192

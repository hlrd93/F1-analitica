ATTACH VIEW _ UUID '8a95c6b5-025a-4e5d-9abd-a4f416250e1c'
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
AS SELECT
    toUInt32(replaceAll(toString(fecha), '-', '')) AS sk_fecha,
    fecha AS fecha,
    toUInt8(toDayOfMonth(fecha)) AS dia,
    toUInt8(toMonth(fecha)) AS mes,
    toUInt16(toYear(fecha)) AS anio,
    toUInt8(if(toDayOfWeek(fecha) IN (6, 7), 1, 0)) AS es_fin_de_semana,
    monthName(fecha) AS nombre_mes,
    toString(toDayOfWeek(fecha)) AS nombre_dia
FROM
(
    SELECT DISTINCT toDate(date) AS fecha
    FROM raw.raw_races
)

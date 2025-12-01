-- Dim table for dates. Materializes a date dimension from the races dataset.
SELECT
  toUInt32(replaceAll(toString(fecha), '-', '')) AS sk_fecha,
  fecha AS fecha,
  toUInt8(dayOfMonth(fecha)) AS dia,
  toUInt8(month(fecha)) AS mes,
  toUInt16(toYear(fecha)) AS anio,
  toUInt8(if(dayOfWeek(fecha) IN (6,7), 1, 0)) AS es_fin_de_semana,
  monthName(fecha) AS nombre_mes,
  toString(dayOfWeek(fecha)) AS nombre_dia
FROM (
  SELECT DISTINCT toDate(date) AS fecha FROM raw.raw_races
)

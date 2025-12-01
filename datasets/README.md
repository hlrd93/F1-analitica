# Profiling rápido de los datos en `datasets/`
> Informe automático: resumen por archivo con conteos, dtypes, nulos y muestras.

## circuits.csv
- Ruta: `/Users/herwin/Desktop/F1/datasets/circuits.csv`
- Tamaño en disco: 10,104 bytes
- Filas (conteo por líneas): 77
- Columnas (muestra): 9 — circuitId, circuitRef, name, location, country, lat, lng, alt, url
- Tipos (muestra):
  - `circuitId`: `int64`
  - `circuitRef`: `object`
  - `name`: `object`
  - `location`: `object`
  - `country`: `object`
  - `lat`: `float64`
  - `lng`: `float64`
  - `alt`: `int64`
  - `url`: `object`
- Estadísticas (exactas):
  - Celdas totales: 693, Nulos totales: 0 (0.00%)
  - No se detectaron nulos en el dataset (muestra completa).
  - Valores únicos (top cols):
    - `country`: 35 valores únicos
    - `alt`: 66 valores únicos
    - `location`: 75 valores únicos
    - `circuitId`: 77 valores únicos
    - `circuitRef`: 77 valores únicos
    - `name`: 77 valores únicos
    - `lat`: 77 valores únicos
    - `lng`: 77 valores únicos
    - `url`: 77 valores únicos
  - Memoria aproximada en RAM (pandas): 32,213 bytes
  - Muestra (primeras 3 filas):

```csv
circuitId,circuitRef,name,location,country,lat,lng,alt,url
1,albert_park,Albert Park Grand Prix Circuit,Melbourne,Australia,-37.8497,144.968,10,http://en.wikipedia.org/wiki/Melbourne_Grand_Prix_Circuit
2,sepang,Sepang International Circuit,Kuala Lumpur,Malaysia,2.76083,101.738,18,http://en.wikipedia.org/wiki/Sepang_International_Circuit
3,bahrain,Bahrain International Circuit,Sakhir,Bahrain,26.0325,50.5106,7,http://en.wikipedia.org/wiki/Bahrain_International_Circuit

```

## constructor_results.csv
- Ruta: `/Users/herwin/Desktop/F1/datasets/constructor_results.csv`
- Tamaño en disco: 219,365 bytes
- Filas (conteo por líneas): 12625
- Columnas (muestra): 5 — constructorResultsId, raceId, constructorId, points, status
- Tipos (muestra):
  - `constructorResultsId`: `int64`
  - `raceId`: `int64`
  - `constructorId`: `int64`
  - `points`: `int64`
  - `status`: `object`
- Estadísticas (exactas):
  - Celdas totales: 63,125, Nulos totales: 0 (0.00%)
  - No se detectaron nulos en el dataset (muestra completa).
  - Valores únicos (top cols):
    - `status`: 2 valores únicos
    - `points`: 61 valores únicos
    - `constructorId`: 175 valores únicos
    - `raceId`: 1060 valores únicos
    - `constructorResultsId`: 12625 valores únicos
  - Memoria aproximada en RAM (pandas): 1,148,986 bytes
  - Muestra (primeras 3 filas):

```csv
constructorResultsId,raceId,constructorId,points,status
1,18,1,14.0,\N
2,18,2,8.0,\N
3,18,3,9.0,\N

```

## constructor_standings.csv
- Ruta: `/Users/herwin/Desktop/F1/datasets/constructor_standings.csv`
- Tamaño en disco: 317,206 bytes
- Filas (conteo por líneas): 13391
- Columnas (muestra): 7 — constructorStandingsId, raceId, constructorId, points, position, positionText, wins
- Tipos (muestra):
  - `constructorStandingsId`: `int64`
  - `raceId`: `int64`
  - `constructorId`: `int64`
  - `points`: `int64`
  - `position`: `int64`
  - `positionText`: `object`
  - `wins`: `int64`
- Estadísticas (exactas):
  - Celdas totales: 93,737, Nulos totales: 0 (0.00%)
  - No se detectaron nulos en el dataset (muestra completa).
  - Valores únicos (top cols):
    - `position`: 22 valores únicos
    - `wins`: 22 valores únicos
    - `positionText`: 23 valores únicos
    - `constructorId`: 160 valores únicos
    - `points`: 579 valores únicos
    - `raceId`: 1061 valores únicos
    - `constructorStandingsId`: 13391 valores únicos
  - Memoria aproximada en RAM (pandas): 1,423,455 bytes
  - Muestra (primeras 3 filas):

```csv
constructorStandingsId,raceId,constructorId,points,position,positionText,wins
1,18,1,14.0,1,1,1
2,18,2,8.0,3,3,0
3,18,3,9.0,2,2,0

```

## constructors.csv
- Ruta: `/Users/herwin/Desktop/F1/datasets/constructors.csv`
- Tamaño en disco: 17,478 bytes
- Filas (conteo por líneas): 212
- Columnas (muestra): 5 — constructorId, constructorRef, name, nationality, url
- Tipos (muestra):
  - `constructorId`: `int64`
  - `constructorRef`: `object`
  - `name`: `object`
  - `nationality`: `object`
  - `url`: `object`
- Estadísticas (exactas):
  - Celdas totales: 1,060, Nulos totales: 0 (0.00%)
  - No se detectaron nulos en el dataset (muestra completa).
  - Valores únicos (top cols):
    - `nationality`: 24 valores únicos
    - `url`: 175 valores únicos
    - `constructorId`: 212 valores únicos
    - `constructorRef`: 212 valores únicos
    - `name`: 212 valores únicos
  - Memoria aproximada en RAM (pandas): 64,303 bytes
  - Muestra (primeras 3 filas):

```csv
constructorId,constructorRef,name,nationality,url
1,mclaren,McLaren,British,http://en.wikipedia.org/wiki/McLaren
2,bmw_sauber,BMW Sauber,German,http://en.wikipedia.org/wiki/BMW_Sauber
3,williams,Williams,British,http://en.wikipedia.org/wiki/Williams_Grand_Prix_Engineering

```

## driver_standings.csv
- Ruta: `/Users/herwin/Desktop/F1/datasets/driver_standings.csv`
- Tamaño en disco: 883,771 bytes
- Filas (conteo por líneas): 34863
- Columnas (muestra): 7 — driverStandingsId, raceId, driverId, points, position, positionText, wins
- Tipos (muestra):
  - `driverStandingsId`: `int64`
  - `raceId`: `int64`
  - `driverId`: `int64`
  - `points`: `int64`
  - `position`: `int64`
  - `positionText`: `int64`
  - `wins`: `int64`
- Estadísticas (exactas):
  - Celdas totales: 244,041, Nulos totales: 0 (0.00%)
  - No se detectaron nulos en el dataset (muestra completa).
  - Valores únicos (top cols):
    - `wins`: 20 valores únicos
    - `position`: 108 valores únicos
    - `positionText`: 109 valores únicos
    - `points`: 442 valores únicos
    - `driverId`: 854 valores únicos
    - `raceId`: 1125 valores únicos
    - `driverStandingsId`: 34863 valores únicos
  - Memoria aproximada en RAM (pandas): 3,720,368 bytes
  - Muestra (primeras 3 filas):

```csv
driverStandingsId,raceId,driverId,points,position,positionText,wins
1,18,1,10.0,1,1,1
2,18,2,8.0,2,2,0
3,18,3,6.0,3,3,0

```

## drivers.csv
- Ruta: `/Users/herwin/Desktop/F1/datasets/drivers.csv`
- Tamaño en disco: 94,367 bytes
- Filas (conteo por líneas): 861
- Columnas (muestra): 9 — driverId, driverRef, number, code, forename, surname, dob, nationality, url
- Tipos (muestra):
  - `driverId`: `int64`
  - `driverRef`: `object`
  - `number`: `object`
  - `code`: `object`
  - `forename`: `object`
  - `surname`: `object`
  - `dob`: `object`
  - `nationality`: `object`
  - `url`: `object`
- Estadísticas (exactas):
  - Celdas totales: 7,749, Nulos totales: 0 (0.00%)
  - No se detectaron nulos en el dataset (muestra completa).
  - Valores únicos (top cols):
    - `nationality`: 43 valores únicos
    - `number`: 49 valores únicos
    - `code`: 98 valores únicos
    - `forename`: 478 valores únicos
    - `surname`: 802 valores únicos
    - `dob`: 843 valores únicos
    - `driverId`: 861 valores únicos
    - `driverRef`: 861 valores únicos
    - `url`: 861 valores únicos
  - Memoria aproximada en RAM (pandas): 475,123 bytes
  - Muestra (primeras 3 filas):

```csv
driverId,driverRef,number,code,forename,surname,dob,nationality,url
1,hamilton,44,HAM,Lewis,Hamilton,1985-01-07,British,http://en.wikipedia.org/wiki/Lewis_Hamilton
2,heidfeld,\N,HEI,Nick,Heidfeld,1977-05-10,German,http://en.wikipedia.org/wiki/Nick_Heidfeld
3,rosberg,6,ROS,Nico,Rosberg,1985-06-27,German,http://en.wikipedia.org/wiki/Nico_Rosberg

```

## lap_times.csv
- Ruta: `/Users/herwin/Desktop/F1/datasets/lap_times.csv`
- Tamaño en disco: 17,622,395 bytes
- Filas (conteo por líneas): 589081
- Columnas (muestra): 6 — raceId, driverId, lap, position, time, milliseconds
- Tipos (muestra):
  - `raceId`: `int64`
  - `driverId`: `int64`
  - `lap`: `int64`
  - `position`: `int64`
  - `time`: `object`
  - `milliseconds`: `int64`
- Estadísticas (estimadas sobre muestra):
  - Celdas en muestra: 6,000, Nulos en muestra: 0 (0.00%)
  - No se detectaron nulos en la muestra.
  - Columnas con pocos valores únicos en la muestra (<=50):
    - `raceId`: 1 valores únicos
    - `driverId`: 20 valores únicos
    - `position`: 21 valores únicos
  - Muestra (primeras filas):

```csv
raceId,driverId,lap,position,time,milliseconds
841,20,1,1,1:38.109,98109
841,20,2,1,1:33.006,93006
841,20,3,1,1:32.713,92713

```

## pit_stops.csv
- Ruta: `/Users/herwin/Desktop/F1/datasets/pit_stops.csv`
- Tamaño en disco: 443,719 bytes
- Filas (conteo por líneas): 11371
- Columnas (muestra): 7 — raceId, driverId, stop, lap, time, duration, milliseconds
- Tipos (muestra):
  - `raceId`: `int64`
  - `driverId`: `int64`
  - `stop`: `int64`
  - `lap`: `int64`
  - `time`: `object`
  - `duration`: `object`
  - `milliseconds`: `int64`
- Estadísticas (exactas):
  - Celdas totales: 79,597, Nulos totales: 0 (0.00%)
  - No se detectaron nulos en el dataset (muestra completa).
  - Valores únicos (top cols):
    - `stop`: 14 valores únicos
    - `lap`: 74 valores únicos
    - `driverId`: 76 valores únicos
    - `raceId`: 285 valores únicos
    - `duration`: 7604 valores únicos
    - `milliseconds`: 7604 valores únicos
    - `time`: 8227 valores únicos
  - Memoria aproximada en RAM (pandas): 1,911,950 bytes
  - Muestra (primeras 3 filas):

```csv
raceId,driverId,stop,lap,time,duration,milliseconds
841,153,1,1,17:05:23,26.898,26898
841,30,1,1,17:05:52,25.021,25021
841,17,1,11,17:20:48,23.426,23426

```

## qualifying.csv
- Ruta: `/Users/herwin/Desktop/F1/datasets/qualifying.csv`
- Tamaño en disco: 465,231 bytes
- Filas (conteo por líneas): 10494
- Columnas (muestra): 9 — qualifyId, raceId, driverId, constructorId, number, position, q1, q2, q3
- Tipos (muestra):
  - `qualifyId`: `int64`
  - `raceId`: `int64`
  - `driverId`: `int64`
  - `constructorId`: `int64`
  - `number`: `int64`
  - `position`: `int64`
  - `q1`: `object`
  - `q2`: `object`
  - `q3`: `object`
- Estadísticas (exactas):
  - Celdas totales: 94,446, Nulos totales: 68 (0.07%)
  - Columnas con más nulos:
    - `q3`: 46 (0.44% filas)
    - `q2`: 22 (0.21% filas)
  - Valores únicos (top cols):
    - `position`: 28 valores únicos
    - `constructorId`: 47 valores únicos
    - `number`: 58 valores únicos
    - `driverId`: 172 valores únicos
    - `raceId`: 494 valores únicos
    - `q3`: 3471 valores únicos
    - `q2`: 5474 valores únicos
    - `q1`: 9147 valores únicos
    - `qualifyId`: 10494 valores únicos
  - Memoria aproximada en RAM (pandas): 2,478,327 bytes
  - Muestra (primeras 3 filas):

```csv
qualifyId,raceId,driverId,constructorId,number,position,q1,q2,q3
1,18,1,1,22,1,1:26.572,1:25.187,1:26.714
2,18,9,2,4,2,1:26.103,1:25.315,1:26.869
3,18,5,1,23,3,1:25.664,1:25.452,1:27.079

```

## races.csv
- Ruta: `/Users/herwin/Desktop/F1/datasets/races.csv`
- Tamaño en disco: 164,344 bytes
- Filas (conteo por líneas): 1125
- Columnas (muestra): 18 — raceId, year, round, circuitId, name, date, time, url, fp1_date, fp1_time...
- Tipos (muestra):
  - `raceId`: `int64`
  - `year`: `int64`
  - `round`: `int64`
  - `circuitId`: `int64`
  - `name`: `object`
  - `date`: `object`
  - `time`: `object`
  - `url`: `object`
  - `fp1_date`: `object`
  - `fp1_time`: `object`
  - `fp2_date`: `object`
  - `fp2_time`: `object`
  - `fp3_date`: `object`
  - `fp3_time`: `object`
  - `quali_date`: `object`
  - `quali_time`: `object`
  - `sprint_date`: `object`
  - `sprint_time`: `object`
- Estadísticas (exactas):
  - Celdas totales: 20,250, Nulos totales: 0 (0.00%)
  - No se detectaron nulos en el dataset (muestra completa).
  - Valores únicos (top cols):
    - `name`: 54 valores únicos
    - `fp3_date`: 73 valores únicos
    - `year`: 75 valores únicos
    - `circuitId`: 77 valores únicos
    - `quali_date`: 91 valores únicos
    - `fp1_date`: 91 valores únicos
    - `fp2_date`: 91 valores únicos
    - `url`: 1125 valores únicos
    - `date`: 1125 valores únicos
    - `raceId`: 1125 valores únicos
  - Memoria aproximada en RAM (pandas): 1,057,764 bytes
  - Muestra (primeras 3 filas):

```csv
raceId,year,round,circuitId,name,date,time,url,fp1_date,fp1_time,fp2_date,fp2_time,fp3_date,fp3_time,quali_date,quali_time,sprint_date,sprint_time
1,2009,1,1,Australian Grand Prix,2009-03-29,06:00:00,http://en.wikipedia.org/wiki/2009_Australian_Grand_Prix,\N,\N,\N,\N,\N,\N,\N,\N,\N,\N
2,2009,2,2,Malaysian Grand Prix,2009-04-05,09:00:00,http://en.wikipedia.org/wiki/2009_Malaysian_Grand_Prix,\N,\N,\N,\N,\N,\N,\N,\N,\N,\N
3,2009,3,17,Chinese Grand Prix,2009-04-19,07:00:00,http://en.wikipedia.org/wiki/2009_Chinese_Grand_Prix,\N,\N,\N,\N,\N,\N,\N,\N,\N,\N

```

## results.csv
- Ruta: `/Users/herwin/Desktop/F1/datasets/results.csv`
- Tamaño en disco: 1,721,961 bytes
- Filas (conteo por líneas): 26759
- Columnas (muestra): 18 — resultId, raceId, driverId, constructorId, number, grid, position, positionText, positionOrder, points...
- Tipos (muestra):
  - `resultId`: `int64`
  - `raceId`: `int64`
  - `driverId`: `int64`
  - `constructorId`: `int64`
  - `number`: `int64`
  - `grid`: `int64`
  - `position`: `object`
  - `positionText`: `object`
  - `positionOrder`: `int64`
  - `points`: `int64`
  - `laps`: `int64`
  - `time`: `object`
  - `milliseconds`: `object`
  - `fastestLap`: `object`
  - `rank`: `object`
  - `fastestLapTime`: `object`
  - `fastestLapSpeed`: `object`
  - `statusId`: `int64`
- Estadísticas (exactas):
  - Celdas totales: 481,662, Nulos totales: 0 (0.00%)
  - No se detectaron nulos en el dataset (muestra completa).
  - Valores únicos (top cols):
    - `statusId`: 137 valores únicos
    - `laps`: 172 valores únicos
    - `constructorId`: 211 valores únicos
    - `driverId`: 861 valores únicos
    - `raceId`: 1125 valores únicos
    - `time`: 7411 valores únicos
    - `fastestLapTime`: 7474 valores únicos
    - `milliseconds`: 7639 valores únicos
    - `fastestLapSpeed`: 7725 valores únicos
    - `resultId`: 26759 valores únicos
  - Memoria aproximada en RAM (pandas): 16,265,369 bytes
  - Muestra (primeras 3 filas):

```csv
resultId,raceId,driverId,constructorId,number,grid,position,positionText,positionOrder,points,laps,time,milliseconds,fastestLap,rank,fastestLapTime,fastestLapSpeed,statusId
1,18,1,1,22,1,1,1,1,10.0,58,1:34:50.616,5690616,39,2,1:27.452,218.300,1
2,18,2,2,3,5,2,2,2,8.0,58,+5.478,5696094,41,3,1:27.739,217.586,1
3,18,3,3,7,7,3,3,3,6.0,58,+8.163,5698779,41,5,1:28.090,216.719,1

```

## seasons.csv
- Ruta: `/Users/herwin/Desktop/F1/datasets/seasons.csv`
- Tamaño en disco: 4,594 bytes
- Filas (conteo por líneas): 75
- Columnas (muestra): 2 — year, url
- Tipos (muestra):
  - `year`: `int64`
  - `url`: `object`
- Estadísticas (exactas):
  - Celdas totales: 150, Nulos totales: 0 (0.00%)
  - No se detectaron nulos en el dataset (muestra completa).
  - Valores únicos (top cols):
    - `year`: 75 valores únicos
    - `url`: 75 valores únicos
  - Memoria aproximada en RAM (pandas): 8,988 bytes
  - Muestra (primeras 3 filas):

```csv
year,url
2009,http://en.wikipedia.org/wiki/2009_Formula_One_season
2008,http://en.wikipedia.org/wiki/2008_Formula_One_season
2007,http://en.wikipedia.org/wiki/2007_Formula_One_season

```

## sprint_results.csv
- Ruta: `/Users/herwin/Desktop/F1/datasets/sprint_results.csv`
- Tamaño en disco: 24,732 bytes
- Filas (conteo por líneas): 360
- Columnas (muestra): 16 — resultId, raceId, driverId, constructorId, number, grid, position, positionText, positionOrder, points...
- Tipos (muestra):
  - `resultId`: `int64`
  - `raceId`: `int64`
  - `driverId`: `int64`
  - `constructorId`: `int64`
  - `number`: `int64`
  - `grid`: `int64`
  - `position`: `object`
  - `positionText`: `object`
  - `positionOrder`: `int64`
  - `points`: `int64`
  - `laps`: `int64`
  - `time`: `object`
  - `milliseconds`: `object`
  - `fastestLap`: `object`
  - `fastestLapTime`: `object`
  - `statusId`: `int64`
- Estadísticas (exactas):
  - Celdas totales: 5,760, Nulos totales: 0 (0.00%)
  - No se detectaron nulos en el dataset (muestra completa).
  - Valores únicos (top cols):
    - `grid`: 21 valores únicos
    - `position`: 21 valores únicos
    - `positionText`: 23 valores únicos
    - `fastestLap`: 24 valores únicos
    - `driverId`: 31 valores únicos
    - `number`: 33 valores únicos
    - `time`: 341 valores únicos
    - `milliseconds`: 341 valores únicos
    - `fastestLapTime`: 351 valores únicos
    - `resultId`: 360 valores únicos
  - Memoria aproximada en RAM (pandas): 161,399 bytes
  - Muestra (primeras 3 filas):

```csv
resultId,raceId,driverId,constructorId,number,grid,position,positionText,positionOrder,points,laps,time,milliseconds,fastestLap,fastestLapTime,statusId
1,1061,830,9,33,2,1,1,1,3,17,25:38.426,1538426,14,1:30.013,1
2,1061,1,131,44,1,2,2,2,2,17,+1.430,1539856,17,1:29.937,1
3,1061,822,131,77,3,3,3,3,1,17,+7.502,1545928,17,1:29.958,1

```

## status.csv
- Ruta: `/Users/herwin/Desktop/F1/datasets/status.csv`
- Tamaño en disco: 2,136 bytes
- Filas (conteo por líneas): 139
- Columnas (muestra): 2 — statusId, status
- Tipos (muestra):
  - `statusId`: `int64`
  - `status`: `object`
- Estadísticas (exactas):
  - Celdas totales: 278, Nulos totales: 0 (0.00%)
  - No se detectaron nulos en el dataset (muestra completa).
  - Valores únicos (top cols):
    - `statusId`: 139 valores únicos
    - `status`: 139 valores únicos
  - Memoria aproximada en RAM (pandas): 10,416 bytes
  - Muestra (primeras 3 filas):

```csv
statusId,status
1,Finished
2,Disqualified
3,Accident

```

---
## Recomendaciones rápidas
- Revisar las columnas con alto porcentaje de nulos para decidir imputación o eliminación.
- Verificar tipos de datos numéricos que vienen como strings (fechas, tiempos).
- Para archivos grandes, usar procesamiento por chunks o Polars para EDA y transformaciones eficientes.
# EDA con pandas — datasets/
> Reporte generado automáticamente por `scripts/eda_pandas.py`.

## circuits.csv
- Ruta: `/Users/herwin/Desktop/F1/datasets/circuits.csv`
- Tamaño en disco: 10,104 bytes
- Filas (conteo líneas): 77
- Lectura: completa
- Columnas detectadas: 9
- Columnas (primeras 20): circuitId, circuitRef, name, location, country, lat, lng, alt, url
### Tipos de datos (muestra)
- `circuitId`: `int64`
- `circuitRef`: `object`
- `name`: `object`
- `location`: `object`
- `country`: `object`
- `lat`: `float64`
- `lng`: `float64`
- `alt`: `int64`
- `url`: `object`
### Valores faltantes
- No se detectaron nulos en la muestra.
### Estadísticas numéricas (muestra)
| columna | count | mean | std | min | 25% | 50% | 75% | max |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `circuitId` | 77 | 39.883 | 23.002 | 1.000 | 20.000 | 40.000 | 59.000 | 80.000 |
| `lat` | 77 | 33.443 | 22.809 | -37.850 | 32.777 | 40.952 | 46.959 | 57.265 |
| `lng` | 77 | 1.077 | 65.517 | -118.189 | -9.394 | 3.931 | 19.249 | 144.968 |
| `alt` | 77 | 247.013 | 362.738 | -7.000 | 18.000 | 129.000 | 332.000 | 2227.000 |
- [INFO] matplotlib/seaborn no disponible — histogramas omitidos.
### Top valores en columnas categóricas (muestra)
- `circuitRef`:
  - `albert_park`: 1
  - `nivelles`: 1
  - `zeltweg`: 1
  - `george`: 1
  - `reims`: 1
  - `lemans`: 1
  - `essarts`: 1
  - `tremblant`: 1
  - `charade`: 1
  - `montjuic`: 1
- `name`:
  - `Albert Park Grand Prix Circuit`: 1
  - `Nivelles-Baulers`: 1
  - `Zeltweg`: 1
  - `Prince George Circuit`: 1
  - `Reims-Gueux`: 1
  - `Le Mans`: 1
  - `Rouen-Les-Essarts`: 1
  - `Circuit Mont-Tremblant`: 1
  - `Charade Circuit`: 1
  - `Montjuïc`: 1
- `location`:
  - `Barcelona`: 2
  - `California`: 2
  - `Melbourne`: 1
  - `Reims`: 1
  - `Le Mans`: 1
  - `Rouen`: 1
  - `Quebec`: 1
  - `Clermont-Ferrand`: 1
  - `Brussels`: 1
  - `Ontario`: 1
- `country`:
  - `USA`: 11
  - `France`: 7
  - `Spain`: 6
  - `Portugal`: 4
  - `UK`: 4
  - `Italy`: 4
  - `Japan`: 3
  - `Canada`: 3
  - `Germany`: 3
  - `Belgium`: 3
- `url`:
  - `http://en.wikipedia.org/wiki/Melbourne_Grand_Prix_Circuit`: 1
  - `http://en.wikipedia.org/wiki/Nivelles-Baulers`: 1
  - `http://en.wikipedia.org/wiki/Zeltweg_Airfield`: 1
  - `http://en.wikipedia.org/wiki/Prince_George_Circuit`: 1
  - `http://en.wikipedia.org/wiki/Reims-Gueux`: 1
  - `http://en.wikipedia.org/wiki/Circuit_de_la_Sarthe#Bugatti_Circuit`: 1
  - `http://en.wikipedia.org/wiki/Rouen-Les-Essarts`: 1
  - `http://en.wikipedia.org/wiki/Circuit_Mont-Tremblant`: 1
  - `http://en.wikipedia.org/wiki/Charade_Circuit`: 1
  - `http://en.wikipedia.org/wiki/Montju%C3%AFc_circuit`: 1
- [INFO] matplotlib/seaborn no disponible — matriz de correlación omitida.
### Chequeos exactos (archivo completo)
- `circuitId`: 77 únicos en 77 filas — unicidad: True

---

## constructor_results.csv
- Ruta: `/Users/herwin/Desktop/F1/datasets/constructor_results.csv`
- Tamaño en disco: 219,365 bytes
- Filas (conteo líneas): 12625
- Lectura: completa
- Columnas detectadas: 5
- Columnas (primeras 20): constructorResultsId, raceId, constructorId, points, status
### Tipos de datos (muestra)
- `constructorResultsId`: `int64`
- `raceId`: `int64`
- `constructorId`: `int64`
- `points`: `float64`
- `status`: `object`
### Valores faltantes
- No se detectaron nulos en la muestra.
### Estadísticas numéricas (muestra)
| columna | count | mean | std | min | 25% | 50% | 75% | max |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `constructorResultsId` | 12,625 | 8424.501 | 5666.311 | 1.000 | 3157.000 | 6313.000 | 13965.000 | 17129.000 |
| `raceId` | 12,625 | 528.236 | 314.794 | 1.000 | 287.000 | 487.000 | 751.000 | 1144.000 |
| `constructorId` | 12,625 | 45.956 | 59.468 | 1.000 | 6.000 | 22.000 | 54.000 | 215.000 |
| `points` | 12,625 | 4.054 | 7.862 | 0.000 | 0.000 | 0.000 | 5.000 | 66.000 |
- [INFO] matplotlib/seaborn no disponible — histogramas omitidos.
### Top valores en columnas categóricas (muestra)
- `status`:
  - `\N`: 12608
  - `D`: 17
- [INFO] matplotlib/seaborn no disponible — matriz de correlación omitida.
### Chequeos exactos (archivo completo)
- `constructorResultsId`: 12625 únicos en 12625 filas — unicidad: True
- `raceId`: 1060 únicos en 12625 filas — unicidad: False
- `constructorId`: 175 únicos en 12625 filas — unicidad: False

---

## constructor_standings.csv
- Ruta: `/Users/herwin/Desktop/F1/datasets/constructor_standings.csv`
- Tamaño en disco: 317,206 bytes
- Filas (conteo líneas): 13391
- Lectura: completa
- Columnas detectadas: 7
- Columnas (primeras 20): constructorStandingsId, raceId, constructorId, points, position, positionText, wins
### Tipos de datos (muestra)
- `constructorStandingsId`: `int64`
- `raceId`: `int64`
- `constructorId`: `int64`
- `points`: `float64`
- `position`: `int64`
- `positionText`: `object`
- `wins`: `int64`
### Valores faltantes
- No se detectaron nulos en la muestra.
### Estadísticas numéricas (muestra)
| columna | count | mean | std | min | 25% | 50% | 75% | max |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `constructorStandingsId` | 13,391 | 16982.111 | 8868.446 | 1.000 | 8883.500 | 20634.000 | 25047.500 | 28982.000 |
| `raceId` | 13,391 | 535.400 | 307.706 | 1.000 | 302.000 | 508.000 | 740.000 | 1144.000 |
| `constructorId` | 13,391 | 49.603 | 61.214 | 1.000 | 6.000 | 25.000 | 58.000 | 215.000 |
| `points` | 13,391 | 37.179 | 84.346 | 0.000 | 0.000 | 7.000 | 33.000 | 860.000 |
| `position` | 13,391 | 7.226 | 4.356 | 1.000 | 4.000 | 7.000 | 10.000 | 22.000 |
| `wins` | 13,391 | 0.697 | 1.880 | 0.000 | 0.000 | 0.000 | 0.000 | 21.000 |
- [INFO] matplotlib/seaborn no disponible — histogramas omitidos.
### Top valores en columnas categóricas (muestra)
- `positionText`:
  - `1`: 1061
  - `3`: 1061
  - `2`: 1061
  - `4`: 1060
  - `5`: 1060
  - `6`: 1060
  - `7`: 1056
  - `8`: 1044
  - `9`: 1030
  - `10`: 999
- [INFO] matplotlib/seaborn no disponible — matriz de correlación omitida.
### Chequeos exactos (archivo completo)
- `constructorStandingsId`: 13391 únicos en 13391 filas — unicidad: True
- `raceId`: 1061 únicos en 13391 filas — unicidad: False
- `constructorId`: 160 únicos en 13391 filas — unicidad: False

---

## constructors.csv
- Ruta: `/Users/herwin/Desktop/F1/datasets/constructors.csv`
- Tamaño en disco: 17,478 bytes
- Filas (conteo líneas): 212
- Lectura: completa
- Columnas detectadas: 5
- Columnas (primeras 20): constructorId, constructorRef, name, nationality, url
### Tipos de datos (muestra)
- `constructorId`: `int64`
- `constructorRef`: `object`
- `name`: `object`
- `nationality`: `object`
- `url`: `object`
### Valores faltantes
- No se detectaron nulos en la muestra.
### Estadísticas numéricas (muestra)
| columna | count | mean | std | min | 25% | 50% | 75% | max |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `constructorId` | 212 | 107.547 | 61.953 | 1.000 | 54.750 | 107.500 | 160.250 | 215.000 |
- [INFO] matplotlib/seaborn no disponible — histogramas omitidos.
### Top valores en columnas categóricas (muestra)
- `constructorRef`:
  - `mclaren`: 1
  - `pawl`: 1
  - `arzani-volpini`: 1
  - `nichels`: 1
  - `bromme`: 1
  - `klenk`: 1
  - `simca`: 1
  - `turner`: 1
  - `del_roy`: 1
  - `veritas`: 1
- `name`:
  - `McLaren`: 1
  - `Pawl`: 1
  - `Arzani-Volpini`: 1
  - `Nichels`: 1
  - `Bromme`: 1
  - `Klenk`: 1
  - `Simca`: 1
  - `Turner`: 1
  - `Del Roy`: 1
  - `Veritas`: 1
- `nationality`:
  - `British`: 86
  - `American`: 39
  - `Italian`: 30
  - `French`: 13
  - `German`: 10
  - `Japanese`: 5
  - `Swiss`: 5
  - `South African`: 3
  - `Dutch`: 3
  - `Canadian`: 2
- `url`:
  - `http://en.wikipedia.org/wiki/Cooper_Car_Company`: 11
  - `http://en.wikipedia.org/wiki/Team_Lotus`: 7
  - `http://en.wikipedia.org/wiki/Brabham`: 6
  - `http://en.wikipedia.org/wiki/De_Tomaso`: 4
  - `http://en.wikipedia.org/wiki/Shadow_Racing_Cars`: 3
  - `http://en.wikipedia.org/wiki/LDS_(automobile)`: 3
  - `http://en.wikipedia.org/wiki/Anglo_American_Racers`: 3
  - `http://en.wikipedia.org/wiki/March_Engineering`: 3
  - `http://en.wikipedia.org/wiki/McLaren_(racing)`: 2
  - `http://en.wikipedia.org/wiki/Midland_F1_Racing`: 2
### Chequeos exactos (archivo completo)
- `constructorId`: 212 únicos en 212 filas — unicidad: True

---

## driver_standings.csv
- Ruta: `/Users/herwin/Desktop/F1/datasets/driver_standings.csv`
- Tamaño en disco: 883,771 bytes
- Filas (conteo líneas): 34863
- Lectura: completa
- Columnas detectadas: 7
- Columnas (primeras 20): driverStandingsId, raceId, driverId, points, position, positionText, wins
### Tipos de datos (muestra)
- `driverStandingsId`: `int64`
- `raceId`: `int64`
- `driverId`: `int64`
- `points`: `float64`
- `position`: `int64`
- `positionText`: `object`
- `wins`: `int64`
### Valores faltantes
- No se detectaron nulos en la muestra.
### Estadísticas numéricas (muestra)
| columna | count | mean | std | min | 25% | 50% | 75% | max |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `driverStandingsId` | 34,863 | 43176.154 | 21934.277 | 1.000 | 19834.500 | 50044.000 | 62054.500 | 73270.000 |
| `raceId` | 34,863 | 584.414 | 292.276 | 1.000 | 354.000 | 603.000 | 805.000 | 1144.000 |
| `driverId` | 34,863 | 316.933 | 274.666 | 1.000 | 88.000 | 223.000 | 521.000 | 862.000 |
| `points` | 34,863 | 14.704 | 38.978 | 0.000 | 0.000 | 1.000 | 10.000 | 575.000 |
| `position` | 34,863 | 19.717 | 16.293 | 1.000 | 8.000 | 16.000 | 26.000 | 108.000 |
| `wins` | 34,863 | 0.277 | 1.033 | 0.000 | 0.000 | 0.000 | 0.000 | 19.000 |
- [INFO] matplotlib/seaborn no disponible — histogramas omitidos.
### Top valores en columnas categóricas (muestra)
- `positionText`:
  - `1`: 1125
  - `2`: 1125
  - `3`: 1125
  - `4`: 1125
  - `5`: 1125
  - `6`: 1125
  - `7`: 1125
  - `8`: 1124
  - `9`: 1121
  - `10`: 1119
- [INFO] matplotlib/seaborn no disponible — matriz de correlación omitida.
### Chequeos exactos (archivo completo)
- `driverStandingsId`: 34863 únicos en 34863 filas — unicidad: True
- `raceId`: 1125 únicos en 34863 filas — unicidad: False
- `driverId`: 854 únicos en 34863 filas — unicidad: False

---

## drivers.csv
- Ruta: `/Users/herwin/Desktop/F1/datasets/drivers.csv`
- Tamaño en disco: 94,367 bytes
- Filas (conteo líneas): 861
- Lectura: completa
- Columnas detectadas: 9
- Columnas (primeras 20): driverId, driverRef, number, code, forename, surname, dob, nationality, url
### Tipos de datos (muestra)
- `driverId`: `int64`
- `driverRef`: `object`
- `number`: `object`
- `code`: `object`
- `forename`: `object`
- `surname`: `object`
- `dob`: `object`
- `nationality`: `object`
- `url`: `object`
### Valores faltantes
- No se detectaron nulos en la muestra.
### Estadísticas numéricas (muestra)
| columna | count | mean | std | min | 25% | 50% | 75% | max |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `driverId` | 861 | 431.062 | 248.794 | 1.000 | 216.000 | 431.000 | 646.000 | 862.000 |
- [INFO] matplotlib/seaborn no disponible — histogramas omitidos.
### Top valores en columnas categóricas (muestra)
- `driverRef`:
  - `hamilton`: 1
  - `shelby`: 1
  - `fontes`: 1
  - `ashdown`: 1
  - `bill_moss`: 1
  - `dennis_taylor`: 1
  - `blanchard`: 1
  - `tomaso`: 1
  - `constantine`: 1
  - `said`: 1
- `number`:
  - `\N`: 802
  - `22`: 2
  - `99`: 2
  - `21`: 2
  - `2`: 2
  - `10`: 2
  - `4`: 2
  - `9`: 2
  - `88`: 2
  - `28`: 2
- `code`:
  - `\N`: 757
  - `BIA`: 2
  - `MSC`: 2
  - `HAR`: 2
  - `MAG`: 2
  - `VER`: 2
  - `ALB`: 2
  - `DOO`: 2
  - `BOT`: 1
  - `NAS`: 1
- `forename`:
  - `John`: 14
  - `Mike`: 14
  - `Peter`: 13
  - `Bill`: 11
  - `Tony`: 11
  - `Bob`: 10
  - `David`: 10
  - `Paul`: 9
  - `Johnny`: 9
  - `George`: 8
- `surname`:
  - `Taylor`: 5
  - `Wilson`: 4
  - `Fittipaldi`: 4
  - `Stewart`: 3
  - `Russo`: 3
  - `Schumacher`: 3
  - `Brown`: 3
  - `Brabham`: 3
  - `Hill`: 3
  - `Winkelhock`: 3
- `dob`:
  - `1919-10-28`: 2
  - `1946-12-12`: 2
  - `1932-05-05`: 2
  - `1919-09-30`: 2
  - `1929-06-13`: 2
  - `1915-10-26`: 2
  - `1920-02-16`: 2
  - `1942-05-27`: 2
  - `1931-05-18`: 2
  - `1937-04-26`: 2
- `nationality`:
  - `British`: 166
  - `American`: 158
  - `Italian`: 99
  - `French`: 73
  - `German`: 50
  - `Brazilian`: 32
  - `Argentine`: 24
  - `Belgian`: 23
  - `Swiss`: 23
  - `South African`: 23
- `url`:
  - `http://en.wikipedia.org/wiki/Lewis_Hamilton`: 1
  - `http://en.wikipedia.org/wiki/Carroll_Shelby`: 1
  - `http://en.wikipedia.org/wiki/Azdrubal_Fontes`: 1
  - `http://en.wikipedia.org/wiki/Peter_Ashdown`: 1
  - `http://en.wikipedia.org/wiki/Bill_Moss_(racing_driver)`: 1
  - `http://en.wikipedia.org/wiki/Dennis_Taylor_(racing_driver)`: 1
  - `http://en.wikipedia.org/wiki/Harry_Blanchard`: 1
  - `http://en.wikipedia.org/wiki/Alessandro_de_Tomaso`: 1
  - `http://en.wikipedia.org/wiki/George_Constantine`: 1
  - `http://en.wikipedia.org/wiki/Bob_Said`: 1
### Chequeos exactos (archivo completo)
- `driverId`: 861 únicos en 861 filas — unicidad: True

---

## lap_times.csv
- Ruta: `/Users/herwin/Desktop/F1/datasets/lap_times.csv`
- Tamaño en disco: 17,622,395 bytes
- Filas (conteo líneas): 589081
- Lectura: muestra (nrows=200000) para estimaciones
- Columnas detectadas: 6
- Columnas (primeras 20): raceId, driverId, lap, position, time, milliseconds
### Tipos de datos (muestra)
- `raceId`: `int64`
- `driverId`: `int64`
- `lap`: `int64`
- `position`: `int64`
- `time`: `object`
- `milliseconds`: `int64`
### Valores faltantes
- No se detectaron nulos en la muestra.
### Estadísticas numéricas (muestra)
| columna | count | mean | std | min | 25% | 50% | 75% | max |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `raceId` | 200,000 | 589.701 | 345.135 | 141.000 | 202.000 | 851.000 | 893.000 | 949.000 |
| `driverId` | 200,000 | 240.758 | 342.274 | 1.000 | 18.000 | 54.000 | 807.000 | 838.000 |
| `lap` | 200,000 | 29.547 | 18.312 | 1.000 | 14.000 | 28.000 | 44.000 | 78.000 |
| `position` | 200,000 | 9.828 | 5.740 | 1.000 | 5.000 | 9.000 | 14.000 | 24.000 |
| `milliseconds` | 200,000 | 98761.538 | 97590.281 | 71235.000 | 84793.000 | 93128.000 | 105271.250 | 7507547.000 |
- [INFO] matplotlib/seaborn no disponible — histogramas omitidos.
### Top valores en columnas categóricas (muestra)
- `time`:
  - `1:22.306`: 21
  - `1:31.793`: 19
  - `1:21.477`: 18
  - `1:29.856`: 17
  - `1:22.111`: 17
  - `1:30.207`: 17
  - `1:22.154`: 17
  - `1:22.303`: 17
  - `1:29.689`: 17
  - `1:30.526`: 17
- [INFO] matplotlib/seaborn no disponible — matriz de correlación omitida.

---

## pit_stops.csv
- Ruta: `/Users/herwin/Desktop/F1/datasets/pit_stops.csv`
- Tamaño en disco: 443,719 bytes
- Filas (conteo líneas): 11371
- Lectura: completa
- Columnas detectadas: 7
- Columnas (primeras 20): raceId, driverId, stop, lap, time, duration, milliseconds
### Tipos de datos (muestra)
- `raceId`: `int64`
- `driverId`: `int64`
- `stop`: `int64`
- `lap`: `int64`
- `time`: `object`
- `duration`: `object`
- `milliseconds`: `int64`
### Valores faltantes
- No se detectaron nulos en la muestra.
### Estadísticas numéricas (muestra)
| columna | count | mean | std | min | 25% | 50% | 75% | max |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `raceId` | 11,371 | 981.195 | 92.327 | 841.000 | 895.000 | 971.000 | 1065.000 | 1144.000 |
| `driverId` | 11,371 | 549.735 | 383.735 | 1.000 | 20.000 | 817.000 | 835.000 | 862.000 |
| `stop` | 11,371 | 1.788 | 1.521 | 1.000 | 1.000 | 2.000 | 2.000 | 70.000 |
| `lap` | 11,371 | 25.387 | 14.831 | 1.000 | 13.000 | 25.000 | 36.000 | 78.000 |
| `milliseconds` | 11,371 | 85230.496 | 310427.261 | 12897.000 | 21937.500 | 23606.000 | 26544.000 | 3069017.000 |
- [INFO] matplotlib/seaborn no disponible — histogramas omitidos.
### Top valores en columnas categóricas (muestra)
- `time`:
  - `14:22:38`: 6
  - `15:08:45`: 6
  - `15:06:11`: 6
  - `15:05:16`: 6
  - `14:42:01`: 5
  - `14:45:06`: 5
  - `15:43:41`: 5
  - `15:07:43`: 5
  - `15:06:01`: 5
  - `15:05:15`: 5
- `duration`:
  - `22.534`: 8
  - `22.684`: 7
  - `22.745`: 7
  - `22.028`: 6
  - `22.616`: 6
  - `22.030`: 6
  - `24.083`: 6
  - `22.303`: 6
  - `22.241`: 6
  - `22.963`: 6
- [INFO] matplotlib/seaborn no disponible — matriz de correlación omitida.
### Chequeos exactos (archivo completo)
- `raceId`: 285 únicos en 11371 filas — unicidad: False
- `driverId`: 76 únicos en 11371 filas — unicidad: False

---

## qualifying.csv
- Ruta: `/Users/herwin/Desktop/F1/datasets/qualifying.csv`
- Tamaño en disco: 465,231 bytes
- Filas (conteo líneas): 10494
- Lectura: completa
- Columnas detectadas: 9
- Columnas (primeras 20): qualifyId, raceId, driverId, constructorId, number, position, q1, q2, q3
### Tipos de datos (muestra)
- `qualifyId`: `int64`
- `raceId`: `int64`
- `driverId`: `int64`
- `constructorId`: `int64`
- `number`: `int64`
- `position`: `int64`
- `q1`: `object`
- `q2`: `object`
- `q3`: `object`
### Valores faltantes
- `q3`: 46 nulos — 0.44% de la muestra
- `q2`: 22 nulos — 0.21% de la muestra
- [INFO] matplotlib/seaborn no disponible — figura de nulos omitida.
### Estadísticas numéricas (muestra)
| columna | count | mean | std | min | 25% | 50% | 75% | max |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `qualifyId` | 10,494 | 5262.483 | 3046.588 | 1.000 | 2625.250 | 5249.500 | 7893.750 | 10551.000 |
| `raceId` | 10,494 | 624.601 | 428.298 | 1.000 | 160.000 | 870.000 | 1006.000 | 1144.000 |
| `driverId` | 10,494 | 343.002 | 389.586 | 1.000 | 17.000 | 60.000 | 822.000 | 862.000 |
| `constructorId` | 10,494 | 47.918 | 73.218 | 1.000 | 4.000 | 9.000 | 31.000 | 215.000 |
| `number` | 10,494 | 18.786 | 18.448 | 0.000 | 7.000 | 14.000 | 22.000 | 99.000 |
| `position` | 10,494 | 11.196 | 6.260 | 1.000 | 6.000 | 11.000 | 16.000 | 28.000 |
- [INFO] matplotlib/seaborn no disponible — histogramas omitidos.
### Top valores en columnas categóricas (muestra)
- `q1`:
  - `\N`: 156
  - `1:20.382`: 4
  - `1:17.244`: 4
  - `1:20.888`: 4
  - `1:27.323`: 3
  - `1:17.502`: 3
  - `1:14.412`: 3
  - `1:22.742`: 3
  - `1:15.923`: 3
  - `1:23.224`: 3
- `q2`:
  - `\N`: 4625
  - `nan`: 22
  - `1:26.161`: 3
  - `1:15.974`: 3
  - `1:15.885`: 3
  - `1:16.687`: 3
  - `1:17.571`: 3
  - `1:12.188`: 3
  - `1:17.166`: 3
  - `1:46.328`: 3
- `q3`:
  - `\N`: 6819
  - `nan`: 46
  - `1:31.478`: 3
  - `1:38.513`: 3
  - `1:33.008`: 3
  - `1:35.766`: 3
  - `1:14.970`: 3
  - `1:45.503`: 3
  - `1:47.216`: 2
  - `1:35.364`: 2
- [INFO] matplotlib/seaborn no disponible — matriz de correlación omitida.
### Chequeos exactos (archivo completo)
- `qualifyId`: 10494 únicos en 10494 filas — unicidad: True
- `raceId`: 494 únicos en 10494 filas — unicidad: False
- `driverId`: 172 únicos en 10494 filas — unicidad: False
- `constructorId`: 47 únicos en 10494 filas — unicidad: False

---

## races.csv
- Ruta: `/Users/herwin/Desktop/F1/datasets/races.csv`
- Tamaño en disco: 164,344 bytes
- Filas (conteo líneas): 1125
- Lectura: completa
- Columnas detectadas: 18
- Columnas (primeras 20): raceId, year, round, circuitId, name, date, time, url, fp1_date, fp1_time, fp2_date, fp2_time, fp3_date, fp3_time, quali_date, quali_time, sprint_date, sprint_time
### Tipos de datos (muestra)
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
### Valores faltantes
- No se detectaron nulos en la muestra.
### Estadísticas numéricas (muestra)
| columna | count | mean | std | min | 25% | 50% | 75% | max |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `raceId` | 1,125 | 565.710 | 328.814 | 1.000 | 282.000 | 563.000 | 845.000 | 1144.000 |
| `year` | 1,125 | 1992.703 | 20.604 | 1950.000 | 1977.000 | 1994.000 | 2011.000 | 2024.000 |
| `round` | 1,125 | 8.580 | 5.160 | 1.000 | 4.000 | 8.000 | 13.000 | 24.000 |
| `circuitId` | 1,125 | 23.890 | 19.634 | 1.000 | 9.000 | 18.000 | 34.000 | 80.000 |
- [INFO] matplotlib/seaborn no disponible — histogramas omitidos.
### Top valores en columnas categóricas (muestra)
- `name`:
  - `Italian Grand Prix`: 75
  - `British Grand Prix`: 75
  - `Monaco Grand Prix`: 70
  - `Belgian Grand Prix`: 69
  - `German Grand Prix`: 64
  - `French Grand Prix`: 62
  - `Spanish Grand Prix`: 54
  - `Canadian Grand Prix`: 53
  - `Brazilian Grand Prix`: 47
  - `United States Grand Prix`: 45
- `date`:
  - `2009-03-29`: 1
  - `1960-06-06`: 1
  - `1960-11-20`: 1
  - `1960-09-04`: 1
  - `1960-08-14`: 1
  - `1960-07-16`: 1
  - `1960-07-03`: 1
  - `1960-06-19`: 1
  - `1960-05-30`: 1
  - `1959-05-30`: 1
- `time`:
  - `\N`: 731
  - `12:00:00`: 113
  - `13:00:00`: 50
  - `14:00:00`: 34
  - `13:10:00`: 30
  - `06:00:00`: 21
  - `17:00:00`: 13
  - `19:00:00`: 13
  - `05:00:00`: 13
  - `15:00:00`: 12
- `url`:
  - `http://en.wikipedia.org/wiki/2009_Australian_Grand_Prix`: 1
  - `http://en.wikipedia.org/wiki/1960_Dutch_Grand_Prix`: 1
  - `http://en.wikipedia.org/wiki/1960_United_States_Grand_Prix`: 1
  - `http://en.wikipedia.org/wiki/1960_Italian_Grand_Prix`: 1
  - `http://en.wikipedia.org/wiki/1960_Portuguese_Grand_Prix`: 1
  - `http://en.wikipedia.org/wiki/1960_British_Grand_Prix`: 1
  - `http://en.wikipedia.org/wiki/1960_French_Grand_Prix`: 1
  - `http://en.wikipedia.org/wiki/1960_Belgian_Grand_Prix`: 1
  - `http://en.wikipedia.org/wiki/1960_Indianapolis_500`: 1
  - `http://en.wikipedia.org/wiki/1959_Indianapolis_500`: 1
- `fp1_date`:
  - `\N`: 1035
  - `2024-03-07`: 1
  - `2023-11-24`: 1
  - `2023-11-16`: 1
  - `2023-11-03`: 1
  - `2023-10-27`: 1
  - `2023-10-20`: 1
  - `2023-10-06`: 1
  - `2023-09-22`: 1
  - `2023-09-15`: 1
- `fp1_time`:
  - `\N`: 1057
  - `11:30:00`: 18
  - `12:00:00`: 8
  - `09:30:00`: 6
  - `10:30:00`: 4
  - `13:30:00`: 4
  - `17:30:00`: 4
  - `02:30:00`: 3
  - `18:30:00`: 3
  - `18:00:00`: 3
- `fp2_date`:
  - `\N`: 1035
  - `2024-03-07`: 1
  - `2023-11-24`: 1
  - `2023-11-16`: 1
  - `2023-11-04`: 1
  - `2023-10-27`: 1
  - `2023-10-21`: 1
  - `2023-10-07`: 1
  - `2023-09-22`: 1
  - `2023-09-15`: 1
- `fp2_time`:
  - `\N`: 1057
  - `15:00:00`: 22
  - `13:00:00`: 8
  - `06:00:00`: 5
  - `10:30:00`: 4
  - `14:00:00`: 4
  - `21:00:00`: 4
  - `17:00:00`: 3
  - `21:30:00`: 3
  - `22:00:00`: 3
- `fp3_date`:
  - `\N`: 1053
  - `2022-10-29`: 1
  - `2023-11-17`: 1
  - `2023-10-28`: 1
  - `2023-09-23`: 1
  - `2023-09-16`: 1
  - `2023-09-02`: 1
  - `2023-08-26`: 1
  - `2023-07-22`: 1
  - `2023-07-08`: 1
- `fp3_time`:
  - `\N`: 1072
  - `10:30:00`: 14
  - `11:00:00`: 9
  - `09:30:00`: 4
  - `02:30:00`: 3
  - `17:00:00`: 3
  - `16:30:00`: 3
  - `01:30:00`: 2
  - `17:30:00`: 2
  - `13:30:00`: 2
- [INFO] matplotlib/seaborn no disponible — matriz de correlación omitida.
### Chequeos exactos (archivo completo)
- `raceId`: 1125 únicos en 1125 filas — unicidad: True
- `circuitId`: 77 únicos en 1125 filas — unicidad: False

---

## results.csv
- Ruta: `/Users/herwin/Desktop/F1/datasets/results.csv`
- Tamaño en disco: 1,721,961 bytes
- Filas (conteo líneas): 26759
- Lectura: completa
- Columnas detectadas: 18
- Columnas (primeras 20): resultId, raceId, driverId, constructorId, number, grid, position, positionText, positionOrder, points, laps, time, milliseconds, fastestLap, rank, fastestLapTime, fastestLapSpeed, statusId
### Tipos de datos (muestra)
- `resultId`: `int64`
- `raceId`: `int64`
- `driverId`: `int64`
- `constructorId`: `int64`
- `number`: `object`
- `grid`: `int64`
- `position`: `object`
- `positionText`: `object`
- `positionOrder`: `int64`
- `points`: `float64`
- `laps`: `int64`
- `time`: `object`
- `milliseconds`: `object`
- `fastestLap`: `object`
- `rank`: `object`
- `fastestLapTime`: `object`
- `fastestLapSpeed`: `object`
- `statusId`: `int64`
### Valores faltantes
- No se detectaron nulos en la muestra.
### Estadísticas numéricas (muestra)
| columna | count | mean | std | min | 25% | 50% | 75% | max |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `resultId` | 26,759 | 13380.977 | 7726.135 | 1.000 | 6690.500 | 13380.000 | 20069.500 | 26764.000 |
| `raceId` | 26,759 | 551.687 | 313.265 | 1.000 | 300.000 | 531.000 | 811.000 | 1144.000 |
| `driverId` | 26,759 | 278.674 | 282.703 | 1.000 | 57.000 | 172.000 | 399.500 | 862.000 |
| `constructorId` | 26,759 | 50.181 | 61.551 | 1.000 | 6.000 | 25.000 | 63.000 | 215.000 |
| `grid` | 26,759 | 11.135 | 7.203 | 0.000 | 5.000 | 11.000 | 17.000 | 34.000 |
| `positionOrder` | 26,759 | 12.794 | 7.666 | 1.000 | 6.000 | 12.000 | 18.000 | 39.000 |
| `points` | 26,759 | 1.988 | 4.351 | 0.000 | 0.000 | 0.000 | 2.000 | 50.000 |
| `laps` | 26,759 | 46.302 | 29.497 | 0.000 | 23.000 | 53.000 | 66.000 | 200.000 |
| `statusId` | 26,759 | 17.225 | 26.026 | 1.000 | 1.000 | 10.000 | 14.000 | 141.000 |
- [INFO] matplotlib/seaborn no disponible — histogramas omitidos.
### Top valores en columnas categóricas (muestra)
- `number`:
  - `4`: 1019
  - `16`: 1005
  - `11`: 1001
  - `3`: 994
  - `6`: 994
  - `8`: 993
  - `14`: 982
  - `10`: 976
  - `20`: 972
  - `2`: 959
- `position`:
  - `\N`: 10953
  - `3`: 1135
  - `4`: 1135
  - `2`: 1133
  - `5`: 1131
  - `1`: 1128
  - `6`: 1124
  - `7`: 1104
  - `8`: 1076
  - `9`: 1038
- `positionText`:
  - `R`: 8897
  - `F`: 1368
  - `3`: 1135
  - `4`: 1135
  - `2`: 1133
  - `5`: 1131
  - `1`: 1128
  - `6`: 1124
  - `7`: 1104
  - `8`: 1076
- `time`:
  - `\N`: 19079
  - `+8:22.19`: 5
  - `+46.2`: 4
  - `+5.7`: 4
  - `+0.7`: 4
  - `+1:29.6`: 4
  - `+24.2`: 3
  - `+12.8`: 3
  - `+6.1`: 3
  - `+58.2`: 3
- `milliseconds`:
  - `\N`: 19079
  - `14259460`: 5
  - `10928200`: 3
  - `5350182`: 2
  - `5593660`: 2
  - `8867400`: 2
  - `4925000`: 2
  - `5808819`: 2
  - `14507710`: 2
  - `14260930`: 2
- `fastestLap`:
  - `\N`: 18507
  - `50`: 309
  - `52`: 289
  - `53`: 287
  - `51`: 275
  - `48`: 230
  - `44`: 224
  - `55`: 220
  - `49`: 219
  - `43`: 217
- `rank`:
  - `\N`: 18249
  - `2`: 410
  - `6`: 410
  - `5`: 410
  - `1`: 410
  - `3`: 410
  - `4`: 410
  - `10`: 409
  - `11`: 409
  - `7`: 409
- `fastestLapTime`:
  - `\N`: 18507
  - `1:18.904`: 4
  - `1:43.026`: 4
  - `1:14.117`: 4
  - `1:17.495`: 4
  - `1:18.262`: 4
  - `1:18.069`: 3
  - `1:18.462`: 3
  - `1:34.090`: 3
  - `1:35.816`: 3
- `fastestLapSpeed`:
  - `\N`: 18507
  - `207.069`: 4
  - `202.685`: 3
  - `188.806`: 3
  - `201.512`: 3
  - `201.330`: 3
  - `209.244`: 3
  - `206.625`: 3
  - `202.871`: 3
  - `225.876`: 3
- [INFO] matplotlib/seaborn no disponible — matriz de correlación omitida.
### Chequeos exactos (archivo completo)
- `resultId`: 26759 únicos en 26759 filas — unicidad: True
- `raceId`: 1125 únicos en 26759 filas — unicidad: False
- `driverId`: 861 únicos en 26759 filas — unicidad: False
- `constructorId`: 211 únicos en 26759 filas — unicidad: False
- `grid`: 35 únicos en 26759 filas — unicidad: False
- `statusId`: 137 únicos en 26759 filas — unicidad: False

---

## seasons.csv
- Ruta: `/Users/herwin/Desktop/F1/datasets/seasons.csv`
- Tamaño en disco: 4,594 bytes
- Filas (conteo líneas): 75
- Lectura: completa
- Columnas detectadas: 2
- Columnas (primeras 20): year, url
### Tipos de datos (muestra)
- `year`: `int64`
- `url`: `object`
### Valores faltantes
- No se detectaron nulos en la muestra.
### Estadísticas numéricas (muestra)
| columna | count | mean | std | min | 25% | 50% | 75% | max |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `year` | 75 | 1987.000 | 21.794 | 1950.000 | 1968.500 | 1987.000 | 2005.500 | 2024.000 |
- [INFO] matplotlib/seaborn no disponible — histogramas omitidos.
### Top valores en columnas categóricas (muestra)
- `url`:
  - `http://en.wikipedia.org/wiki/2009_Formula_One_season`: 1
  - `http://en.wikipedia.org/wiki/1954_Formula_One_season`: 1
  - `http://en.wikipedia.org/wiki/1956_Formula_One_season`: 1
  - `http://en.wikipedia.org/wiki/1957_Formula_One_season`: 1
  - `http://en.wikipedia.org/wiki/1958_Formula_One_season`: 1
  - `http://en.wikipedia.org/wiki/1959_Formula_One_season`: 1
  - `http://en.wikipedia.org/wiki/1960_Formula_One_season`: 1
  - `http://en.wikipedia.org/wiki/1961_Formula_One_season`: 1
  - `http://en.wikipedia.org/wiki/1962_Formula_One_season`: 1
  - `http://en.wikipedia.org/wiki/1963_Formula_One_season`: 1
### Chequeos exactos (archivo completo)
- No se detectaron columnas con patrón `id` o `_id`.

---

## sprint_results.csv
- Ruta: `/Users/herwin/Desktop/F1/datasets/sprint_results.csv`
- Tamaño en disco: 24,732 bytes
- Filas (conteo líneas): 360
- Lectura: completa
- Columnas detectadas: 16
- Columnas (primeras 20): resultId, raceId, driverId, constructorId, number, grid, position, positionText, positionOrder, points, laps, time, milliseconds, fastestLap, fastestLapTime, statusId
### Tipos de datos (muestra)
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
### Valores faltantes
- No se detectaron nulos en la muestra.
### Estadísticas numéricas (muestra)
| columna | count | mean | std | min | 25% | 50% | 75% | max |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `resultId` | 360 | 180.500 | 104.067 | 1.000 | 90.750 | 180.500 | 270.250 | 360.000 |
| `raceId` | 360 | 1106.944 | 25.636 | 1061.000 | 1084.000 | 1112.500 | 1126.000 | 1143.000 |
| `driverId` | 360 | 734.658 | 276.412 | 1.000 | 822.000 | 840.000 | 848.000 | 861.000 |
| `constructorId` | 360 | 94.367 | 89.166 | 1.000 | 6.000 | 84.000 | 210.000 | 215.000 |
| `number` | 360 | 28.178 | 23.796 | 1.000 | 11.000 | 22.000 | 44.000 | 99.000 |
| `grid` | 360 | 9.922 | 5.842 | 0.000 | 5.000 | 10.000 | 15.000 | 20.000 |
| `positionOrder` | 360 | 10.500 | 5.774 | 1.000 | 5.750 | 10.500 | 15.250 | 20.000 |
| `points` | 360 | 1.550 | 2.496 | 0.000 | 0.000 | 0.000 | 3.000 | 8.000 |
| `laps` | 360 | 19.583 | 4.753 | 0.000 | 18.000 | 19.000 | 24.000 | 24.000 |
| `statusId` | 360 | 3.336 | 13.448 | 1.000 | 1.000 | 1.000 | 1.000 | 130.000 |
- [INFO] matplotlib/seaborn no disponible — histogramas omitidos.
### Top valores en columnas categóricas (muestra)
- `position`:
  - `1`: 18
  - `9`: 18
  - `15`: 18
  - `14`: 18
  - `13`: 18
  - `12`: 18
  - `2`: 18
  - `10`: 18
  - `11`: 18
  - `8`: 18
- `positionText`:
  - `1`: 18
  - `9`: 18
  - `15`: 18
  - `14`: 18
  - `13`: 18
  - `2`: 18
  - `11`: 18
  - `10`: 18
  - `12`: 18
  - `8`: 18
- `time`:
  - `\N`: 20
  - `25:38.426`: 1
  - `+37.840`: 1
  - `+31.951`: 1
  - `+25.696`: 1
  - `+24.713`: 1
  - `+22.088`: 1
  - `+20.696`: 1
  - `+17.486`: 1
  - `+15.258`: 1
- `milliseconds`:
  - `\N`: 20
  - `1538426`: 1
  - `1962500`: 1
  - `1956611`: 1
  - `1950356`: 1
  - `1949373`: 1
  - `1946748`: 1
  - `1945356`: 1
  - `1942146`: 1
  - `1939918`: 1
- `fastestLap`:
  - `4`: 42
  - `17`: 28
  - `3`: 25
  - `8`: 24
  - `6`: 23
  - `5`: 23
  - `18`: 22
  - `19`: 21
  - `16`: 20
  - `9`: 17
- `fastestLapTime`:
  - `\N`: 9
  - `1:28.717`: 2
  - `1:30.013`: 1
  - `1:15.738`: 1
  - `1:41.107`: 1
  - `1:40.951`: 1
  - `1:40.962`: 1
  - `1:41.003`: 1
  - `1:41.065`: 1
  - `1:40.420`: 1
- [INFO] matplotlib/seaborn no disponible — matriz de correlación omitida.
### Chequeos exactos (archivo completo)
- `resultId`: 360 únicos en 360 filas — unicidad: True
- `raceId`: 18 únicos en 360 filas — unicidad: False
- `driverId`: 31 únicos en 360 filas — unicidad: False
- `constructorId`: 12 únicos en 360 filas — unicidad: False
- `grid`: 21 únicos en 360 filas — unicidad: False
- `statusId`: 8 únicos en 360 filas — unicidad: False

---

## status.csv
- Ruta: `/Users/herwin/Desktop/F1/datasets/status.csv`
- Tamaño en disco: 2,136 bytes
- Filas (conteo líneas): 139
- Lectura: completa
- Columnas detectadas: 2
- Columnas (primeras 20): statusId, status
### Tipos de datos (muestra)
- `statusId`: `int64`
- `status`: `object`
### Valores faltantes
- No se detectaron nulos en la muestra.
### Estadísticas numéricas (muestra)
| columna | count | mean | std | min | 25% | 50% | 75% | max |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `statusId` | 139 | 71.237 | 41.092 | 1.000 | 35.500 | 72.000 | 106.500 | 141.000 |
- [INFO] matplotlib/seaborn no disponible — histogramas omitidos.
### Top valores en columnas categóricas (muestra)
- `status`:
  - `Finished`: 1
  - `Excluded`: 1
  - `Not restarted`: 1
  - `Alternator`: 1
  - `Underweight`: 1
  - `Safety belt`: 1
  - `Oil pump`: 1
  - `Fuel leak`: 1
  - `Did not prequalify`: 1
  - `Spark plugs`: 1
### Chequeos exactos (archivo completo)
- `statusId`: 139 únicos en 139 filas — unicidad: True

---

## Notas generales
- El script usa muestras para archivos grandes; para análisis exactos, carga los archivos completos si tu máquina tiene memoria suficiente.
- Las figuras se guardaron en `datasets/figures/` (rutas relativas en el informe).
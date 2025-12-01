ATTACH TABLE _ UUID 'd7ddbb68-0865-4b02-9330-0e7dbd2608e5'
(
    `test` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192

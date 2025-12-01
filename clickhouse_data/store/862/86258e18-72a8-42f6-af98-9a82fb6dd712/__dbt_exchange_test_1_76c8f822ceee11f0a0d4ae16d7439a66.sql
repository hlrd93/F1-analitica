ATTACH TABLE _ UUID 'caa4e6c3-8942-4475-8c68-16146864c104'
(
    `test` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192

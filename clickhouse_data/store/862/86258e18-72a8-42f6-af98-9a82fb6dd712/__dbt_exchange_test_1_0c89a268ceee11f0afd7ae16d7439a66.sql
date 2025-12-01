ATTACH TABLE _ UUID 'de1ae880-e11e-45c3-b806-aaf1840c0713'
(
    `test` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192

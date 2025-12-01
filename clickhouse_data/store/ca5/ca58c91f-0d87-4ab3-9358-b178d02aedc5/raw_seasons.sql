ATTACH TABLE _ UUID '1bf2fa4e-5db2-450d-a52a-e28665486e30'
(
    `year` String,
    `url` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192

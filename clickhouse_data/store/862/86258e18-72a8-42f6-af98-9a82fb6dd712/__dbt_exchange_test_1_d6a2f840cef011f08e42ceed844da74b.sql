ATTACH TABLE _ UUID '995465ac-3a4f-4728-997d-04bbee230a40'
(
    `test` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192

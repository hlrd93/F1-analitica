ATTACH TABLE _ UUID '0f9b8c38-7d54-4dda-b0a4-8d49c2ba5b1f'
(
    `test` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192

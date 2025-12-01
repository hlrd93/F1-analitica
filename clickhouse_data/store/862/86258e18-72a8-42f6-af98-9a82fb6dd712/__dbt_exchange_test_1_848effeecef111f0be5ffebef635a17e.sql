ATTACH TABLE _ UUID '9e883989-10b3-42dc-928c-e32c570791d0'
(
    `test` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192

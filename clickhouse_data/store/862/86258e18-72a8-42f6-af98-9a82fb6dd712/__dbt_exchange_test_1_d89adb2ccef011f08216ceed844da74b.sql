ATTACH TABLE _ UUID 'f3923772-3426-4749-8a90-aed6862daa1a'
(
    `test` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192

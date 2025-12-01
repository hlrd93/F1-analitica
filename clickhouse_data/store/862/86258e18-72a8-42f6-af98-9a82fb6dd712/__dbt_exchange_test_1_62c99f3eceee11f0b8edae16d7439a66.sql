ATTACH TABLE _ UUID 'f69c468f-87a9-4873-ad73-8c0a65af2736'
(
    `test` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192

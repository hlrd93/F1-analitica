ATTACH TABLE _ UUID 'deade491-8e4e-46d7-bc0a-0d9f56c72cf7'
(
    `test` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192

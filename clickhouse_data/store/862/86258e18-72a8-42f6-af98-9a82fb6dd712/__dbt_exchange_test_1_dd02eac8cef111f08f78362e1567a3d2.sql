ATTACH TABLE _ UUID '60196a75-63e3-4b32-ad33-475198223931'
(
    `test` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192

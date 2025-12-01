ATTACH TABLE _ UUID '6db688f0-9e51-46ac-995a-14fd9a8d1750'
(
    `test` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192

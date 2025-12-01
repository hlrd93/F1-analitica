ATTACH TABLE _ UUID 'ef6fc167-02e7-4630-8093-f8d8ad20fc82'
(
    `test` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192

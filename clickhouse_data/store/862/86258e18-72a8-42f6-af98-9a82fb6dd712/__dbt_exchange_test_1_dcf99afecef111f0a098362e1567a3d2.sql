ATTACH TABLE _ UUID '1be77446-d51a-4cc7-972c-d6b516ad7942'
(
    `test` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192

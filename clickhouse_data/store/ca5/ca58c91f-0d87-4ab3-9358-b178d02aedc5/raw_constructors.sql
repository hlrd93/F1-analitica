ATTACH TABLE _ UUID '2004dcb9-7c3b-4e03-9aa9-c60362150b7b'
(
    `constructorId` String,
    `constructorRef` String,
    `name` String,
    `nationality` String,
    `url` String
)
ENGINE = MergeTree
ORDER BY tuple()
SETTINGS index_granularity = 8192

# Proof Of Concept for Druid realtime ingestion with Kafka firehose

## Queries
Here are some example queries for this POC. You can change files to modify queries.

### timeBoundary (manual)
```
curl -XPOST -H'Content-type: application/json' "http://localhost:8080/druid/v2/?pretty" -d'{"queryType":"timeBoundary","dataSource":"poc"}'
```

### timeBoundary (file)
```
curl -XPOST -H'Content-type: application/json' "http://localhost:8080/druid/v2/?pretty" -d@query_timeBoundary.json
```

### timeseries (file)
```
curl -XPOST -H'Content-type: application/json' "http://localhost:8080/druid/v2/?pretty" -d@query_timeseries.json
```

### groupBy (file)
```
curl -XPOST -H'Content-type: application/json' "http://localhost:8080/druid/v2/?pretty" -d@query_groupBy.json
```
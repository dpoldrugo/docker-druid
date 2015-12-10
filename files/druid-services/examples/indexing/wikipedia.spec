[
  {
    "schema": {
      "dataSource": "wikipedia",
      "aggregators" : [{
         "type" : "count",
         "name" : "count"
        }, {
         "type" : "doubleSum",
         "name" : "added",
         "fieldName" : "added"
        }, {
         "type" : "doubleSum",
         "name" : "deleted",
         "fieldName" : "deleted"
        }, {
         "type" : "doubleSum",
         "name" : "delta",
         "fieldName" : "delta"
      }],
      "indexGranularity": "none"
    },
    "config": {
      "maxRowsInMemory": 500000,
      "intermediatePersistPeriod": "PT10m"
    },
    "firehose": {
      "type": "kafka-0.8",
      "consumerProps": {
		"zookeeper.connect": "localhost:2181",
		"zookeeper.connection.timeout.ms" : "15000",
		"zookeeper.session.timeout.ms" : "15000",
		"zookeeper.sync.time.ms" : "5000",
		"group.id": "druid-example",
		"fetch.message.max.bytes" : "1048586",
		"auto.offset.reset": "largest",
		"auto.commit.enable": "false"
      },
      "feed": "wikipedia",
      "parser": {
        "timestampSpec": {
          "column": "timestamp"
        },
        "data": {
          "format": "json",
          "dimensions" : ["page","language","user","unpatrolled","newPage","robot","anonymous","namespace","continent","country","region","city"]
        }
      }
    },
    "plumber": {
      "type": "realtime",
      "windowPeriod": "PT10m",
      "segmentGranularity": "hour",
      "basePersistDirectory": "\/tmp\/realtime\/basePersist",
      "rejectionPolicy": {
        "type": "test"
      }
    }
  }
]
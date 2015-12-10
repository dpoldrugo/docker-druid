[
  {
	    "schema": {
	      "dataSource": "poc",
	      "aggregators" : [{
	         "type" : "longSum",
	         "name" : "totalCount",
	         "fieldName" : "countDelta"
	        }, {
	         "type" : "doubleSum",
	         "name" : "price",
	         "fieldName" : "priceDelta"
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
			"group.id": "poc-example",
			"fetch.message.max.bytes" : "1048586",
			"auto.offset.reset": "largest",
			"auto.commit.enable": "false"
	      },
	      "feed": "poc",
	      "parser": {
	        "timestampSpec": {
	          "column": "timestamp"
	        },
	        "data": {
	          "format": "json",
	          "dimensions" : ["campaignId"]
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
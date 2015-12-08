docker-druid
============
Docker container running Coordinator, Historical, Realtime, Broker, Overlord, MySql, Zookeeper, and Kafka.

Requirements:Docker

Build Docker image
==================
```bash
./build
```

Run Container
=============
```bash
./shell
```

Inside the container, start the entire cluster
```bash
runsvdir-start&
```

OR

Start Docker Containter Druid cluster non-interactive
=====================================================
```bash
./start-docker-druid-cluster
```

Note port 8083 forwards the Druid Rest API,

You may now follow the tutorial here http://druid.io/docs/0.6.105/Tutorial:-Loading-Your-Data-Part-1.html

#!/bin/bash

mongod --config config/config.conf &
mongod --config shard1/mongod.conf &
mongod --config repl1/mongod.conf &
mongod --config repl2/mongod.conf &
mongod --config shard2/mongod.conf &
mongod --config shard3/mongod.conf &


#!/bin/bash
mongos --config mongos/mongos.conf &
sleep 5
mongo localhost:30005 --eval 'sh.addShard("rs2/127.0.0.1:30010")'
mongo localhost:30005 --eval 'sh.addShard("rs3/127.0.0.1:30020")'

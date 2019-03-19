#!/bin/bash

mongo localhost:20000 --eval 'rs.initiate({ _id : "configRepl", members:[ {_id:0, host:"127.0.0.1:20000"} ] })'
mongo localhost:30010 --eval 'rs.initiate({ _id : "rs2", members:[ {_id:0, host:"127.0.0.1:30010"}]})'
mongo localhost:30020 --eval 'rs.initiate({ _id : "rs3", members:[ {_id:0, host:"127.0.0.1:30020"}]})'

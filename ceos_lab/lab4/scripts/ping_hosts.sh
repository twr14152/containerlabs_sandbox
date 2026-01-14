#!/bin/bash
#
docker exec h1 ping -c 4 10.0.20.11
docker exec h1 ping -c 4 10.0.20.12


docker exec h3 ping -c 4 10.0.20.10
docker exec h3 ping -c 4 10.0.20.11

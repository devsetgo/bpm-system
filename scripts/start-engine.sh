#!/bin/bash
set -e
set -x
# change directory
cd bpm-engine
# run camunda
./bpm_run/start.sh
# ./bpm_run/start.sh --production --webapps --rest
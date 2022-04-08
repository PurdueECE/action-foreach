#!/bin/bash

# ######################################################
# Author : Will Moffat
# email : moffatw@purdue.edu
# ID : ee364b13
# Date : 2/6/22
# ######################################################

ID=$1
FILENAME="maps/projects.dat"

grep $ID $FILENAME | sort | uniq | awk '{print $1}'

exit 0
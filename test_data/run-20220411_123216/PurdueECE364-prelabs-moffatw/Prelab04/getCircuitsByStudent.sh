#!/bin/bash

# ######################################################
# Author : Will Moffat
# email : moffatw@purdue.edu
# ID : ee364b13
# Date : 2/6/22
# ######################################################

STUDENT=$1
FILENAME="maps/students.dat"

ID="$(grep $STUDENT $FILENAME -s | awk '{print $4}')"
grep -H $ID circuits/*.dat | cut -b 18-24 | sort | uniq

exit 0
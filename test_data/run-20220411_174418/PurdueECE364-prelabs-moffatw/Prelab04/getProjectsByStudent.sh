#!/bin/bash

# ######################################################
# Author : Will Moffat
# email : moffatw@purdue.edu
# ID : ee364b13
# Date : 2/6/22
# ######################################################

STUDENT=$1
FILENAME="maps/students.dat"

ID=$(grep $STUDENT $FILENAME -s | awk '{print $4}')
CIRCUITS=$(grep -H $ID circuits/*.dat | cut -b 18-24 | sort | uniq)
CIRCUITS=$(sed 's/ /\\|/g' <<< $CIRCUITS)

FILENAME="maps/projects.dat"
grep $CIRCUITS $FILENAME | sort -k 2 | uniq | awk '{print $2}'

exit 0
#!/bin/bash

# ######################################################
# Author : Will Moffat
# email : moffatw@purdue.edu
# ID : ee364b13
# Date : 2/6/22
# ######################################################

COMP=$1

grep -H $COMP circuits/*.dat | wc -l

exit 0
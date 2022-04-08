#!/bin/bash

# ######################################################
# Author : Will Moffat
# email : moffatw@purdue.edu
# ID : ee364b13
# Date : 2/6/22
# ######################################################

COUNT1=$(grep -H $1 circuits/*.dat | wc -l)
COUNT2=$(grep -H $2 circuits/*.dat | wc -l)

if (($COUNT1 > $COUNT2))
then
    echo $1
else
    echo $2
fi

exit 0
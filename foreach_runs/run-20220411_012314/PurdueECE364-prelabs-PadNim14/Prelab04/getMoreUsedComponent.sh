#! /bin/bash

# ######################################################
# Author : < Nimal Padmanabhan >
# email : < npadmana@purdue.edu >
# ID : < ee364b17 >
# Date : < 2/2/2022 >
# ######################################################
# Write your sequence of statements here
circuit_id1=$1
circuit_id2=$2
circuit1=$(grep "$circuit_id1" "circuits/"* | wc -l)
circuit2=$(grep "$circuit_id2" "circuits/"* | wc -l)
if (($circuit1 > $circuit2))
then
    echo $circuit_id1
else
    echo $circuit_id2
fi
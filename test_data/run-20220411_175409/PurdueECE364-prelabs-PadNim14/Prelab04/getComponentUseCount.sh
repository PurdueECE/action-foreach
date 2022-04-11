#! /bin/bash
# ######################################################
# Author : < Nimal Padmanabhan >
# email : < npadmana@purdue.edu >
# ID : < ee364b17 >
# Date : < 2/2/2022 >
# ######################################################
# Write your sequence of statements here
circuit_id=$1
result=$(grep "$circuit_id" "circuits/"* | wc -l)
echo $result

#! /bin/bash

# ######################################################
# Author : < Nimal Padmanabhan >
# email : < npadmana@purdue.edu >
# ID : < ee364b17 >
# Date : < 2/2/2022 >
# ######################################################
# Write your sequence of statements here
project_id=$1
fname="maps/projects.dat"
result=$(grep -i "$project_id" "$fname"|sort|uniq|cut -c 1-11)
echo "$result"

exit 0
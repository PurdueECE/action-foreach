# ######################################################
# Author : Eshaan Minocha
# email : eminocha@purdue.edu
# ID : ee364b01
# Date : 2/5/2022
# ######################################################
# Write your sequence of statements here .

#!/bin/bash/sh

# Problem 1

file="maps/projects.dat"
declare -a store

((i=0))
given_proj_id="$1" # Getting the command line argument

while read circ_id proj_id; do
    if [[ "$given_proj_id" = "$proj_id" ]]; then 
        store+=([${i}]="$circ_id")
        ((i=i+1))
    fi
done < $file

# Sorting and Removing duplicates
sorted_unique_ids=($(echo "${store[@]}" | tr ' ' '\n' | sort -u | tr '\n' ' '))

# Printing the array 
for j in ${sorted_unique_ids[@]}; do
    echo $j;
done 

exit 0

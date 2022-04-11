#! /bin/bash
# ######################################################
# Author : < Nimal Padmanabhan >
# email : < npadmana@purdue.edu >
# ID : < ee364b17 >
# Date : < 2/2/2022 >
# ######################################################
# Write your sequence of statements here

student_name=$1
fname="maps/students.dat"
result=$(grep -i "$student_name" "$fname" )
# echo $result
b=$(echo $result | cut -c 18-28)


# result2 = $(echo $result | cut -c 1-6)
for circuit in "circuits"/*
do
    if (grep -q "$b" "$circuit"); then 
        c=$(echo $circuit | cut -c 18-24)
        grep -w "$c" "maps/projects.dat"|cut -c 15-60 
    fi
done | sort | uniq

exit 0
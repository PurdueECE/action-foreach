#! /bin/bash

# ######################################################
# Author : Adrian Chen
# email : chen3124@purdue.edu
# ID : ee364b10
# Date : 2/2/2022
# ######################################################

projects=$(grep -r -l $(grep "$1" "maps/students.dat" | sort | cut -c45-55) "circuits" | sort | cut -c18-24)
for p in $projects
do
    output+=$(grep $p "maps/projects.dat" | cut -c21-57)
done

for o in $output
do
    echo $o
done | sort | uniq
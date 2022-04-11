#!/bin/bash

#######################################################
# Author : Lingyue Christine Fang
# email : fang245@purdue.edu
# ID : ee364b09
# Date : January 31, 2022
# ######################################################
{
    read
    read
    while read first last blank id; do
        name="$first $last"
        if [[ $name == $1 ]]; then
            student=$id
        fi
        
    done
}< "maps/students.dat"
grep $student circuits/*.dat | awk -F'[_.]' '{print $2}'

exit 0

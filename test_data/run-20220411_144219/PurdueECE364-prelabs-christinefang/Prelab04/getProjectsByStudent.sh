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
tmp=$(grep $student circuits/*.dat | awk -F'[_.]' '{print $2}')
{
    read
    read
    while read stu p; do
        for proj in $tmp
        do
            if [[ $proj == $stu ]]; then
                echo $p >> sortproj.txt
            fi

        done
    done
}< "maps/projects.dat"
uniq sortproj.txt >> othersortproj.txt
sort othersortproj.txt
rm sortproj.txt
rm othersortproj.txt
exit 0


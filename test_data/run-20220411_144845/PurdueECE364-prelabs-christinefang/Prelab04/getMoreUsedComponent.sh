#!/bin/bash

#######################################################
# Author : Lingyue Christine Fang
# email : fang245@purdue.edu
# ID : ee364b09
# Date : January 31, 2022
# ######################################################

num1=$(grep -l "$1" circuits/*.dat | wc -l)
num2=$(grep -l "$2" circuits/*.dat | wc -l)

if (( $num1 > $num2 )); then
    echo $1
elif (( $num1 < $num2 )); then
    echo $2
fi

exit 0


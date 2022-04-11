#!/bin/bash
# ######################################################
# Author : Insherah Neizer-Ashun
# email : ineizera@purdue.edu
# ID : ee364a02
# Date : 01/31/2022
# ######################################################
# Write your sequence of statements here .
if [[ $(grep $1 -lr circuits/* | wc -l) -gt $(grep $2 -lr circuits/* | wc -l) ]]
then
    echo $1;
else
    echo $2;
fi
exit 0
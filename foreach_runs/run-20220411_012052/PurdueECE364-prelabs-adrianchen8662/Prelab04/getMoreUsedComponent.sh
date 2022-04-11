#! /bin/bash

# ######################################################
# Author : Adrian Chen
# email : chen3124@purdue.edu
# ID : ee364b10
# Date : 2/2/2022
# ######################################################

if [ $(grep -r -l $1 "circuits" | wc -l) -gt $(grep -r -l $2 "circuits" | wc -l) ]
then
    echo $1
else
    echo $2
fi
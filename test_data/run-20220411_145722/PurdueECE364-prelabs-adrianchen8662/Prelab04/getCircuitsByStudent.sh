#! /bin/bash

# ######################################################
# Author : Adrian Chen
# email : chen3124@purdue.edu
# ID : ee364b10
# Date : 2/2/2022
# ######################################################

grep -r -l $(grep "$1" "maps/students.dat" | sort | cut -c45-55) "circuits" | sort | cut -c18-24
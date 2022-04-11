#! /bin/bash

# ######################################################
# Author : Adrian Chen
# email : chen3124@purdue.edu
# ID : ee364b10
# Date : 2/2/2022
# ######################################################

grep "$1" "maps/projects.dat" | sort | cut -c1-11
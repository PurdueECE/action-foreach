#!/bin/bash
# ######################################################
# Author : Insherah Neizer-Ashun
# email : ineizera@purdue.edu
# ID : ee364a02
# Date : 01/31/2022
# ######################################################
# Write your sequence of statements here .

grep "$1" -lr maps/projects.dat | sort -u

exit 0
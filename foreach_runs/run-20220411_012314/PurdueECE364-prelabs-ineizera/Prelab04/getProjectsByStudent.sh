#!/bin/bash
# ######################################################
# Author : Insherah Neizer-Ashun
# email : ineizera@purdue.edu
# ID : ee364a02
# Date : 01/31/2022
# ######################################################
# Write your sequence of statements here .

# student name > id > circuits > projects

SID=$(grep "$1" maps/students.dat | cut -d '|' -f2 | cut -c 16-26)
CID=$(grep "$SID" circuits/* | cut -c 18-24 | sort -u)
grep "$CID" maps/projects.dat | cut -c 21-57 | sort -u

exit 0
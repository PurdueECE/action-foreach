#!/bin/bash

#######################################################
# Author : Lingyue Christine Fang
# email : fang245@purdue.edu
# ID : ee364b09
# Date : January 31, 2022
# ######################################################

grep -l "$1" circuits/*.dat | wc -l
exit 0

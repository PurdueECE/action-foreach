# ######################################################
# Author : Sidd Mitra
# email : mitra30@purdue.edu
# ID: eeb06
# Date : Feb 6, 2022
# ######################################################
projID=$1

grep $1 maps/projects.dat | sort | grep -oP "\d\d-\d-\d\d" | sort -u
exit 0
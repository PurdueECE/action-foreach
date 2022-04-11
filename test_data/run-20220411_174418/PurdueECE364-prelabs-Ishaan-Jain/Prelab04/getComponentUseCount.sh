# ######################################################
# Author :  Ishaan Jain
# email : jain343@purdue.edu
# ID : ece39595
# Date : 02/06/22
# ######################################################
# Write your sequence of statements here .
cir_id=$1
res=$(grep "$cir_id" "circuits/"* | wc -l)
echo "$res"
# ######################################################
# Author :  Ishaan Jain
# email : jain343@purdue.edu
# ID : ece39595
# Date : 02/06/22
# ######################################################
# Write your sequence of statements here .
cir_id=$1
cir_id1=$2
res=$(grep "$cir_id" "circuits/"* | wc -l)
res1=$(grep "$cir_id1" "circuits/"* | wc -l)
if(($res1 > $res))
then
    echo "$cir_id1"
else
    echo "$cir_id"
fi
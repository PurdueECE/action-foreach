# ######################################################
# Author : Eshaan Minocha
# email : eminocha@purdue.edu
# ID : ee364b01
# Date : 2/5/2022
# ######################################################
# Write your sequence of statements here .

#!/bin/bash/sh

# Problem 5

comp1_id=$1
comp2_id=$2
counta=0
countb=0
space1="  "
space2="  "
space1+="$comp1_id"
space2+="$comp2_id"

for filename in circuits/*.dat;do
    if grep -Fxq "$space1" $filename; then 
        ((counta++))
    fi
done

for filename in circuits/*.dat;do
    if grep -Fxq "$space2" $filename; then 
        ((countb++))
    fi
done


if [ $counta -gt $countb ]; then
    echo "$comp1_id"
else
    echo "$comp2_id"

fi

exit 0

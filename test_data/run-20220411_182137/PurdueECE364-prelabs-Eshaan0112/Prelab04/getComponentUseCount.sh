# ######################################################
# Author : Eshaan Minocha
# email : eminocha@purdue.edu
# ID : ee364b01
# Date : 2/5/2022
# ######################################################
# Write your sequence of statements here .

#!/bin/bash/sh

# Problem 4
component_id=$1
space="  "
space+="$component_id"
((count=0))
for filename in circuits/*.dat;do
    if grep -Fxq "$space" $filename; then 
        ((count++))
    fi
done
echo $count

exit 0
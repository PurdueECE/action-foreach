#! /bin/bash

# ######################################################
# Author : Xingjian Wang
# email :  wang5066@purdue.edu
# ID:      ee364b03
# Date :   Feb 6, 2022
# ######################################################

count1=$(./getComponentUseCount.sh "$1")
count2=$(./getComponentUseCount.sh "$2")

if  (( $count1 > $count2 )) 
then
    echo $1
elif (( $count1 < $count2 ))
then
    echo $2
else    # two components used equally
    echo "They are used equally."
fi

exit 0
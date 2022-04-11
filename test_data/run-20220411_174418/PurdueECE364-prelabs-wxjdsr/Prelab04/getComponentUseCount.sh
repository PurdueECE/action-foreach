#! /bin/bash

# ######################################################
# Author : Xingjian Wang
# email :  wang5066@purdue.edu
# ID:      ee364b03
# Date :   Feb 6, 2022
# ######################################################
cd ./circuits

componentID=$1
fileList=$(ls)
count=0

for file in $fileList
do
    if grep -q $componentID $file
    then
        ((count=count+1))
    fi
done

echo $count

exit 0

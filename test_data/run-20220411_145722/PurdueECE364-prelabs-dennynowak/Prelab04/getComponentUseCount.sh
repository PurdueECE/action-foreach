#! usr/bin/bash

#############################################
#   Author:     Denny Nowak
#   email:      nowak32@purdue.edu
#   ID:         ee364b14
#   Date:       02/05/2022
#############################################

# Take in component name and print out num of circuits
# Search through circuit files for component
totalCount=0
for file in circuits/*.dat
do
    if grep -wq $1 $file;
    then
        totalCount=$((totalCount+1))
    fi
done

echo $totalCount
exit 0
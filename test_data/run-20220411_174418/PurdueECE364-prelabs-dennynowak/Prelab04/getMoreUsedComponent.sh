#! usr/bin/bash

#############################################
#   Author:     Denny Nowak
#   email:      nowak32@purdue.edu
#   ID:         ee364b14
#   Date:       02/05/2022
#############################################

# Take in component names and print out which occurs more often
# Search through circuit files for components
totalCountFirst=0
totalCountSecond=0
for file in circuits/*.dat
do
    if grep -wq $1 $file;
    then
        totalCountFirst=$((totalCountFirst+1))
    fi
    if grep -wq $2 $file;
    then    
        totalCountSecond=$((totalCountSecond+1))
    fi
done

# Compare counts
if (( $totalCountFirst > $totalCountSecond ))
then
    echo $1
elif (( $totalCountFirst < $totalCountSecond ))
then 
    echo $2
else
    echo "Equal amount used"
fi

exit 0
#! /bin/bash

# ######################################################
# Author : Xingjian Wang
# email :  wang5066@purdue.edu
# ID:      ee364b03
# Date :   Feb 6, 2022
# ######################################################
PROJECT_DATABASE=./maps/projects.dat

TEMP_FILE_PATH=./temp.txt
TEMP_FILE_2_PATH=./temp2.txt

studentName=$1

circuitsID=$(./getCircuitsByStudent.sh "$studentName")

# This segment finds projectsID given circuitsID
for circuitID in $circuitsID
do  
    result+="$(grep -r $circuitID $PROJECT_DATABASE)\n"
    result=${result//$circuitID/}
    
done

# This segment sorts the projectID and removes duplicates
printf "$result" > "$TEMP_FILE_PATH"
awk '!seen[$0]++' $TEMP_FILE_PATH > $TEMP_FILE_2_PATH
sort $TEMP_FILE_2_PATH > $TEMP_FILE_PATH
result=$(<$TEMP_FILE_PATH)
rm $TEMP_FILE_PATH
rm $TEMP_FILE_2_PATH

# This segment prints the result
for line in $result
do
    echo $line
done

exit 0

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


projectID=$1

result="$(grep -r $projectID $PROJECT_DATABASE)"

result=${result//$projectID/}
echo "$result" > "$TEMP_FILE_PATH"
sort $TEMP_FILE_PATH | uniq > $TEMP_FILE_2_PATH
result=$(<$TEMP_FILE_2_PATH)
rm $TEMP_FILE_PATH
rm $TEMP_FILE_2_PATH

for line in $result
do
    if [[ $line =~ [0-99][-][0-9][-][0-99] ]]
    then
        echo $line
    fi
done

exit 0

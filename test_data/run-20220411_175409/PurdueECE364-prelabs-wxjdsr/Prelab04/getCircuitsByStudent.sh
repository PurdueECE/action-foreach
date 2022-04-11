#! /bin/bash

# ######################################################
# Author : Xingjian Wang
# email :  wang5066@purdue.edu
# ID:      ee364b03
# Date :   Feb 6, 2022
# ######################################################
STUDENT_DATABASE=./maps/students.dat

TEMP_FILE_PATH=./temp.txt
TEMP_FILE_2_PATH=./temp2.txt


# This segment finds the studentID with no extra character
studentName=$1

studentID="$(grep -r "$studentName" $STUDENT_DATABASE)"

studentID=${studentID//$studentName/}
studentID=${studentID//"| "}

# This segment finds the circuitsID giving a studentID
cd ./circuits

fileList=$(ls)

for file in $fileList
do
    if grep -q $studentID $file
    then
        # get "_" position
        underscore="${file%%"_"*}"
        underscore_index=${#underscore}
        
        # get "." position
        dot="${file%%"."*}"
        dot_index=${#dot}

        # start after "_" and ends before "."
        echo "${file:$underscore_index+1:$dot_index-$underscore_index-1}" >> "$TEMP_FILE_PATH"
    fi
done

# this part sorts the output using two temporary files
sort $TEMP_FILE_PATH | uniq > $TEMP_FILE_2_PATH
result=$(<$TEMP_FILE_2_PATH)
rm $TEMP_FILE_PATH
rm $TEMP_FILE_2_PATH

# output the result
for line in $result
do
    echo $line
done

exit 0

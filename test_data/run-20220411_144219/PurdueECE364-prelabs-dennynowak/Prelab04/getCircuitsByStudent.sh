#! usr/bin/bash

#############################################
#   Author:     Denny Nowak
#   email:      nowak32@purdue.edu
#   ID:         ee364b14
#   Date:       02/05/2022
#############################################

# Take in student name and print sorted list of Circuit IDs of student, no duplicates
touch tempFile
while IFS="|" read student id;
do
# Extract id from student
if [[ "${1// /}" = "${student// /}" ]];
then
    # Search through circuit files for student iD
    for file in circuits/*.dat
    do
        if grep -wq $id $file;
        then
            echo $file | cut -c18-24 >> tempFile
        fi
    done
fi
done < maps/students.dat

# sort and remove duplicates
sort -u tempFile 
rm tempFile
exit 0
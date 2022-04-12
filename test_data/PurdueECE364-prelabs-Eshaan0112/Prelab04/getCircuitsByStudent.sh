# ######################################################
# Author : Eshaan Minocha
# email : eminocha@purdue.edu
# ID : ee364b01
# Date : 2/5/2022
# ######################################################
# Write your sequence of statements here .

#!/bin/bash/sh

# Problem 2

file2="maps/students.dat"


((i=0))
#given_name="$1" # Getting the command line argument
IFS=" " read -r -a name_arr <<< "$1"
fname=${name_arr[0]}
lname=${name_arr[1]}

# Getting student ID
while read first last bar id; do
    if [[ "$fname" = "$first" ]] && [[ "$lname" = "$last" ]]; then 
        stu_id=$id
        break
    fi 
done < $file2

declare -a store
((i=0))

# In circuits directory
for filename in circuits/*.dat;do
    if grep -Fxq "$stu_id" $filename; then 
       name="${filename%%.*}"
       circ_id=${name#*'_'}
       store+=([${i}]="$circ_id")
       ((i=i+1))
    fi
done

# Sorting and Removing duplicates
sorted_unique_ids=($(echo "${store[@]}" | tr ' ' '\n' | sort -u | tr '\n' ' '))

# Printing the array 
for j in ${sorted_unique_ids[@]}; do
    echo $j;
done 
exit 0



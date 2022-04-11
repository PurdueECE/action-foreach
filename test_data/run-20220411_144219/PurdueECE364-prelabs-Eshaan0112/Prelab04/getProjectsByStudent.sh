# ######################################################
# Author : Eshaan Minocha
# email : eminocha@purdue.edu
# ID : ee364b01
# Date : 2/5/2022
# ######################################################
# Write your sequence of statements here .

#!/bin/bash/sh

# Problem 3

# Getting the list of circuit ids
file="maps/students.dat"

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
done < $file

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

file2="maps/projects.dat"

declare -a store_proj_ids
((skip=2))
((count=0))
while read -r circ_id2 proj_id; do
    if [ $count -ge $skip ];then
        if (printf '%s\n' ${store[@]} | grep -Fxq $circ_id2); then
            store_proj_ids+=([${count}]="$proj_id")
        fi
    fi
    ((count=count+1))
done < $file2

# Sorting and Removing duplicates
sorted_unique_proj_ids=($(echo "${store_proj_ids[@]}" | tr ' ' '\n' | sort -u | tr '\n' ' '))

# Printing the array 
for j in ${sorted_unique_proj_ids[@]}; do
    echo $j;
done 

exit 0
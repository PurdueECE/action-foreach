#######################################################
# Author: <Deyuan Sun >
# email: <sun829@purdue.edu >
# ID: <ee364a04 >
# Date: <2/5/2022 >
#######################################################
# Write your sequence of statements here.

input="./maps/projects.dat"

# get every data out
while IFS= read -r line
do
    if [[ "$line" == *"$1"* ]]; then
        # echo "here"
        # echo "${line:4:7}"
        unsortedArray+=("${line:4:7}")
    fi
done < "$input"

# do a bit of initial sort, -u for remove duplicates
IFS=$'\n' sorted=($(sort -u<<<"${unsortedArray[*]}"))
unset IFS

# echo each of them out
i=0
len=${#sorted[@]}
while [ $i -lt $len ];
do
    echo ${sorted[$i]}
    let i++
done


exit 0
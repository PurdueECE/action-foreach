# ######################################################
# Author : Sidd Mitra
# email : mitra30@purdue.edu
# ID: eeb06
# Date : Feb 6, 2022
# ######################################################
studentName=$1
studentID=`grep -w --color "$1" ./maps/students.dat | grep -oP "\d\d\d\d\d-\d\d\d\d\d"`
pattern="[0-9][0-9]-[0-9]-[0-9][0-9]"

projIDs=()
for filename in ./circuits/*
do
    [[ $filename =~ $pattern ]]
    circuitID=${BASH_REMATCH[0]}
    if cat $filename | grep -q $studentID
    then
        # echo $circuitID
        # cat ./maps/projects.dat | grep $circuitID | grep -oP "\w*-\w*-\w*-\w*-\w*+"
        # echo
        # cat ./maps/projects.dat | grep $circuitID | grep -coP "\w*-\w*-\w*-\w*-\w*+"
        projIDs+=( `cat ./maps/projects.dat | grep $circuitID | grep -oP "\w*-\w*-\w*-\w*-\w*+"` )
    fi

done

echo "${projIDs[@]}" | tr ' ' '\n' | sort -u | tr ' ' '\n'
# echo ${#projIDs[@]}
# sort -u ${projIDs[@]} | echo | tr ' ' '\n'
# echo;echo
# data=( "haha" "yes" "sidd" )
# for id in $data
# do
#     echo $id
# done
# ######################################################
# Author : Sidd Mitra
# email : mitra30@purdue.edu
# ID: eeb06
# Date : Feb 6, 2022
# ######################################################
studentName=$1
# echo "$studentName";echo

studentID=`grep -w --color "$1" ./maps/students.dat | grep -oP "\d\d\d\d\d-\d\d\d\d\d"`
# echo $studentID;echo

pattern="[0-9][0-9]-[0-9]-[0-9][0-9]"
for filename in ./circuits/*
do
    # grep -o ".dat" $FILE

    # find circuit ID
    [[ $filename =~ $pattern ]]
    circuitID=${BASH_REMATCH[0]}
    # echo $circuitID

    # find if student involved in circuit
    if cat $filename | grep -q $studentID
    then
        echo $circuitID
    fi

done

exit 0
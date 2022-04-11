# ######################################################
# Author : Sidd Mitra
# email : mitra30@purdue.edu
# ID: eeb06
# Date : Feb 6, 2022
# ######################################################
component1=$1
component2=$2
let sum1=0; let sum2=0
for circuit in ./circuits/*
do
    if cat $circuit | grep -q $component1
    then
        ((sum1+=1))
    elif cat $circuit | grep -q $component2
    then
        ((sum2+=1))
    fi
done

if (( $sum1 >= $sum2 ))
then
    echo $component1
else
    echo $component2
fi

exit 0
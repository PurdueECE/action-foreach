# ######################################################
# Author : Sidd Mitra
# email : mitra30@purdue.edu
# ID: eeb06
# Date : Feb 6, 2022
# ######################################################
componentID=$1
let num=0
for circuit in ./circuits/*
do
    if cat $circuit | grep -q $componentID
    then
        ((num+=1))
    fi
done

echo $num

exit 0
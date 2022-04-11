# ######################################################
# Author : Berkay Belli
# email : bbelli@purdue.edu
# ID : ee364b16
# Date : 05/02/22
# ######################################################

egrep -r "$1" circuits/ > compCount1 
ct1=$(wc -l < compCount1)

egrep -r "$2" circuits/ > compCount2 
ct2=$(wc -l < compCount2)

if [ "$ct1" -gt "$ct2" ]; 
    then 
    echo $1; 
    else 
    echo $2; 
fi

rm compCount1
rm compCount2

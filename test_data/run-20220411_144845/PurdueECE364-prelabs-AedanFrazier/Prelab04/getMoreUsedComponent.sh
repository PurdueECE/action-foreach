#######################################################
# Author : Aedan Frazier
# email : Frazie35@purdue.edu
# ID : ee364a06
# Date : 2/6/2022
#######################################################
COMPONENTS=$#

greatestcomp=""
greatestvalue=-1

for COMPONENTS; do
    eval "egrep -lr $COMPONENTS $CIRCUITSLIST" >> circuits.txt
    count=0
    while IFS= read -r line; do
        count=`expr $count + 1`
    done < circuits.txt
    rm circuits.txt

    if [ $count -gt $greatestvalue ]; then
        greatestcomp=$COMPONENTS
        greatestvalue=$count
    elif [ $count -gt $greatestvalue ]; then
        greatestcomp=$COMPONENTS
        greatestvalue=$count
    fi
done

echo $greatestcomp






exit 0
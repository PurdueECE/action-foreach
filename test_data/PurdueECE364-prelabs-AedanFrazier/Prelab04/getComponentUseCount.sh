#######################################################
# Author : Aedan Frazier
# email : Frazie35@purdue.edu
# ID : ee364a06
# Date : 2/3/2022
#######################################################
COMPONENT=$1
eval "egrep -lr $COMPONENT $CIRCUITSLIST" >> circuits.txt
count=0
while IFS= read -r line; do
    count=`expr $count + 1`
done < circuits.txt

echo $count

rm circuits.txt

exit 0
#######################################################
# Author : Aedan Frazier
# email : Frazie35@purdue.edu
# ID : ee364a06
# Date : 2/3/2022
#######################################################
STUDENT=$1
STUDENT="\"${STUDENT}\""
STUDENTLIST=maps/students.dat
CIRCUITSLIST=circuits/
I=0

#eval egrep $STUDENT $STUDENTLIST

for LINE in $(eval "egrep $STUDENT $STUDENTLIST");do
        I="$(($I + 1))"
        if [ "$I" == "4" ];then
            ID=$LINE
        fi   
done

CIRCUITS=$(eval "egrep -lr $ID $CIRCUITSLIST")


for c in $CIRCUITS;do
    echo ${c:17:7}
done

exit 0
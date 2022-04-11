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


for LINE in $(eval "egrep $STUDENT $STUDENTLIST");do
        I="$(($I + 1))"
        if [ "$I" == "4" ];then
            ID=$LINE
        fi   
done

CIRCUITS=$(eval "egrep -lr $ID $CIRCUITSLIST")


for c in $CIRCUITS;
do
    circuit=${c:17:7}
    projs=$(eval "egrep $circuit maps/projects.dat")
    echo "$projs" >> "circinproj.txt"
done

for c in $CIRCUITS;
do
    circuit=${c:17:7}
    projs=$(eval "egrep $circuit maps/projects.dat")
    echo "$projs" >> "circinproj.txt"
done

while IFS= read -r line; do
    #echo "$line"
    projs=${line:21:46}
    echo "$projs" >> "selectprojs.txt"
done < circinproj.txt

sort selectprojs.txt >> sortedprojs.txt

touch filteredprojs.txt

while IFS= read -r line; do
    if egrep -q $line "filteredprojs.txt"; then
        :
    else
        echo "$line" >> "filteredprojs.txt"
    fi
done < sortedprojs.txt

while IFS= read -r line; do
    echo "$line"
    
done < filteredprojs.txt

rm circinproj.txt
rm selectprojs.txt
rm sortedprojs.txt
rm filteredprojs.txt
exit 0
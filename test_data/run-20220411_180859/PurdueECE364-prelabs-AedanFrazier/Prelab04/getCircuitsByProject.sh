#######################################################
# Author : Aedan Frazier
# email : Frazie35@purdue.edu
# ID : ee364a06
# Date : 2/3/2022
#######################################################
ID="$1"
FILE=maps/projects.dat
I=0
for LINE in $(eval "egrep $ID $FILE");do
    if [ "$LINE" != "$ID" ];then
        LINES[I]=$LINE
        I=$I+1
    fi
done
STRNG=""
for LINE in ${LINES[@]};do
    echo "$LINE" >> SORTED.txt
done
SORTED=$(eval "sort SORTED.txt")
for LINE in $SORTED;do
    echo "$LINE"
done
rm -r SORTED.txt
exit 0
#######################################################
# Author:   William Jorge
# email:    wjorgebe@purdue.edu
# ID:       ee364b12
# Date:     February 6, 2022
#######################################################

for d in circuits/*;
do
    var1=$(fgrep $1 $d)
    var2=$(fgrep $2 $d)
    if [[ -n $var1 ]]
    then
        temp=${d#*_}
        numb=${temp%.*}
        echo $numb >> tempout1.txt
    fi
    if [[ -n $var2 ]]
    then
        temp=${d#*_}
        numb=${temp%.*}
        echo $numb >> tempout2.txt
    fi 
done

count1=$(wc -l < tempout1.txt | xargs)
count2=$(wc -l < tempout2.txt | xargs)

if [[ $count1 > $count2 ]]
then
    echo $1
else
    echo $2
fi
rm *.txt

exit 0
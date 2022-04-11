#######################################################
# Author:   William Jorge
# email:    wjorgebe@purdue.edu
# ID:       ee364b12
# Date:     February 6, 2022
#######################################################

for d in circuits/*;
do
    var1=$(fgrep $1 $d)
    if [[ -n $var1 ]]
    then
        temp=${d#*_}
        numb=${temp%.*}
        echo $numb >> tempout1.txt
    fi
done
wc -l < tempout1.txt | xargs
rm *.txt

exit 0
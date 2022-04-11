#######################################################
# Author:   William Jorge
# email:    wjorgebe@purdue.edu
# ID:       ee364b12
# Date:     February 6, 2022
#######################################################

var=$(fgrep "$1" maps/students.dat | tail -c 12)
for d in circuits/*;
do
    var2=$(fgrep $var $d)
    if [[ -n $var2 ]]
    then
        temp=${d#*_}
        numb=${temp%.*}
        echo $numb >> tempout1.txt
    fi
done
sort tempout1.txt | uniq -u > tempout2.txt
cat tempout2.txt
rm *.txt

exit 0
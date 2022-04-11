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
        tmp=${d#*_}
        num=${tmp%.*}
        echo $num >> tempout1.txt
    fi
done

sort tempout1.txt | uniq -u > tempout2.txt

while read line
do
    fgrep $line maps/projects.dat >> tempout3.txt
done < tempout2.txt

cut -c22- tempout3.txt > tempout4.txt
sort tempout4.txt | uniq -u
rm *.txt

exit 0
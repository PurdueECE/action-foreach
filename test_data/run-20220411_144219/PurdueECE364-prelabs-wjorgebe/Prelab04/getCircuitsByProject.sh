#######################################################
# Author:   William Jorge
# email:    wjorgebe@purdue.edu
# ID:       ee364b12
# Date:     February 6, 2022
#######################################################

fgrep $1 maps/projects.dat | sort | uniq -u > tempout1.txt
while read line
do
    echo ${line:0:7}
done < tempout1.txt
rm tempout1.txt

exit 0
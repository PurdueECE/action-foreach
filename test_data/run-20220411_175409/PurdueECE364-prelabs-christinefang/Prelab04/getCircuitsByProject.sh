 #!/bin/bash

#######################################################
# Author : Lingyue Christine Fang
# email : fang245@purdue.edu
# ID : ee364b09
# Date : January 31, 2022
# ######################################################
{
    read
    read
    while read circuit project; do
        if [[ $project == $1 ]]; then
            echo $circuit >> circuit.txt
        fi
    done
}<"maps/projects.dat"
uniq -i circuit.txt >> othercircuit.txt
sort othercircuit.txt

rm circuit.txt
rm othercircuit.txt
exit 0

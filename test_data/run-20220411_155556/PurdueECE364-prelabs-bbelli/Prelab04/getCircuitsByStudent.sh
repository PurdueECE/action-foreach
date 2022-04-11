# ######################################################
# Author : Berkay Belli
# email : bbelli@purdue.edu
# ID : ee364b16
# Date : 05/02/22
# ######################################################


egrep "$1" maps/students.dat > studentID
id=$(tail -c 12 studentID)

egrep -r "$id" circuits/ > circuitList 
sort circuitList > sortedList
cut -c 18-24 sortedList 

rm circuitList
rm sortedList
rm studentID
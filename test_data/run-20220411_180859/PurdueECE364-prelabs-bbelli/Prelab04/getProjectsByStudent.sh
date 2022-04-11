# ######################################################
# Author : Berkay Belli
# email : bbelli@purdue.edu
# ID : ee364b16
# Date : 05/02/22
# ######################################################

egrep "$1" maps/students.dat > studentID
id=$(tail -c 12 studentID)

egrep -r "$id" circuits/ > circuitList 
cut -c 18-24 circuitList > cutList 
rm circuitList

cat cutList | egrep -f - maps/projects.dat > projectList
rm cutList
cut -c 21-90 projectList > cutList
sort cutList

rm projectList
rm cutList
rm studentID






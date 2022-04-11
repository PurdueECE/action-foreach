# ######################################################
# Author :  Ishaan Jain
# email : jain343@purdue.edu
# ID : ece39595
# Date : 02/06/22
# ######################################################
# Write your sequence of statements here .
proj_id=$1
res=$(grep "$proj_id" "maps/projects.dat"|sort|uniq|cut -c 1-11)
echo "$res"

exit 0
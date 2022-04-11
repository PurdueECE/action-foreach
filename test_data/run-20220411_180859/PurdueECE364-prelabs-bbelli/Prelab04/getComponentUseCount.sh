# ######################################################
# Author : Berkay Belli
# email : bbelli@purdue.edu
# ID : ee364b16
# Date : 05/02/22
# ######################################################


egrep -r "$1" circuits/ > componentListCount 
wc -l < componentListCount

rm componentListCount
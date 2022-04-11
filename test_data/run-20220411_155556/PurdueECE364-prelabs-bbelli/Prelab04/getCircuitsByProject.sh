# ######################################################
# Author : Berkay Belli
# email : bbelli@purdue.edu
# ID : ee364b16
# Date : 05/02/22
# ######################################################

egrep $1 maps/projects.dat | cut -c-11 > circutsByPID
sort circutsByPID

rm circutsByPID
# ######################################################
# Author :  Ishaan Jain
# email : jain343@purdue.edu
# ID : ece39595
# Date : 02/06/22
# ######################################################
# Write your sequence of statements here .
stu_id=$1
res=$(grep -i "$stu_id" "maps/students.dat")
r=$(echo $res|cut -c 18-28) 

for cir in "circuits"/*
do
    if(grep -q "$r" "$cir"); then
        v=$(echo $cir | cut -c 18-24)
        echo $v
    fi
done | sort |uniq   

exit 0
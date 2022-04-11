 ######################################################
# Author : Erin Park
# email : Park1131@purdue.edu
# ID : ee364a05
# Date : Feb 6, 2022
# ######################################################
# Write your sequence of statements here .

count=0
count2=0
input="maps/students.dat"
while IFS= read -r line
do
  #
  #if line contains $1, we strip it >:3
  if [[ "$line" == *"$1"* ]]; then
    #echo "there"
    
    studentID=${line:44:56}
    #echo Student ID: ${studentID}
  fi
done < "$input"

#ok now we loop every file in circuit and check if studentID is on it.

circuitPath="circuits"
allProjID=" "
for file in circuits/*
do
    while IFS= read -r line
    do #for every file in circuits, we are reading every line. lol
        if [[ "$line" == *"$1"* ]] 
        then
            #echo $line
            ((count=count+1))
        fi
    #fi
    done < "$file"

    
done
echo $count
#echo $allProjID

exit 0
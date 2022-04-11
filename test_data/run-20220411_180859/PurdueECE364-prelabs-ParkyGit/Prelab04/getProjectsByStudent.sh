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
    do
    #
    #if line contains $1, we strip it >:3
    if [[ "$line" == *"$studentID"* ]]; then
        #echo "there"
        fileID=${file:5:19}
        circID=${fileID:12:20}
        #echo $circID

        #now we know circuit ID so we can sweep and get corresponding project ID
        input4="maps/projects.dat"
        while IFS= read -r line
        do
        #
        #if line contains circID, we strip it >:3
        if [[ "$line" == *"$circID"* ]]; then
            #echo "It's there."
            projID=${line:13:70}
                if [[ "$allProjID" != *"$projID"* ]]; then
                    echo $projID
                fi
            allProjID="$allProjID+$projID"
            #echo $projID
            #echo $allProjID
        fi
        done < "$input4"


    fi
    done < "$file"

    ((count=count+1))
done
#echo Count: $count
#echo $allProjID

exit 0
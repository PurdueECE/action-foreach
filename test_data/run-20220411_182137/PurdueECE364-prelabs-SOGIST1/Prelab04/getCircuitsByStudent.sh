#! /bin/bash
#####################################################################
#     Author: Luke Chigges
#     email:  lchigges@purdue.edu
#     ID:     ee364b02
#     Date:   2/5/22
#####################################################################


# statements here
studentName=$@
# get the student's ID
studentID=$(grep "$studentName" ./maps/students.dat)
studentID="${studentID##* }"

# get all circuits student id is in.
for file in ./circuits/*; do
	circuitID=$(echo $file | cut -c 20-26)
	if grep -q -o $studentID $file; then
		echo $circuitID
	fi
	#echo $circuitID
done

exit 0

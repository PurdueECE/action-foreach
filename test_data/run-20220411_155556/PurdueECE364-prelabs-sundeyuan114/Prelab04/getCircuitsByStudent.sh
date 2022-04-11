#######################################################
# Author: <Deyuan Sun >
# email: <sun829@purdue.edu >
# ID: <ee364a04 >
# Date: <2/5/2022 >
#######################################################
# Write your sequence of statements here.
string="--------------------------------------------"
string2="./circuits/circuit_"
input="./maps/students.dat"

# get every data out
while IFS= read -r line
do
    if [[ "$line" == *"$1"* ]]; then     
        studentID="${line:${#string}:11}"
        break
    fi
done < "$input"

    grep $studentID ./circuits/* > grepoutput.txt

input2="./grepoutput.txt"
list=("")
while IFS= read -r line2
do
    if [[ "$line2" == *"$studentID"* ]]; then  
        if [[ ! " ${list[*]} " =~ " ${line2:${#string2}:7} " ]]; then
            list+="${line2:${#string2}:7}"
            echo "${line2:${#string2}:7}"
        fi
    fi
done < "$input2"
rm grepoutput.txt

exit 0
#######################################################
# Author: <Deyuan Sun >
# email: <sun829@purdue.edu >
# ID: <ee364a04 >
# Date: <2/5/2022 >
#######################################################
# Write your sequence of statements here.

grep $1 ./circuits/* > grepoutput.txt

input2="./grepoutput.txt"
count=0

sed -n '$=' $input2

rm ./grepoutput.txt
exit 0
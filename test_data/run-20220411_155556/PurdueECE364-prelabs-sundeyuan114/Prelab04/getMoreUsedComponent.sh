#######################################################
# Author: <Deyuan Sun >
# email: <sun829@purdue.edu >
# ID: <ee364a04 >
# Date: <2/5/2022 >
#######################################################
# Write your sequence of statements here.

grep $1 ./circuits/* > grepoutput.txt
grep $2 ./circuits/* > grepoutput2.txt

path1="grepoutput.txt"
path2="grepoutput2.txt"


number_of_lines=`wc --lines < $path1`
number_of_lines2=`wc --lines < $path2`

if [[ $number_of_lines -gt $number_of_lines2 ]]
then  
  echo $1
else
  echo $2
fi

rm ./grepoutput.txt
rm ./grepoutput2.txt

exit 0
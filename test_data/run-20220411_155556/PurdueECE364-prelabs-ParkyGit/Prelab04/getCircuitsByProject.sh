 ######################################################
# Author : Erin Park
# email : Park1131@purdue.edu
# ID : ee364a05
# Date : Feb 6, 2022
# ######################################################
# Write your sequence of statements here .

input="maps/projects.dat"
while IFS= read -r line
do
  #
  #if line contains $1, we strip it >:3
  if [[ "$line" == *"$1"* ]]; then
    #echo "It's there."
    
    echo ${line:4:10}
  fi
done < "$input"

exit 0

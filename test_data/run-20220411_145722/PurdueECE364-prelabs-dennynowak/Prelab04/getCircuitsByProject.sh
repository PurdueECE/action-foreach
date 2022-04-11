#! usr/bin/bash

#############################################
#   Author:     Denny Nowak
#   email:      nowak32@purdue.edu
#   ID:         ee364b14
#   Date:       02/05/2022
#############################################

# Take in project ID and print sorted list of Circuit IDs
sort -u -k 1 maps/projects.dat > sortedCircuits # sort circuits into temp file

while read circuits projectID;
do
if [[ $1 = $projectID ]];
then
    echo $circuits
fi
done < sortedCircuits

rm sortedCircuits
exit 0
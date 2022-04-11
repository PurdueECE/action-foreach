#! /bin/bash
#####################################################################
#     Author: Luke Chigges
#     email:  lchigges@purdue.edu
#     ID:     ee364b02
#     Date:   2/5/22
#####################################################################


# statements here
input=$@
cat maps/projects.dat | while read line; do
    projectID="${line##* }" # get last word
    circuit="${line%% *}" # get first word
    if [[ $input == $projectID ]]; then
        echo $circuit
    fi
done

exit 0

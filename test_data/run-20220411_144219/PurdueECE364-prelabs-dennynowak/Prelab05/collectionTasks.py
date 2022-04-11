#####################################
#   Author:     Denny Nowak
#   Email:      nowak32@purdue.edu
#   ID:         ee364b14
#   Date:       02/11/2022
#####################################

import os 
import sys
import re

# Problem 1
# Func that takes in projectID and letter symbol
# Returns the distinct number of components used in all circuits within that project
# If project ID dne, raise valueerror
# project ID to circuit ID | cirucit ID to component ID

def getComponentCountByProject(projectID, componentSymbol):
    # Check if project ID exist
    fptr = open("maps/projects.dat", "r")
    valid = 0
    circuitIDList = []
    for line in fptr.readlines():
        projectIDTest = re.search('          (.*)', line)
        if projectIDTest:
            # check if valid projectID
            temp = projectIDTest.group(1)
            if (temp == projectID):
                valid = 1
                # Add circuit ID to list
                circuitIDList.append(line[4:12])

    fptr.close()
    # Invalid, did not find project ID and raise value error
    if valid == 0:
        raise ValueError('Project ID entered does not exist')

    # Get distinct components from circuit files
    componentList = []
    for circID in circuitIDList:
        fptr = open("circuits/circuit_" + circID[:-1] + ".dat", "r")
        for line in fptr.readlines():
            comp = re.search(' (.{8})', line)
            if comp:
                temp = comp.group(1)
                componentList.append(temp[1:])

    count = 0
    # Pick specific file based on component symbol
    if componentSymbol == 'R':
        fptr = open("maps/resistors.dat", "r")
        for line in fptr.readlines():
            if line[:7] in componentList:
                count += 1
    elif componentSymbol == 'I':
        fptr = open("maps/inductors.dat", "r")
        for line in fptr.readlines():
            if line[:7] in componentList:
                count += 1
    elif componentSymbol == 'C':
        fptr = open("maps/capacitors.dat", "r")
        for line in fptr.readlines():
            if line[:7] in componentList:
                count += 1
    elif componentSymbol == 'T':
        fptr = open("maps/transistors.dat", "r") 
        for line in fptr.readlines():
            if line[:7] in componentList:
                count += 1       

    fptr.close()

    return count

# Problem 2
# Func that takes in student name and component symbol
# returns distinct num of components, valueerrorr if student name dne
def getComponentCountByStudent(studentName, componentSymbol):
    # Check if student name exists
    fptr = open("maps/students.dat", "r")
    valid = 0
    for line in fptr.readlines():
        studentTest = re.search('(.*)( *)\|', line)
        if studentTest:
            # check if valid student
            temp = studentTest.group(1)
            if (studentName.replace(" ", "") == temp.replace(" ","")):
                valid = 1
                # get studentID
                studentID = line[-12:]
                studentID = studentID.strip()
                break
    
    fptr.close()
    # Invalid, did not find student and raise value error
    if valid == 0:
        raise ValueError('Student name entered does not exist')

    # Search all circuit files to check for participants
    found = 0
    componentList = []
    for file in os.listdir("circuits"):
        fptr = open("circuits/"+str(file))
        # check student ID in file
        for line in fptr.readlines():
            # Get components
            if studentID == line.strip():
                found = 1
            if found == 1:
                comp = re.search(' (.{8})', line)
                if comp:
                    temp = comp.group(1)
                    componentList.append(temp[1:])
                    
        fptr.close()
        found = 0

    # Get count
    count = 0
    if componentSymbol == 'R':
        fptr = open("maps/resistors.dat", "r")
        for line in fptr.readlines():
            if line[:7] in componentList:
                count += 1
    elif componentSymbol == 'I':
        fptr = open("maps/inductors.dat", "r")
        for line in fptr.readlines():
            if line[:7] in componentList:
                count += 1
    elif componentSymbol == 'C':
        fptr = open("maps/capacitors.dat", "r")
        for line in fptr.readlines():
            if line[:7] in componentList:
                count += 1
    elif componentSymbol == 'T':
        fptr = open("maps/transistors.dat", "r") 
        for line in fptr.readlines():
            if line[:7] in componentList:
                count += 1     

    fptr.close()

    return count

# Problem 3
# Takes in student name and returns set of project IDS student was in
# if student name dne return valueerror
def getParticipationByStudent(studentName):

    # Check if student name exists
    fptr = open("maps/students.dat", "r")
    valid = 0
    for line in fptr.readlines():
        studentTest = re.search('(.*)( *)\|', line)
        if studentTest:
            # check if valid student
            temp = studentTest.group(1)
            if (studentName.replace(" ", "") == temp.replace(" ","")):
                valid = 1
                # get studentID
                studentID = line[-12:]
                studentID = studentID.strip()
                break
    fptr.close()

    # Invalid, did not find student and raise value error
    if valid == 0:
        raise ValueError('Student name entered does not exist')

    # Search all circuit files to check for participants
    found = 0
    circuitList = []
    for file in os.listdir("circuits"):
        fptr = open("circuits/"+str(file))
        # check student ID in file
        for line in fptr.readlines():
            # Get circuit name
            if studentID == line.strip():
                found = 1
                circuitList.append(file[8:15])
        fptr.close()
        found = 0

    # Search through projects for matching projectIDs
    fptr = open("maps/projects.dat", "r")
    projectSet = set()
    for line in fptr.readlines():
        circuitTest = re.search('    (.*)          ', line)
        if circuitTest:
            temp = circuitTest.group(1)
            if (temp.replace(" ", "") in circuitList):
                projectSet.add(line[-37:-1])

    fptr.close()

    return projectSet

# Problem 4
# Takes in project ID and returns set of students who particpated in project
def getParticipationByProject(projectID):
    # Check if project ID exist
    fptr = open("maps/projects.dat", "r")
    valid = 0
    circuitIDList = []
    for line in fptr.readlines():
        projectIDTest = re.search('          (.*)', line)
        if projectIDTest:
            # check if valid projectID
            temp = projectIDTest.group(1)
            if (temp == projectID):
                valid = 1
                # Add circuit ID to list
                circuitIDList.append(line[4:12])
    fptr.close()

    # Invalid, did not find project ID and raise value error
    if valid == 0:
        raise ValueError('Project ID entered does not exist')

    # Get distinct participants from circuitID
    participantSet = set()
    for circID in circuitIDList:
        fptr = open("circuits/circuit_" + circID[:-1] + ".dat", "r")
        for line in fptr.readlines():
                partID = re.search('(\d{5}-\d{5})', line)
                if partID:
                    temp = partID.group(1)
                    participantSet.add(temp)
        fptr.close()

    # Get full student name from partID
    studentSet = set()
    fptr = open("maps/students.dat", "r")
    for line in fptr.readlines():
        if line[-12:-1] in participantSet:
            # Get student name
            studentName = re.search('(\w*, \w*)', line)
            if studentName:
                temp = studentName.group(1)
                studentSet.add(temp)
    fptr.close()

    return studentSet

# Problem 5
# Takes in nothing and returns projectID:totalCost dict 
def getCostOfProjects():
    
    costDict = {}
    # Go through projectIDs and get circuit IDs
    fptr = open("maps/projects.dat", "r")
    circuitIDList = []
    prevID = ''
    startFlag = 0
    for line in fptr.readlines():
        projectIDTest = re.search('(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})', line)
        # Valid project ID
        if projectIDTest:
            # Check if new key
            if prevID != projectIDTest.group(1):
                if (startFlag == 1):
                    # Process previous project ID
                    # Get distinct components from circuit files
                    componentList = []
                    for x in circuitIDList:
                        fptr2 = open("circuits/circuit_" + x + ".dat", "r")
                        for line2 in fptr2.readlines():
                            comp = re.search(' (.{8})', line2)
                            if comp:
                                temp = comp.group(1)
                                componentList.append(temp[1:])
                        fptr2.close()
                    
                    # Get cost of components
                    totalCost = 0
                    # Resistors
                    fptr2 = open("maps/resistors.dat", "r")
                    for line2 in fptr2.readlines():
                        if line2[:7] in componentList:
                            totalCost += float(line2[-5:-1])
                    
                    # Add to dictionary
                    costDict.update({prevID:round(totalCost,2)})

                    
                else:
                    startFlag = 1 # first project ID
                prevID = projectIDTest.group(1)
                circuitIDList = []
                circuitIDList.append(line[4:11])
                
            else:
                # add circuit ID
                circuitIDList.append(line[4:11])

    fptr.close()
    # Do last case
    componentList = []
    for x in circuitIDList:
        fptr2 = open("circuits/circuit_" + x + ".dat", "r")
        for line2 in fptr2.readlines():
            comp = re.search(' (.{8})', line2)
            if comp:
                temp = comp.group(1)
                componentList.append(temp[1:])
        fptr2.close()

    # Get cost of components
    totalCost = 0
    # Resistors
    fptr2 = open("maps/resistors.dat", "r")
    for line2 in fptr2.readlines():
        if line2[:7] in componentList:
            totalCost += float(line2[-5:-1])

    # Add to dictionary
    costDict.update({prevID:round(totalCost,2)})
    return costDict

# Problem 6
# Takes in set of component IDs and returns set of project IDs 
def getProjectByComponent(componentIDs):
    projectSet = set()
    # Search through circuit files for component ID
    for file in os.listdir("circuits"):
        fptr = open("circuits/"+str(file))
        # check comp ID in file
        for line in fptr.readlines():
            # Get components
            comp = re.search(' (.{8})', line)
            if comp:
                temp = comp.group()
                temp = temp[2:]
                # Check if comp ID is in set
                if temp in componentIDs:
                    # Get project ID
                    fptr2 = open("maps/projects.dat", "r")
                    for line2 in fptr2.readlines():
                        projectIDTest = re.search('(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})', line2)
                        # Valid project ID
                        if projectIDTest:
                            # Find matching circuit ID
                            if file[8:15] in line2:
                                projectSet.add(projectIDTest.group(1))
                    fptr2.close()
        fptr.close()

    return projectSet

# Problem 7
# Returns sorted list of all distinct comps that have been used in both projects passed
def getCommonByProject(projectID1, projectID2):

    # Check if valid IDs
    fptr = open("maps/projects.dat", "r")
    valid1 = 0
    valid2 = 0
    circuitIDList1 = []
    circuitIDList2 = []
    for line in fptr.readlines():
        projectIDTest = re.search('          (.*)', line)
        if projectIDTest:
            # check if valid projectID
            temp = projectIDTest.group(1)
            if (temp == projectID1):
                valid1 = 1
                if (projectID1 == projectID2):
                    valid2 = 1
                    circuitIDList2.append(line[4:12])
                # Add circuit ID to list
                circuitIDList1.append(line[4:12])
            elif (temp == projectID2):
                valid2 = 1
                # Add circuit ID to list
                circuitIDList2.append(line[4:12])

    fptr.close()
    # Invalid, did not find project ID and raise value error
    if valid1 == 0 or valid2 == 0:
        raise ValueError('Project ID entered does not exist')
    
    # Get distinct components from circuit files
    componentSet1 = set()
    componentSet2 = set()

    # First list
    for circID in circuitIDList1:
        fptr = open("circuits/circuit_" + circID[:-1] + ".dat", "r")
        for line in fptr.readlines():
            comp = re.search(' (.{8})', line)
            if comp:
                temp = comp.group(1)
                componentSet1.add(temp[1:])
        fptr.close()
    
    # Second list
    for circID in circuitIDList2:
        fptr = open("circuits/circuit_" + circID[:-1] + ".dat", "r")
        for line in fptr.readlines():
            comp = re.search(' (.{8})', line)
            if comp:
                temp = comp.group(1)
                componentSet2.add(temp[1:])
        fptr.close()
    commonSet = componentSet1.intersection(componentSet2)
    commonList = sorted(commonSet)
    return commonList

# Problem 8 
# Takes in set of component IDs and returns {compID:totalVal}
def getComponentReport(componentIDs):

    count = 0
    compDict = {}
    # Iterate through componentID
    for comp in componentIDs:
        # Check every circuit file
        for file in os.listdir("circuits"):
            fptr = open("circuits/"+str(file))
            for line in fptr.readlines():
                # Get components
                comp2 = re.search(' (.{8})', line)
                if comp2:
                    temp = comp2.group()
                    temp = temp[2:]
                    if temp == comp:
                        count += 1            
            fptr.close()
        compDict.update({comp: count})
        count = 0

    return compDict

# Problem 9
# Takes in set of student names and returns set of all circuit IDs that any student worked on
def getCircuitByStudent(studentNames):

    circuitSet = set()
    # Go through set
    for stud in studentNames:
        # Get stud ID
        fptr = open("maps/students.dat", "r")
        for line in fptr.readlines():
            studentTest = re.search('(.*)( *)\|', line)
            if studentTest:
                # check if valid student
                temp = studentTest.group(1)
                if (stud.replace(" ", "") == temp.replace(" ","")):
                    valid = 1
                    # get studentID
                    studentID = line[-12:]
                    studentID = studentID.strip()
                    break
        fptr.close()

        # Search circuits with student ID
        for file in os.listdir("circuits"):
            fptr = open("circuits/"+str(file))
            for line in fptr.readlines():
                # Check id in circuit
                if studentID == line.strip():
                    circuitSet.add(file[8:15])
                        
            fptr.close()

    return circuitSet

# Problem 10
# Takes in set of component IDs and returns all circuitIDs that any comp used in
def getCircuitByComponent(componentIDs):
    
    circuitSet = set()
     # Go through component set
    for comp in componentIDs:
        # Search circuits with comp
        for file in os.listdir("circuits"):
            fptr = open("circuits/"+str(file))
            for line in fptr.readlines():
                # Check if comp in circuit
                if comp in line:
                    circuitSet.add(file[8:15])
            fptr.close()  
   
    return circuitSet

# Testing
if __name__ == "__main__":
    #getComponentCountByProject('90BE0D09-1438-414A-A38B-8309A49C02EF', 'C')
    #count = getComponentCountByProject('082D6241-40EE-432E-A635-65EA8AA374B6', 'R')
    #count += getComponentCountByProject('082D6241-40EE-432E-A635-65EA8AA374B6', 'T')
    #count += getComponentCountByProject('082D6241-40EE-432E-A635-65EA8AA374B6', 'C')
    #count += getComponentCountByProject('082D6241-40EE-432E-A635-65EA8AA374B6', 'I')
    #count = getComponentCountByStudent("Henderson, Christopher", "R")
    #projectSet = getParticipationByStudent("Adams, Keith")
    #print(getParticipationByProject('96CC6F98-B44B-4FEB-A06B-390432C1F6EA'))
    #costDict = getCostOfProjects()
    #compSet = {'CEC-489', 'YQC-438','GLZ-901'}
    #getProjectByComponent(compSet)
    #print(getCommonByProject('082D6241-40EE-432E-A635-65EA8AA374B6', '90BE0D09-1438-414A-A38B-8309A49C02EF'))
    #compDict = getComponentReport(compSet)
    #print(compDict)
    #studSet = {'White, Diana', 'Young, Frank'}
    #print(getCircuitByStudent(studSet))
    #print(getCircuitByComponent(compSet))
    pass
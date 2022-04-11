# ######################################################
# Author :  Xingjian Wang
# email :   wang5066@purdue.edu
# ID:       ee364b03
# Date :    Feb 12, 2022
# ######################################################

import os # List of module import statements
from enum import Enum
import re
from os import listdir
from os.path import isfile, join

PROJECT_DATABASE="maps/projects.dat"
STUDENT_DATABASE="maps/students.dat"
RESISTOR_DATABASE="maps/resistors.dat"
INDUCTOR_DATABASE="maps/inductors.dat"
CAPACITOR_DATABASE="maps/capacitors.dat"
TRANSISTOR_DATABASE="maps/transistors.dat"

TEMP_FILE_PATH="temp.txt"
TEMP_FILE_2_PATH="temp2.txt"

class RequiredType(Enum):
    ID = 1
    ID_AND_COST = 2


# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################
# Helper
# This function returns a ID set from @filePointer.
def _readSet(filePointer):
    dataSet = set()
    for line in filePointer:
        data = re.match("[A-Z]{3}[-][0-9]{3}", line)
        if data:
            dataSet.add(data.group()) 
    filePointer.close() 
    return dataSet


# This functions returns a ID-cost dict from @filePointer.
def _readDict(filePointer):
    pass
    # resistorIDSet = set()
    # f = open(RESISTOR_DATABASE)
    # for line in f:
    #     data = re.match("([A-Z]{3}[-][0-9]{3})(\W*)[$]([0-9]*[.][0-9]*)",line)
    #     if data:
    #         dataSet
    # f.close()
    # filePointer.close() 


# This helper function builds the collection based on @componentSymbol and
# @requiredType. The output is as follow:
# ID:   ID -> Set
# ID_AND_COST:  (ID, cost) -> Dictionary
def _getData(componentSymbol, DataType):
    filepath = None    
    if componentSymbol == "R":
        filePath = RESISTOR_DATABASE
    elif componentSymbol == "I":
        filePath = INDUCTOR_DATABASE
    elif componentSymbol == "C":
        filePath = CAPACITOR_DATABASE
    elif componentSymbol == "T":
        filePath = TRANSISTOR_DATABASE
    else:
        raise ValueError("This symbol is not valid (should be R or I or C or T).")
    file = open(filePath, "r")
    # file is closed inside these two helper functions
    if DataType is RequiredType.ID:
        return _readSet(file)
    elif DataType is RequiredType.ID_AND_COST:
        return _readDict(file)
    return 0
    
    
# This function returns a set of circuitID given a @projectID
# Prereq: @projectID exists
def _projectToCircuit(projectID):
    circuitIDSet = set()
    projectIDLines = []
    projectFile = open(PROJECT_DATABASE, "r")
    
    # find the line contains the projectID first, and
    # put them into a list
    for line in projectFile:
        if projectID in line:
            projectIDLines.append(line)
    
    # Then, get circuitID from this list
    for line in projectIDLines:
        data = re.match("(\W*)([0-9]{2}[-][0-9][-][0-9]{2})(\W*)(\w*)(\W*)", line)
        if data:
            circuitIDSet.add(data.group(2)) # this adds circuitID
    
    projectFile.close()
    return circuitIDSet
    
 
# This functions return a set of componentID given a @circuitID
# Prereq: @circuitID exists
def _CircuitToComponent(circuitID):
    componentIDSet = set()
    circuitFileName = "circuits/circuit_" + circuitID + ".dat"
    circuitFile = open(circuitFileName, "r")
    
    for line in circuitFile:
        data = re.match("(\W*)([A-Z]{3}[-][0-9]{3})(\W*)", line)
        if data:
            componentIDSet.add(data.group(2))
            
    circuitFile.close()
    return componentIDSet


# This functions return a set of circuitID given a @studentID
# Prereq: @studentID exists
def _studentToCircuit(studentID):
    # Read from all files
    files = [f for f in listdir("circuits/") if isfile(join("circuits/", f))]
    os.chdir("circuits/")   # go into circuits folder for handy
    circuitIDSet = set()
    for file in files:
        f = open(file, "r")
        for line in f:
            if studentID in line:
                circuitIDMatch = re.match("[a-z]+[_]([0-9]+[-][0-9]+[-][0-9]+)[.][a-z]+", file)
                if circuitIDMatch:
                    circuitIDSet.add(circuitIDMatch.group(1))
                break
        f.close()

    os.chdir("..")          # go back for next function
    return circuitIDSet


# This functions return a set of projectID given a @circuitID
# Prereq: @circuitID exists
def _circuitToProject(circuitID):
    projectFile = open(PROJECT_DATABASE, "r")
    projectIDSet = set()
    for line in projectFile:
        if circuitID in line:
            data = re.match("(\W*)([0-9]{2}[-][0-9][-][0-9]{2})(\W*)(\S*)(\W*)", line)
            if data:
                projectIDSet.add(data.group(4))       
    projectFile.close()
    return projectIDSet


# This functions return a set of studentID given a @circuitID
# Prereq: @circuitID exists
def _circuitToStudent(circuitID):
    studentIDSet = set()
    circuitFileName = "circuits/circuit_" + circuitID + ".dat"
    circuitFile = open(circuitFileName, "r")

    for line in circuitFile:
        data = re.match("(\W*)([0-9]{5}[-][0-9]{5})(\W*)", line)
        if data:
            studentIDSet.add(data.group(2))
    
    circuitFile.close()
    return studentIDSet    


# Check if the projectID exists or is valid input
def _checkProjectID(projectID):
    # Check if the projectID is in valid format
    PROJECT_ID_LENGTH = 36
    if len(projectID) != PROJECT_ID_LENGTH:
        raise ValueError("The projectID should be a valid length.")
    
    # Check if the projectID exists
    projectFile = open(PROJECT_DATABASE, "r")
    projectID_valid = False
    
    for line in projectFile:
        if projectID in line:
            projectID_valid = True
            break
        
    if not projectID_valid:
        raise ValueError("ProjectID does not exist.")
    
    projectFile.close()


# Check if the student name exists
# If exists, return the studentID.
def _checkStudentName(studentName):
    studentFile = open(STUDENT_DATABASE, "r")
    studentName_valid = False
    studentID = "No Matching"
    
    for line in studentFile:
        if studentName in line:
            studentName_valid = True
            # studentName -> studentID
            studentIDMatch = re.match("(.*?)([0-9]{5}[-][0-9]{5})(\W*)", line)
            if studentIDMatch:
                studentID = studentIDMatch.group(2)

            break
        
    if not studentName_valid:
        raise ValueError("Student name does not exist.")  
    
    studentFile.close()
    return studentID


# This functions return the student name given a @studentID
# Prereq: @studentID exists
def _studentIDToStudentName(studentID):
    studentFile = open(STUDENT_DATABASE, "r")
    studentName = ""
    
    for line in studentFile:
        if studentID in line:
            studentNameMatch = re.match("(\W*)((\w*)[,](\s)(\w*))(\W*)([0-9]{5}[-][0-9]{5})(\W*)", line)
            if studentNameMatch:
                studentName = studentNameMatch.group(2)
                
    studentFile.close()            
    return studentName


 # This functions return a set of circuitID given a @componentID
# Prereq: @componentID exists
def _componentToCircuit(componentID):
# Read from all files
    files = [f for f in listdir("circuits/") if isfile(join("circuits/", f))]
    os.chdir("circuits/")   # go into circuits folder for handy
    circuitIDSet = set()
    for file in files:
        f = open(file, "r")
        for line in f:
            if componentID in line:
                componentIDMatch = re.match("(\W*)([A-Z]{3}[-][0-9]{3})(\W*)", line)
                if componentIDMatch:
                    circuitIDSet.add(componentIDMatch.group(1))
                break
        f.close()

    os.chdir("..")          # go back for next function
    
    return circuitIDSet


# Q1
def getComponentCountByProject(projectID, componentSymbol):
    # Check projectID exists
    _checkProjectID(projectID)
    
    # ProjectID -> CircuitID
    circuitIDSet = _projectToCircuit(projectID)

    # CircuitID -> ComponentID
    componentIDSet = set()
    for circuitID in circuitIDSet:
        componentIDSet.update(_CircuitToComponent(circuitID))
        
    # ComponentID -> Type
    componentIDAllSet = _getData(componentSymbol, RequiredType.ID)
    resultSet = componentIDAllSet.intersection(componentIDSet)

    return len(resultSet)
    

# Q2
def getComponentCountByStudent(studentName, componentSymbol):
    # Check if the studentName exists
    studentID = _checkStudentName(studentName)

    # studentID -> CircuitID
    circuitIDSet = _studentToCircuit(studentID)
    
    # CircuitID -> ComponentID
    componentIDSet = set()
    for circuitID in circuitIDSet:
        componentIDSet.update(_CircuitToComponent(circuitID))
        
    # ComponentID -> Type
    componentIDAllSet = _getData(componentSymbol, RequiredType.ID)
    resultSet = componentIDAllSet.intersection(componentIDSet)
    
    return len(resultSet)
    

# Q3
def getParticipationByStudent(studentName):
    studentID = _checkStudentName(studentName)
    
    # studentID -> CircuitID
    circuitIDSet = _studentToCircuit(studentID)

    # CircuitID -> ProjectID
    projectIDSet = set()
    for circuitID in circuitIDSet:
        projectIDSet.update(_circuitToProject(circuitID))
    
    return projectIDSet

# Q4
def getParticipationByProject(projectID):
    _checkProjectID(projectID)
    
    # projectID -> CircuitID
    circuitIDSet = _projectToCircuit(projectID)
    
    # CircuitID -> StudentID
    studentIDSet = set()
    for circuitID in circuitIDSet:
        studentIDSet.update(_circuitToStudent(circuitID))
        
    # StudentID -> StudentName
    studentNameSet = set()
    for studentID in studentIDSet:
        studentNameSet.add(_studentIDToStudentName(studentID))
    
    return studentNameSet
    

# Q5
def getCostOfProjects():
    pass


# Q6
def getProjectByComponent(componentIDs):
    # ComponentID -> CircuitID
    circuitIDSet = set()
    for componentID in componentIDs:
        circuitIDSet.update(_componentToCircuit(componentID))
    
    # CircuitID -> ProjectID
    projectIDSet = set()
    for circuitID in circuitIDSet:
        projectIDSet.update(_circuitToProject(circuitID))
        
    return projectIDSet


# Q7
def getCommonByProject(projectID1, projectID2):
    _checkProjectID(projectID1)
    _checkProjectID(projectID2)
    
    # ProjectID -> CircuitID
    circuitIDSet1 = _projectToCircuit(projectID1)
    circuitIDSet2 = _projectToCircuit(projectID2)
    
    # CircuitID -> ComponentID
    componentIDSet1 = set()
    componentIDSet2 = set()
    for circuitID in circuitIDSet1:
        componentIDSet1.update(_CircuitToComponent(circuitID))
    for circuitID in circuitIDSet2:
        componentIDSet2.update(_CircuitToComponent(circuitID))
    
    # Find common
    commonSet = componentIDSet1.intersection(componentIDSet2)
    return sorted(commonSet)
        

# Q8
def getComponentReport(componentIDs):
    componentCountdict = {}
    for componentID in componentIDs:
        # ComponentID -> CircuitID
        circuitIDSet = _componentToCircuit(componentID)
        # CircuitID -> ProjectID
        projectIDSet = set()
        for circuitID in circuitIDSet:
            projectIDSet.update(_circuitToProject(circuitID))
        componentCountdict[componentID] = len(projectIDSet)
    
    return componentCountdict

# Q9
def getCircuitByStudent(studentNames):
    studentIDSet = set()
    for studentName in studentNames:
        studentIDSet.update(_checkStudentName(studentName))
    
    # StudentID -> CircuitID
    circuitIDSet = set()
    for studentID in studentIDSet:
        circuitIDSet.update(_studentToCircuit(studentID))       
        
    return circuitIDSet

# Q10
def getCircuitByComponent(componentIDs):
    # ComponentID -> CircuitID
    circuitIDSet = set()
    for componentID in componentIDs:
        circuitIDSet.update(_componentToCircuit(componentID))
        
    return circuitIDSet
            
                
# This block is optional and is used for testing .
# ######################################################
# if __name__ == " __main__ ":
test_projectID = "082D6241-40EE-432E-A635-65EA8AA374B6"
test_projectID2 = "90BE0D09-1438-414A-A38B-8309A49C02EF"
print(getComponentCountByProject(test_projectID, "T"))
test_studentName = "Watson, Martin"
print(getComponentCountByStudent(test_studentName, "R"))
print(getParticipationByStudent(test_studentName))
print(getParticipationByProject(test_projectID))
print(getProjectByComponent({'ZHR-274', 'MAL-574'}))
print(getCommonByProject(test_projectID, test_projectID2))
print(getComponentReport({'ZHR-274', 'MAL-574'}))
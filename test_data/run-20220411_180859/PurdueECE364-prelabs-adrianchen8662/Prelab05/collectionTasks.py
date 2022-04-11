# ######################################################
# Author : Adrian Chen
# email : chen3124@purdue.edu
# ID : ee364b10
# Date : 2/7/2022
# ######################################################

import os # List of module import statements
import sys # Each one on a line

# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################

def getComponentCountByProject(projectID, componentSymbol):
    # read file in maps
    if (componentSymbol == "R"):
        if os.path.exists('maps/resistors.dat') and os.access('maps/resistors.dat', os.R_OK):
            componentFile = open('maps/resistors.dat').readlines()
        else:
            print("Error reading component file")
            return
    elif (componentSymbol == "I"):
        if os.path.exists('maps/inductors.dat') and os.access('maps/inductors.dat', os.R_OK):
            componentFile = open('maps/inductors.dat').readlines()
        else:
            print("Error reading component file")
            return
    elif (componentSymbol == "C"):
        if os.path.exists('maps/capacitors.dat') and os.access('maps/capacitors.dat', os.R_OK):
            componentFile = open('maps/capacitors.dat').readlines()
        else:
            print("Error reading component file")
            return
    elif (componentSymbol == "T"):
        if os.path.exists('maps/transistors.dat') and os.access('maps/transistors.dat', os.R_OK):
            componentFile = open('maps/transistors.dat').readlines()
        else:
            print("Error reading component file")
            return
    else:
        print("Invalid component symbol!")
        return

    count = 0
    if os.path.exists("circuits/circuit_"+projectID+".dat") and os.access("circuits/circuit_"+projectID+".dat", os.R_OK):
        projectFile = open("circuits/circuit_"+projectID+".dat").readlines()
    else:
        print("Error reading project file")
        return
    for projectComponent in projectFile:
        for componentSymbol in componentFile:
            if projectComponent[2:9] == componentSymbol[0:7]:
                count+=1
    return count

def getComponentCountByStudent(studentName, componentSymbol):
    studentFile = open('maps/students.dat').readlines()
    for studentNames in studentFile:
        if studentName == (studentNames[0:28]).strip():
            studentID = studentNames[44:55]

    count = 0
    for filename in os.listdir('circuits'):
        projectFile = open('circuits/'+filename).readlines()
        for projectParticipants in projectFile:
            if (studentID == projectParticipants[0:11]):
                count+=1
    return count

# print(getComponentCountByStudent("Adams, Keith","R"))

def getParticipationByStudent(studentName):
    circuits = {1}
    circuits.remove(1)

    studentFile = open('maps/students.dat').readlines()
    for studentNames in studentFile:
        if studentName == (studentNames[0:28]).strip():
            studentID = studentNames[44:55]
    for filename in os.listdir('circuits'):
        circuitFile = open('circuits/'+filename).readlines()
        for studentName in circuitFile:
            if studentID == studentName[0:11]:
                circuits.add(filename[8:15])
    return circuits

def getParticipationByProject(projectID):
    studentID = {1}
    studentID.remove(1)
    projectFile = open('maps/projects.dat').readlines()
    for projects in projectFile:
        if projectID == (projects[21:57]):
            project = projects[4:11]
    for filename in os.listdir('circuits'):
        if filename[8:15] == project:
            file = filename
    # print(file)
    circuitFile = open('circuits/'+file).readlines()

    for i in range(2,len(circuitFile)-3):
        if (circuitFile[i] == "Components:\n"):
            break
        studentID.add(circuitFile[i][:-1])
    studentID.remove("")
    return studentID

# print(getParticipationByProject("082D6241-40EE-432E-A635-65EA8AA374B6"))

def getCostOfProjects():
            
    return

def getProjectByComponent(componentIDs):
    circuits = {1}
    circuits.discard(1)
    projectNames = {1}
    projectNames.discard(1)

    for filename in os.listdir('circuits'):
        circuitFile = open('circuits/'+filename).readlines()
        for component in circuitFile:
            for componentID in componentIDs:
                if componentID == component[2:9]:
                    circuits.add(filename[8:15])
    
    projects = open('maps/projects.dat').readlines()
    for projectName in projects:
        for circuit in circuits:
            if (circuit == projectName[4:11]):
                projectNames.add(projectName[21:57])
    
    return projectNames

# print(getProjectByComponent({"TAZ-349"}))

def getCommonByProject(projectID1, projectID2):
    componentList = ["test"]
    circuitNames = open('maps/projects.dat').readlines()
    for i in circuitNames:
        if i[21:57] == projectID1:
            circuitID1 = i[4:11]        
        if i[21:57] == projectID2:
            circuitID2 = i[4:11]
    componentSearch = open('circuits/circuit_'+circuitID1+'.dat').readlines()
    for i in range(9,len(componentSearch)-9):
        componentList.append(componentSearch[i])
    componentSearch = open('circuits/circuit_'+circuitID2+'.dat').readlines()
    for i in range(9,len(componentSearch)-9):
        componentList.append(componentSearch[i])
    
    componentOutput = []
    for i in componentList:
        if (i != "-------------\n"):
            componentOutput.append(i.strip())

    return list(set(componentOutput[1:]))

# print(getCommonByProject("082D6241-40EE-432E-A635-65EA8AA374B6","90BE0D09-1438-414A-A38B-8309A49C02EF"))

def getComponentReport(componenetIDs):

    return

def getCircuitByStudent(studentNames):
    circuits = {1}
    circuits.discard(1)
    studentIDs = {1}
    studentIDs.discard(1)

    studentFile = open('maps/students.dat').readlines()
    for studentName in studentFile:
        for student in studentNames:
            if (student == (studentName[0:28]).strip()):
                studentIDs.add(studentName[44:55])
    # print(studentIDs)
    for filename in os.listdir('circuits'):
        circuitFile = open('circuits/'+filename).readlines()
        for studentName in circuitFile:
            for studentID in studentIDs:
                if studentID == studentName[0:11]:
                    circuits.add(filename[8:15])
    return circuits

# print(getCircuitByStudent({"Adams, Keith"}))

def getCircuitByComponent(componentIDs):
    circuits = {1}
    circuits.discard(1)

    for filename in os.listdir('circuits'):
        circuitFile = open('circuits/'+filename).readlines()
        for component in circuitFile:
            for componentID in componentIDs:
                if componentID == component[2:9]:
                    circuits.add(filename[8:15])
    return circuits

# print(getCircuitByComponent({"TFL-784"}))
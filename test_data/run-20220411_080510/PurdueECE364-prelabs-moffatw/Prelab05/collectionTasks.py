# ######################################################
# Author : William Moffat
# email : moffatw@purdue.edu
# ID : ee364b13
# Date : 2/12/2022
# ######################################################

import os 
import sys
import glob 

def getComponentCountByProject(projectID, componentSymbol):
    # Get all circuits associated with the project
    circuits = []
    FILE = open("maps/projects.dat", "r")
    for line in FILE:
        if (len(line.split()) != 2):
            continue

        circuit = line.split()[0]
        ID = line.split()[1]
        if (ID == projectID):
            circuits.append(circuit)

    FILE.close()
    if (len(circuits) == 0):
        raise ValueError("Project ID does not exist\n")

    # Get all components from each circuit
    components = []
    for file in glob.glob("circuits/*.dat"):
        if file[17:24] in circuits:
            FILE = open(file, "r")
            for line in FILE:
                if (len(line.split()) != 1):
                    continue
                if (len(line.split()[0]) == 7):
                    components.append(line.split()[0])
            FILE.close()


    # Search resistor/inductor/capacitor/transistor files for the components

    if componentSymbol == "R":
        FILE = open("maps/resistors.dat", "r")
    if componentSymbol == "I":
        FILE = open("maps/inductors.dat", "r")
    if componentSymbol == "C":
        FILE = open("maps/capacitors.dat", "r")
    if componentSymbol == "T":
        FILE = open("maps/transistors.dat", "r")

    count = 0
    for line in FILE:
        if (len(line.split()) != 2):
            continue

        if line.split()[0] in components:
            count = count + 1

    FILE.close()
    return count

def getComponentCountByStudent(studentName, componentSymbol):
    # Get student ID
    studentID = ""
    FILE = open("maps/students.dat", "r")
    for line in FILE:

        if (len(line.split()) != 4):
            continue

        if ((line.split()[0] + " " + line.split()[1]) == studentName):
            studentID = line.split()[3]

    FILE.close()
    if (studentID == ""):
        raise ValueError("Student does not exist\n")

    # Get all components student worked on 
    components = []
    for file in glob.glob("circuits/*.dat"):
        FILE = open(file, "r")
        if studentID in FILE.read():
            FILE.seek(0)
            for line in FILE:
                if (len(line.split()) != 1):
                    continue
                if (len(line.split()[0]) == 7):
                    components.append(line.split()[0])
        FILE.close()

    # Search resistor/inductor/capacitor/transistor files for the components

    if componentSymbol == "R":
        FILE = open("maps/resistors.dat", "r")
    if componentSymbol == "I":
        FILE = open("maps/inductors.dat", "r")
    if componentSymbol == "C":
        FILE = open("maps/capacitors.dat", "r")
    if componentSymbol == "T":
        FILE = open("maps/transistors.dat", "r")

    count = 0
    for line in FILE:
        if (len(line.split()) != 2):
            continue

        if line.split()[0] in components:
            count = count + 1

    FILE.close()
    return count

def getParticipationByStudent(studentName):
    # Get student ID
    studentID = ""
    FILE = open("maps/students.dat", "r")
    for line in FILE:

        if (len(line.split()) != 4):
            continue

        if ((line.split()[0] + " " + line.split()[1]) == studentName):
            studentID = line.split()[3]

    FILE.close()
    if (studentID == ""):
        raise ValueError("Student does not exist\n")

    # Get circuits student participated in
    circuits = []
    for file in glob.glob("circuits/*.dat"):
        FILE = open(file, "r")
        if studentID in FILE.read():
            circuits.append(file[17:24])

    # Get projects student participated in
    projects = set()
    FILE = open("maps/projects.dat", "r")
    for line in FILE:
        if (len(line.split()) != 2):
            continue
        
        if (line.split()[0] in circuits):
            projects.add(line.split()[1])

    FILE.close()
    return projects


def getParticipationByProject(projectID):
    # Get all circuits associated with the project
    circuits = []
    FILE = open("maps/projects.dat", "r")
    for line in FILE:
        if (len(line.split()) != 2):
            continue

        circuit = line.split()[0]
        ID = line.split()[1]
        if (ID == projectID):
            circuits.append(circuit)

    FILE.close()
    if (len(circuits) == 0):
        raise ValueError("Project ID does not exist\n")

    # Get student IDs from each circuit
    studentIDs = []
    for file in glob.glob("circuits/*.dat"):
        FILE = open(file, "r")
        for line in FILE:
            if (len(line.split()) != 1):
                continue
            if (len(line.split()[0]) == 11):
                studentIDs.append(line.split()[0])
        FILE.close()

    # Get full names of students from the student IDs
    studentNames = set()
    FILE = open("maps/students.dat", "r")
    for line in FILE:

        if (len(line.split()) != 4):
            continue

        if (line.split()[3] in studentIDs):
            studentNames.add((line.split()[0] + " " + line.split()[1]))

    FILE.close()
    return studentNames

#def getCostOfProjects():

def getProjectByComponent(componentIDs):
    # Get circuits that contains any of the component IDs
    circuits = []
    for file in glob.glob("circuits/*.dat"):
        FILE = open(file, "r")
        for line in FILE:
            if (len(line.split()) != 1):
                continue
            if (line.split()[0] in componentIDs):
                circuits.append(file[17:24])
        FILE.close()

    # Get projects that contain any of the circuits
    projects = set()
    FILE = open("maps/projects.dat", "r")
    for line in FILE:
        if (len(line.split()) != 2):
            continue
        
        if (line.split()[0] in circuits):
            projects.add(line.split()[1])

    FILE.close()
    return projects

#def getCommonByProject(projectID1, projectID2):

#def getComponentReport(componentIDs):

def getCircuitByStudent(studentNames):
    # Get student IDs
    studentIDs = []
    FILE = open("maps/students.dat", "r")
    for line in FILE:

        if (len(line.split()) != 4):
            continue

        if ((line.split()[0] + " " + line.split()[1]) in studentNames):
            studentIDs.append(line.split()[3])

    FILE.close()

    # Get circuit IDs that any of the students have worked on
    circuits = set()
    for file in glob.glob("circuits/*.dat"):
        FILE = open(file, "r")
        for line in FILE:
            if (len(line.split()) != 1):
                continue
            if (line.split()[0] in studentIDs):
                circuits.add(file[17:24])
        FILE.close()

    return circuits

def getCircuitByComponent(componentIDs):
    # Get circuits that contains any of the component IDs
    circuits = set()
    for file in glob.glob("circuits/*.dat"):
        FILE = open(file, "r")
        for line in FILE:
            if (len(line.split()) != 1):
                continue
            if (line.split()[0] in componentIDs):
                circuits.add(file[17:24])
        FILE.close()

    return circuits

print(getComponentCountByProject("082D6241-40EE-432E-A635-65EA8AA374B6", "I"))
print(getComponentCountByStudent("Scott, Michael", "I"))
print(getParticipationByStudent("Scott, Michael"))
print(getParticipationByProject("082D6241-40EE-432E-A635-65EA8AA374B6"))


componentIDs = set()
componentIDs.add("NOC-324")
print(getProjectByComponent(componentIDs))

studentNames = set()
studentNames.add("Scott, Michael")
print(getCircuitByStudent(studentNames))

print(getCircuitByComponent(componentIDs))

# ######################################################
# Author : < Nimal Padmanabhan >
# email : < npadmana@purdue.edu >
# ID : < ee364b17 >
# Date : < 2/8/22 >
# ######################################################
from logging import raiseExceptions

import os
from re import L # List of module import statements
import sys

from torch import equal # Each one on a line
# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################

# Takes in a projectID and one letter component symbol: "R", "I", "C", "T"
# Should return the distinct number of components of the requested
# type
def getComponentCountByProject(projectID, componentSymbol):
    # raise ValueError("Hi")
    projFilePath = "maps/projects.dat"
    resFilePath = "maps/resistors.dat"
    indFilePath = "maps/inductors.dat"
    capFilePath = "maps/capacitors.dat"
    tranFilePath = "maps/transistors.dat"

    # Project ID to Circuit ID mapping
    projDat = []
    with open(projFilePath) as f:
        lines_after_2 = f.readlines()[2:]
        for lines in lines_after_2:
            mod_line = lines.lstrip()
            mod_line = mod_line.split()
            projDat.append(mod_line)
    # print(projDat)
    
    projListofTups = [tuple(x) for x in projDat if projectID in x]
    # print(len(projListofTups))
    # projIdComps = [tup for tup in projListofTups if projectID in tup]
    # print("---------------------------------")
    # print(projListofTups)
    # Circuit ID to Component ID mapping
    circuit_files = []
    for tup in projListofTups: 
        for circuit in tup:
            if len(circuit) == 7:
                circuit_files.append(circuit)
    # print(circuit_files)

    # Component ID to type mapping
    compList = []
    for file in circuit_files:
        # print("File name: " +str(file))
        with open("circuits/circuit_"+str(file)+".dat") as f:
            for line in f:
                #  Only start reading if there are two spaces 
                # print(line)
                if 'Components' in line:
                    # print(line)
                    for line in f:
                        compList.append(f.read().split())
    # print(compList)

    # Now find the components based on componentSymbol
    compTotal = 0
    for circuitFile in compList:
        # print("Circuit File-----"+ str(circuitFile))
        for comp in circuitFile:
            # print("Comp: "+ str(comp))
            if componentSymbol == "R":
                with open(resFilePath) as f:
                    for line in f:
                        if comp in f.read():
                            compTotal += 1
                            # print("Matches: "+comp , str(compTotal))
                            # print(compTotal)
            elif componentSymbol == "I":
                with open(indFilePath) as f:
                     for line in f:
                        if comp in f.read():
                            compTotal += 1
                            # print("Matches: "+comp)

            elif componentSymbol == "C":
                with open(capFilePath) as f:
                    for line in f:
                        if comp in f.read():
                            compTotal += 1
                            # print("Matches: "+comp)

            elif componentSymbol == "T":
                with open(tranFilePath) as f:
                     for line in f:
                        if comp in f.read():
                            compTotal += 1
                            # print("Matches: "+comp)
            else:
                print("Invalid Component!")

    # If the component total is 0, that means the project ID wasn't valid
    # Maybe not so when the project ID genuinely has no components, but idk
    if compTotal == 0:
        raise ValueError("Invalid Project ID")
  
    return compTotal
# Takes in student name and component symbol 
# Returns the distinct number of components of the requested type
# Return 0 if student has not been in any projects
# Raise a ValueError if student name does not exist
def getComponentCountByStudent(studentName, componentSymbol):
    
    studentFilePath = "maps/students.dat"
    resFilePath = "maps/resistors.dat"
    indFilePath = "maps/inductors.dat"
    capFilePath = "maps/capacitors.dat"
    tranFilePath = "maps/transistors.dat"
    studentDict = {} # Contains full name and student ID

    with open(studentFilePath) as f:
        lines_after_2 = f.readlines()[2:]
        for line in lines_after_2:
            key, value = line.strip().split('|')
            # print()
            # print(key, value)
            studentDict[key] = value

    # Removes excess spaces
    studentDict = {x.replace(" ", ""):v.replace(" ", "") for x, v in studentDict.items()}
    studentDict = {x.replace(",", ", "):v for x, v in studentDict.items()}

    if studentName not in studentDict:
        raise ValueError("Student name does not exist.")
    # First, get the student ID from the student name
    student_id = studentDict.get(studentName)
    # print(studentDict)
    # Loop through circuits directory and go through each file
    # to find the student IDs that exist
    compList = []
    fileList = []
    compTotal = 0
    for file in os.listdir("circuits/"):
        with open("circuits/"+str(file)) as f:
            # Get all the files where student id is present
            for line in f:
                if student_id in line:
                    fileList.append(file)
    # print(fileList)
    # Now get all the components from the matched files
    for file in fileList:
        with open("circuits/"+str(file)) as f:
            if '  ' in line:
                for line in f:
                    if "-------------" not in line:
                        compList.append(f.read().split())
    compList = [x for x in compList[0] if x != "-------------"]
    print(compList)
    for comp in compList:
        # print("Circuit File-----"+ str(circuitFile))
            # print("Comp: "+ str(comp))
        if componentSymbol == "R":
            with open(resFilePath) as f:
                for line in f:
                    if comp in f.read():
                        compTotal += 1
                        print("Matches: "+comp)
                            # print(compTotal) 
        elif componentSymbol == "I":
            with open(indFilePath) as f:
                for line in f:
                    if comp in f.read():
                        compTotal += 1
                        # print("Matches: "+comp)

        elif componentSymbol == "C":
            with open(capFilePath) as f:
                for line in f:
                    if comp in f.read():
                        compTotal += 1
                    # print("Matches: "+comp)

        elif componentSymbol == "T":
            with open(tranFilePath) as f:
                for line in f:
                    if comp in f.read():
                        compTotal += 1
                            # print("Matches: "+comp)
        else:
            print("Invalid Component!") 
         
    return compTotal

  
# Takes in full student name and returns a set of the project IDs
# the student has participated in    

def getParticipationByStudent(studentName):
    studentFilePath = "maps/students.dat"
    projFilePath = "maps/projects.dat"
    projIDset = set()
    studentDict = {} # Contains full name and student ID

    with open(studentFilePath) as f:
        lines_after_2 = f.readlines()[2:]
        for line in lines_after_2:
            key, value = line.strip().split('|')
            studentDict[key] = value

    # Removes excess spaces
    studentDict = {x.replace(" ", ""):v.replace(" ", "") for x, v in studentDict.items()}
    studentDict = {x.replace(",", ", "):v for x, v in studentDict.items()}
    # print(studentDict)
    if studentName not in studentDict:
        raise ValueError("Student name does not exist.")
     # First, get the student ID from the student name
    student_id = studentDict.get(studentName)
    # Now go through the circuits directory to find which file they're in
    circuitFile = []
    for file in os.listdir("circuits/"):
        with open("circuits/"+str(file)) as f:
            # Get all the files where student id is present
            for line in f:
                if student_id in line:
                    circuit_name = file[8:15]
                    circuitFile.append(circuit_name)
    # print(circuitFile)

    # Now open up the projects.dat to see which
    # projectIDs correspond with the circuit files
    circuittoProjID = []
    with open(projFilePath) as f:
        lines_after_2 = f.readlines()[2:]
        for lines in lines_after_2:
            mod_line = lines.lstrip().split()
            circuittoProjID.append(mod_line)
    print(circuittoProjID)
    for circ in circuitFile:
         for elem in circuittoProjID:
            for name in elem:
               if name == circ:
                   projIDset.add(elem[1])
    
    
    return projIDset

def getParticipationByProject(projectID):
    studentFilePath = "maps/students.dat"
    projFilePath = "maps/projects.dat"
    projPartSet = set()
    projDat = []
    with open(projFilePath) as f:
        lines_after_2 = f.readlines()[2:]
        for lines in lines_after_2:
            mod_line = lines.lstrip().split()
            projDat.append(mod_line)
    
    projListofTups = [tuple(x) for x in projDat]
    
    projIdComps = [tup for tup in projListofTups if projectID in tup]

    # for tup in projListofTups:
    #     for circuit, id in tup:
    #         if id != projectID:
    #             print(id)
    # Circuit ID to Component ID mapping
    circuit_files = []
    for tup in projIdComps: 
        for circuit in tup:
            if len(circuit) == 7:
                circuit_files.append(circuit)
    # print(circuit_files)

    # Component ID to type mapping
    compList = []
    for file in circuit_files:
        # print("File name: " +str(file))
        with open("circuits/circuit_"+str(file)+".dat") as f:
           for line in f.readlines()[2:]:
               if "  " not in line:
                   compList.append(line.strip())

    for comp in compList:
        if comp == "" or comp == "-------------":
            compList.remove(comp)
    
    # Use the dictionary I made to get names from student ids
    # 
    studentDict = {} # Contains full name and student ID
    with open(studentFilePath) as f:
        lines_after_2 = f.readlines()[2:]
        for line in lines_after_2:
            key, value = line.strip().split('|')
            studentDict[key] = value

    # Removes excess spaces
    studentDict = {x.replace(" ", ""):v.replace(" ", "") for x, v in studentDict.items()}
    studentDict = {x.replace(",", ", "):v for x, v in studentDict.items()}
   
    for comp in compList:
        for key, value in studentDict.items():
            if comp == value:
                # print(comp, key)
                projPartSet.add(key)
            
    return projPartSet

# Return a dictionary {string: float}
# key = project ID
# value = total cost of completing that project (rounded to 2 decimals)
def getCostOfProjects():
    projFilePath = "maps/projects.dat"
    resFilePath = "maps/resistors.dat"
    indFilePath = "maps/inductors.dat"
    capFilePath = "maps/capacitors.dat"
    tranFilePath = "maps/transistors.dat"

    partCost = {}
    # Project ID to Circuit ID mapping
    projDat = []
    totalCost = 0e0
    with open(projFilePath) as f:
        lines_after_2 = f.readlines()[2:]
        for lines in lines_after_2:
            mod_line = lines.lstrip().split()
            projDat.append(mod_line)
    
    projListofTups = [tuple(x) for x in projDat]
    
    # projIdComps = [tup for tup in projListofTups if projectID in tup]

    # print(len(projIdComps))
    # Circuit ID to Component ID mapping
    circuit_files = []
    for tup in projListofTups: 
        for circuit in tup:
            if len(circuit) == 7:
                circuit_files.append(circuit)
    print((circuit_files))

    # Component ID to type mapping
    compList = []
    for file in circuit_files:
        # print("File name: " +str(file))
        with open("circuits/circuit_"+str(file)+".dat") as f:
            for line in f:
                #  Only start reading if there are two spaces 
                if '  ' in line:
                    for line in f:
                        compList.append(f.read().split())
    # print(compList)

    compTotal = 0
    
    for circuitFile in compList:
        # print("Circuit File-----"+ str(circuitFile))
        for comp in circuitFile:
            # print("Comp: "+ str(comp))
            with open(resFilePath) as f:
                for line in f:
                    if comp in line:
                       key, value = line.split()
                       partCost[key] = value

    
    return partCost

# Takes in a set of componentIDs 
# Returns the set of projectIDs where these components have
# been used
def getProjectByComponent(componentIDs):
    # First read through each component in each circuit file
    projIDSet = set()
    circuitFile = []
    for comps in componentIDs:
        for file in os.listdir("circuits/"):
            with open("circuits/"+str(file)) as f:
                # Get all the files where component is present
                for line in f:
                    if comps in line:
                        circuit_name = file[8:15]
                        circuitFile.append(circuit_name)

    
    # Now search for these circuit files in the projects.dat file
    projFilePath = "maps/projects.dat"
    circuittoProjID = []
    with open(projFilePath) as f:
        lines_after_2 = f.readlines()[2:]
        for lines in lines_after_2:
            mod_line = lines.lstrip().split()
            circuittoProjID.append(mod_line)
    # print(circuittoProjID)
    for circ in circuitFile:
         for elem in circuittoProjID:
            for name in elem:
               if circ == name:
                   projIDSet.add(elem[1])
    return projIDSet

# Returns a sorted list of all the distinct components
def getCommonByProject(projectID1, projectID2):
    # first open up the projects.dat file
    projFilePath = "maps/projects.dat"
    projDat = []
    commonComps = []
    with open(projFilePath) as f:
        lines_after_2 = f.readlines()[2:]
        for lines in lines_after_2:
            mod_line = lines.lstrip().split()
            projDat.append(mod_line)
    
    projListofTups = [tuple(x) for x in projDat]
    projIdComps1 = [tup for tup in projListofTups if projectID1 in tup]

    projIdComps2 = [tup for tup in projListofTups if projectID2 in tup]

    # print(projIdComps1)
    # print("-------------------------------------------------------------")
    # print(projIdComps2)
    # Circuit ID to Component ID mapping
    circuit_files1 = []
    for tup in projIdComps1: 
        for circuit in tup:
            if len(circuit) == 7:
                circuit_files1.append(circuit)
    # print(circuit_files)
    circuit_files2 = []
    for tup in projIdComps2: 
        for circuit in tup:
            if len(circuit) == 7:
                circuit_files2.append(circuit)

    # Component ID to type mapping
    compList1 = []
    for file in circuit_files1:
        # print("File name: " +str(file))
        with open("circuits/circuit_"+str(file)+".dat") as f:
            for line in f:
                #  Only start reading if there are two spaces 
                if '  ' in line:
                    for line in f:
                        compList1.append(f.read().split())
    
    compList2 = []
    for file in circuit_files2:
        # print("File name: " +str(file))
        with open("circuits/circuit_"+str(file)+".dat") as f:
            for line in f:
                #  Only start reading if there are two spaces 
                if '  ' in line:
                    for line in f:
                        compList2.append(f.read().split())
    # print(compList1)
    # print("-------------------------------------")
    # print(compList2)

    compTup1 = [tuple(x) for x in compList1]
    compTup2 = [tuple(x) for x in compList2]
    compSet1 = set(compTup1)
    compSet2 = set(compTup2)
    commonSet = compSet1.intersection(compSet2)
    commonComps = list(commonSet)
    return sorted(commonComps)

# Takes in a set of component IDs
# Returns a {string: int}
# key = component ID
# value = total number of times that component 
# has been used in all projects
def getComponentReport(componentIDs):
    report = {}
    circuitFile = []
    for comp in componentIDs:
        for file in os.listdir("circuits/"):
            with open("circuits/"+str(file)) as f:
                # Get all the files where component id is present
                for line in f:
                    if comp in line:
                        circuit_name = file[8:15]
                        circuitFile.append(circuit_name)
    # find the files from the component ID
    # now go to to projects.dat to find the number of occurences of these circuits
    projFilePath = "maps/projects.dat"
    count = 0
    countList = []
    for comp in circuitFile:
        with open(projFilePath) as f:
            lines_after_2 = f.readlines()[2:]
            for lines in lines_after_2:
                mod_line = lines.lstrip().split()[0]
                if mod_line == comp:
                    # print(mod_line)
                    countList.append(mod_line)

    for item in countList:
        if item in report:
            report[item] += 1
        else:
            report[item] = 1

    # print(circuitFile)
    return report

# Takes in a set of student names
# returns a set of all circuit IDs each student worked on
def getCircuitByStudent(studentNames):
    studentDict = {}
    studentFilePath = "maps/students.dat"
    # for studentName in studentNames:
    with open(studentFilePath) as f:
        lines_after_2 = f.readlines()[2:]
        for line in lines_after_2:
            key, value = line.strip().split('|')
            studentDict[key] = value

# Removes excess spaces
    studentDict = {x.replace(" ", ""):v.replace(" ", "") for x, v in studentDict.items()}
    studentDict = {x.replace(",", ", "):v for x, v in studentDict.items()}
    # print(studentDict)
    # print("---------------------")
    # print("ITEMS-----------------")
    # print(studentDict.get("Adams, Keith"))
    # print("KEYS------------------")
    # print(studentDict.keys())
    # print("---------------------------------")
    # if studentName not in studentDict:
    #     raise ValueError("Student name does not exist.")
    # First, get the student ID from the student name
    studentList = []
    for students in studentNames:
        student_id = studentDict.get(students)
        studentList.append(student_id)
    print(studentList)
    # print(studentList)
    # Loop through circuits directory and go through each file
    # to find the student IDs that exist
    circuitFile = set()
    for student in studentList:
        # print(student)
        for file in os.listdir("./circuits"):
            with open("./circuits/"+str(file)) as f:
            # Get all the files where student id is present
                for line in f:
                    if student in line:
                        
                        circuit_name = file[8:15]
                        # print(circuit_name)
                        circuitFile.add(circuit_name)
    # print(circuitFile)
    return circuitFile
    # Now get all the components from the matched files
   

# Takes in a set of componentIDs
# Returns a set of all the circuit IDs components were used in
def getCircuitByComponent(componentIDs):
    projIDSet = set()
    circuitFile = []
    for comps in componentIDs:
        for file in os.listdir("circuits/"):
            with open("circuits/"+str(file)) as f:
                # Get all the files where component is present
                for line in f:
                    if comps in line:
                        circuit_name = file[8:15]
                        circuitFile.append(circuit_name)

    
    # Now search for these circuit files in the projects.dat file
    projFilePath = "maps/projects.dat"
    circuittoProjID = []
    with open(projFilePath) as f:
        lines_after_2 = f.readlines()[2:]
        for lines in lines_after_2:
            mod_line = lines.lstrip().split()
            circuittoProjID.append(mod_line)
    # print(circuittoProjID)
    for circ in circuitFile:
         for elem in circuittoProjID:
            for name in elem:
               if circ == name:
                   projIDSet.add(elem[0])
    return projIDSet

# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################
if __name__ == "__main__":
    # resistors = getComponentCountByProject("082D6241-40EE-432E-A635-65EA8AA374B6", "R")
    # capicators = getComponentCountByProject("177EBF38-1C20-497B-A2EF-EC1880FEFDF9", "C")
    # inductors = getComponentCountByProject("08EDAB1A-743D-4B62-9446-2F1C5824A756", "I")
    # transistors = getComponentCountByProject("D88C2930-9DA4-431F-8CDB-99A2AA2C7A05", "T")
    # # print(getComponentReport({'LFC-108', 'DCB-178'}))
    # # print(getCircuitByStudent({"Allen, Amanda", "Baker, Craig"}))
    # # # # getComponentCountByProject("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "R")
    # print("Number of resistors: "+str(resistors))
    # print("Number of capacitors: "+str(capicators))
    # print("Number of inductors: "+str(inductors))
    # print("Number of transistors: "+str(transistors))
    # adamsR = getComponentCountByStudent("Adams, Keith", "R")
    # adamsC = getComponentCountByStudent("Adams, Keith", "C")
    # adamsI = getComponentCountByStudent("Adams, Keith", "I")
    # adamsT = getComponentCountByStudent("Adams, Keith", "T")
    # print(adamsR)
    # print(adamsC)
    # print(adamsI)
    # print(adamsT)
    # print(len(getParticipationByStudent("Harris, Anne")))
    # data = getComponentCountByProject("8C71F259-ECA8-4267-A8B3-6CAD6451D4CC", 'R')
    # print("Resistors: "+str(data))
    # data = getComponentCountByProject("177EBF38-1C20-497B-A2EF-EC1880FEFDF9", 'C')
    # print("Capacitors: "+str(data))
    # data = getComponentCountByProject("08EDAB1A-743D-4B62-9446-2F1C5824A756", 'T')
    # print("Transistors: "+str(data))
    # data = getComponentCountByProject("D88C2930-9DA4-431F-8CDB-99A2AA2C7A05", 'I')
    # print("Inductors: "+str(data))

    # part = getParticipationByStudent("Scott, Michael")
    # print(part)

    # testing with 19-8-60 and everything that has this project ID
    # partByProj = getParticipationByProject("082D6241-40EE-432E-A635-65EA8AA374B6")
    # print(partByProj)

    # test = getCostOfProjects()
    # print(test)

    # sampleComps = {'TQJ-016','LVO-651','GQT-421','QTA-356','RAR-965','JLC-943','MLF-617','UNL-746','VLR-746','VYT-743','YVL-845','TDP-854'}
    # print(getProjectByComponent(sampleComps))

    # test = getCommonByProject("082D6241-40EE-432E-A635-65EA8AA374B6", "08EDAB1A-743D-4B62-9446-2F1C5824A756")
    # print(test)


    # sampleComps = {'TAZ-349', 'TAZ-349', 'CUI-043', 'QLS-943' 'ORW-143'}

    # test = getComponentReport(sampleComps)
    # print(test)
    # comm = getCommonByProject("082D6241-40EE-432E-A635-65EA8AA374B6", "90BE0D09-1438-414A-A38B-8309A49C02EF")
    # res = getComponentCountByProject("8C71F259-ECA8-4267-A8B3-6CAD6451D4CC", "R")
    # cap = getComponentCountByProject("8C71F259-ECA8-4267-A8B3-6CAD6451D4CC", "C")
    # tran = getComponentCountByProject("8C71F259-ECA8-4267-A8B3-6CAD6451D4CC", "T")
    # ind = getComponentCountByProject("8C71F259-ECA8-4267-A8B3-6CAD6451D4CC", "I")
    # total1 = res + cap + tran + ind

    # print(total1)

    # res = getComponentCountByProject("90BE0D09-1438-414A-A38B-8309A49C02EF", "R")
    # cap = getComponentCountByProject("90BE0D09-1438-414A-A38B-8309A49C02EF", "C")
    # tran = getComponentCountByProject("90BE0D09-1438-414A-A38B-8309A49C02EF", "T")
    # ind = getComponentCountByProject("90BE0D09-1438-414A-A38B-8309A49C02EF", "I")

    # total2 = res + cap + tran + ind

    # print(total2)

    # print(comm)
    # studentNames = {"Adams, Keith", "Scott, Michael", "Garcia, Martha"}
    # data = getCircuitByStudent({"Allen, Amanda", "Baker, Craig"})
    # print(data)
    # print(getCircuitByStudent(data))

    # sampleComps = {'TAZ-349', 'ZHR-274', 'QLS-943', 'ORW-143'}
    # print(getCircuitByComponent(sampleComps))
    print()

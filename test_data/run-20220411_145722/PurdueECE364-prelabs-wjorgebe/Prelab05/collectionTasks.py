# ######################################################
#   Author :    William Jorge
#   email :     wjorgebe@purdue.edu
#   ID :        ee364b12   
#   Date :      February 12, 2022
# ######################################################

from collections import defaultdict
from multiprocessing.managers import ValueProxy
import os
import string # List of module import statements
import sys
from typing import final
from unicodedata import name # Each one on a line

# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################

def getComponentCountByProject(projectID: string, componentSymbol: string) -> int:
    projects = "maps/projects.dat"
    line_strings = []
    circuits = []

    with open(projects, 'r') as fp:
        for line in fp.readlines():
            if projectID in line:
                line_strings.append(line)
    
    if len(line_strings) == 0:
        raise ValueError("The provided project ID does not exist!")

    for i in range(len(line_strings)):
        circuits.append((line_strings[i].split())[0])
    
    amount = 0
    for i in circuits:
        current_file = "circuits/circuit_" + i + ".dat"
        if componentSymbol == "R":
            resistors = []
            with open("maps/resistors.dat", 'r') as f1:
                for line in f1:
                    resistors.append((line.split())[0])
            del(resistors[0:3])
            with open(current_file, 'r') as f2:
                for line in f2:
                    if (line.strip()) in resistors:
                        amount += 1

        elif componentSymbol == "I":
            inductors = []
            with open("maps/inductors.dat", 'r') as f1:
                for line in f1:
                    inductors.append((line.split())[0])
            del(inductors[0:3])
            with open(current_file, 'r') as f2:
                for line in f2:
                    if (line.strip()) in inductors:
                        amount += 1   

        elif componentSymbol == "C":
            capacitors = []
            with open("maps/capacitors.dat", 'r') as f1:
                for line in f1:
                    capacitors.append((line.split())[0])
            del(capacitors[0:3])
            with open(current_file, 'r') as f2:
                for line in f2:
                    if (line.strip()) in capacitors:
                        amount += 1
        
        elif componentSymbol == "T":
            transistors = []
            with open("maps/transistors.dat", 'r') as f1:
                for line in f1:
                    transistors.append((line.split())[0])
            del(transistors[0:3])
            with open(current_file, 'r') as f2:
                for line in f2:
                    if (line.strip()) in transistors:
                        amount += 1
    return amount

def getComponentCountByStudent(studentName: string, componentSymbol: string) -> int:
    
    with open("maps/students.dat", 'r') as f1:
        idnum = ""
        for line in f1:
            if studentName in line:
                idnum = (line.split())[3]
        
    if len(idnum) == 0:
        raise ValueError("Student does not exist!")

    files = []
    for name_of_file in os.scandir("circuits"):
        if name_of_file.is_file():
            files.append(name_of_file.path)

    amount = 0
    for i in files:
        with open(i, 'r') as file:
            if idnum in [line.strip() for line in file]:
                if componentSymbol == "R":
                    resistors = []
                    with open("maps/resistors.dat", 'r') as f1:
                        for line in f1:
                            resistors.append((line.split())[0])
                    del(resistors[0:3])
                    with open(i, 'r') as f2:
                        for line in f2:
                            if (line.strip()) in resistors:
                                amount += 1

                elif componentSymbol == "I":
                    inductors = []
                    with open("maps/inductors.dat", 'r') as f1:
                        for line in f1:
                            inductors.append((line.split())[0])
                    del(inductors[0:3])
                    with open(i, 'r') as f2:
                        for line in f2:
                            if (line.strip()) in inductors:
                                amount += 1  

                elif componentSymbol == "C":
                    capacitors = []
                    with open("maps/capacitors.dat", 'r') as f1:
                        for line in f1:
                            capacitors.append((line.split())[0])
                    del(capacitors[0:3])
                    with open(i, 'r') as f2:
                        for line in f2:
                            if (line.strip()) in capacitors:
                                amount += 1
                
                elif componentSymbol == "T":
                    transistors = []
                    with open("maps/transistors.dat", 'r') as f1:
                        for line in f1:
                            transistors.append((line.split())[0])
                    del(transistors[0:3])
                    with open(i, 'r') as f2:
                        for line in f2:
                            if (line.strip()) in transistors:
                                amount += 1
    return amount

def getParticipationByStudent(studentName):
    with open("maps/students.dat", 'r') as f1:
        idnum = ""
        for line in f1:
            if studentName in line:
                idnum = (line.split())[3]
        
    if len(idnum) == 0:
        raise ValueError("Student does not exist!")
    
    files = []
    for name_of_file in os.scandir("circuits"):
        if name_of_file.is_file():
            files.append(name_of_file.path)
    
    circuits = []
    for i in files:
       with open(i, 'r') as file:
            if idnum in [line.strip() for line in file]:
                circuits.append(i[17:24])

    project_IDs = []
    for i in circuits:
        with open("maps/projects.dat") as file:
            for line in file:
                if i in line:
                    project_IDs.append((line.split())[1])
    
    return set(project_IDs)

def getParticipationByProject(projectID):

    circuits = []
    with open("maps/projects.dat", "r") as file:
        for line in file:
            if projectID in line:
                circuits.append((line.split())[0])
    
    if len(circuits) == 0:
        raise ValueError("The project ID does not exist!")
    
    participants = []
    for i in circuits:
        curr_file = "circuits/circuit_" + i + ".dat"
        with open(curr_file, 'r') as f1:
            for line in f1:
                if len(line) == 12 and line.strip() != "Components:":
                    participants.append(line.strip())
    
    names = []
    for j in participants:
        with open("maps/students.dat", 'r') as f2:
            for line in f2:
                if j in line:
                    last_name = (line.split())[0]
                    first_name = (line.split())[1]
                    names.append(last_name + " " + first_name)
    
    return set(names)

def getCostOfProjects():
    
    projects = []
    with open("maps/projects.dat", 'r') as file:
        for line in file:
            if "Circuit" not in line and "------------------------------------------------------------" not in line:
                projects.append((line.split())[1])

    filenames = ['maps/capacitors.dat','maps/resistors.dat','maps/transistors.dat','maps/inductors.dat']
    prices = {}
    for i in filenames:
        with open(i, 'r') as fp:
            for line in fp:
                if "Price" not in line and "-----" not in line:
                    prices[(line.split())[0]] = float((((line.split())[1]).split("$"))[1])
    
    unique_projects = list(set(projects))
    project_prices = {}
    for i in unique_projects:
        total_price = 0
        with open("maps/projects.dat", 'r') as f1:
            circuits = []
            for line in f1:
                if i in line:
                    circuits.append((line.split())[0])
            for j in circuits:
                circuit_file = "circuits/circuit_" + j + ".dat"
                with open(circuit_file, 'r') as f2:
                    for line in f2:
                        if line.strip() in prices:
                            total_price += prices[line.strip()]
        rounded_price = round(total_price, 2)
        project_prices[i] = rounded_price

    return project_prices

def getProjectByComponent(componentIDs):
    
    files = []
    for name_of_file in os.scandir("circuits"):
        if name_of_file.is_file():
            files.append(name_of_file.path)
    
    circuits = []
    for i in files:
        with open(i, 'r') as f1:
            for line in f1:
                if line.strip() in componentIDs:
                    circuits.append(i[17:24])
    
    projectIDs = []
    with open("maps/projects.dat", 'r') as f2:
        for line in f2:
            if "Project" not in line and "------------------------------------------------------------" not in line:
                split_line = line.split()
                if split_line[0] in circuits:
                    projectIDs.append(split_line[1])
    
    return set(projectIDs)

def getCommonByProject(projectID1, projectID2):

    circuits1 = []
    circuits2 = []

    with open("maps/projects.dat", 'r') as file:
        for line in file:
            if projectID1 in line:
                circuits1.append((line.split())[0])
            if projectID2 in line:
                circuits2.append((line.split())[0])
    
    if len(circuits1) == 0 or len(circuits2) == 0:
        raise ValueError("One or both of the project IDs does not exist!")

    components1 = []
    components2 = []
    for i in circuits1:
        open_file = "circuits/circuit_" + i + ".dat"
        with open(open_file, 'r') as f1:
            for line in f1:
                if len(line) == 10:
                    components1.append(line.strip())
    for i in circuits2:
        open_file = "circuits/circuit_" + i + ".dat"
        with open(open_file, 'r') as f2:
            for line in f2:
                if len(line) == 10:
                    components2.append(line.strip())
    
    both_components = []
    for i in components1:
        if i in components2:
            both_components.append(i)

    final_list = list(set(both_components))
    final_list.sort()
    return final_list

def getComponentReport(componentIDs):
    final_dict = {}
    
    files = []
    for name_of_file in os.scandir("circuits"):
        if name_of_file.is_file():
            files.append(name_of_file.path)
    
    for i in files:
        with open(i, 'r') as file:
            for line in file:
                if line.strip() in componentIDs:
                    final_dict[line.strip()] = final_dict.setdefault(line.strip(), -1) + 1
    del final_dict['']
    return final_dict

def getCircuitByStudent(studentNames):
    files = []
    for name_of_file in os.scandir("circuits"):
        if name_of_file.is_file():
            files.append(name_of_file.path)

    studentIDs = [] 
    with open("maps/students.dat", 'r') as f1:
        for line in f1:
            if "-------------------------------------------------------" not in line:
                line_split = line.split()
                name = line_split[0] + " " + line_split[1]
                if name in studentNames:
                    studentIDs.append(line_split[3])

    circuits = []
    for i in files:
        with open(i, 'r') as f2:
            for line in f2:
                if line.strip() in studentIDs:
                    circuits.append(i[17:24])

    return set(circuits)

def getCircuitByComponent(componentIDs):
    files = []
    for name_of_file in os.scandir("circuits"):
        if name_of_file.is_file():
            files.append(name_of_file.path)
    
    circuits = []
    for i in files:
        with open(i, 'r') as f1:
            for line in f1:
                if line.strip() in componentIDs:
                    circuits.append(i[17:24])
    
    projectIDs = []
    with open("maps/projects.dat", 'r') as f2:
        for line in f2:
            if "Project" not in line and "------------------------------------------------------------" not in line:
                split_line = line.split()
                if split_line[0] in circuits:
                    projectIDs.append(split_line[0])
    
    return set(projectIDs) 

# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################
if __name__ == "__main__":   
    # Write anything here to test your code.
    print(getComponentCountByProject("082D6241-40EE-432E-A635-65EA8AA374B6", "I"))
    print(getComponentCountByStudent("Clark, Joe", "I"))
    print(getParticipationByStudent("Clark, Joe")) 
    print(getParticipationByProject("082D6241-40EE-432E-A635-65EA8AA374B6"))
    print(getCostOfProjects())
    print(getProjectByComponent({'LOK-793', 'HBR-310'}))
    print(getCommonByProject("90BE0D09-1438-414A-A38B-8309A49C02EF", "83383848-1D69-40D4-A360-817FB22769ED"))
    print(getComponentReport("LOK-793"))
    print(getCircuitByStudent({"Brown, Robert","Edwards, Rachel"}))
    print(getCircuitByComponent("LOK-793"))
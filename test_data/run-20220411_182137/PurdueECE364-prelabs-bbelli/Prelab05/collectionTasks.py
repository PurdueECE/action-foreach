# ######################################################
# Author : < Your Full Name >
# email : < Your Email >
# ID : < Your course ID , e . g . ee364j20 >
# Date : < Start Date >
# ######################################################


import os # List of module import statements
import sys # Each one on a line
import re
from helper import *


# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################


def getComponentCountByProject(projectID, componentSymbol):
    
    projectCircuits = []

    with open('maps/projects.dat') as f:
        lines = f.readlines()

        for line in lines:
            if projectID in line:
                projectCircuits.append(line[4:11])
    if (projectCircuits == []):
        print("Project ID could not be linked with any circuits!")
        return ValueError

    if(componentSymbol == 'R'):
        components = getAllResistors()
    elif (componentSymbol == 'I'):
        components = getAllInductors()
    elif (componentSymbol == 'C'):
        components = getAllCapacitors()
    elif (componentSymbol == 'T'):
        components = getAllTransistors()

    # print(components)
    
    count = 0
    # print(str(len((projectCircuits))))
    for circuit in projectCircuits:
        # print('circuits/circuit_' + circuit + '.dat')
        with open('circuits/circuit_' + circuit + '.dat') as f:
            lines = f.readlines()
            for line in lines:
                # print(line)
                # if (comp for comp in components if(comp in line)):
                #     count = count + 1
                for comp in components:
                    if comp in line:
                        count = count + 1
    return count



def getComponentCountByStudent(studentName, componentSymbol):
    
    studentID = ""
    count = 0
    with open('maps/students.dat') as f:
        lines = f.readlines()
        for line in lines:
            if studentName in line:
                studentID = (line[44:55])
    
    if (studentID == ""):
        print("Student ID could not be found!")
        return ValueError        

    
    if(componentSymbol == 'R'):
        components = getAllResistors()
    elif (componentSymbol == 'I'):
        components = getAllInductors()
    elif (componentSymbol == 'C'):
        components = getAllCapacitors()
    elif (componentSymbol == 'T'):
        components = getAllTransistors()


    for file in os.listdir('circuits/'):
        with open(os.path.join("circuits/", file), 'r') as f:
            lines = f.readlines()
            if(isParticipant(studentID, f.name)):
                for line in lines:
                    for comp in components:
                        if comp in line:
                            count = count + 1              
            else:
                lines = ""
                continue
    return count

def getParticipationByStudent(studentName):

    studentProjects = set()
    studentID = ""
    count = 0
    circuits = []
    with open('maps/students.dat') as f:
        lines = f.readlines()
        for line in lines:
            if studentName in line:
                studentID = (line[44:55])
    
    if (studentID == ""):
        print("Student ID could not be found!")
        return ValueError   

    for file in os.listdir('circuits/'):
        with open(os.path.join("circuits/", file), 'r') as f:
            lines = f.readlines()
            if(isParticipant(studentID, f.name)):
                circuits.append(f.name[17:24])
            else:
                lines = ""
                continue
    
    with open('maps/projects.dat') as f:
        lines = f.readlines()
        for line in lines:
            for circ in circuits:
                if (circ in line):
                    studentProjects.add(line[21:57])
    return studentProjects

def getParticipationByProject(projectID):
    
    names = set()
    projectCircuits = []
    isDone = False
    participantsID = []

    with open('maps/projects.dat') as f:
        lines = f.readlines()

        for line in lines:
            if projectID in line:
                projectCircuits.append(line[4:11])
    if (projectCircuits == []):
        print("Project ID could not be linked with any circuits!")
        return ValueError

    for circuit in projectCircuits:
        # print('circuits/circuit_' + circuit + '.dat')
        with open('circuits/circuit_' + circuit + '.dat') as f:
            lines = f.readlines()[2:]
            for line in lines:
                if(line == "\n"):
                    break
                else:
                    participantsID.append(line[0:11])

    for id in participantsID:
        names.add(getStudentNameByID(id))
    return names

def getCostOfProjects():
    projectCosts = {}
    projects =  getProjects()
    cost = 0
    for project in projects:
        circuits = getCircuitsByProjectID(project)
        for circuit in circuits:
            cost = cost + getCostOfCircuit(circuit)
        cost = "{:.2f}".format(cost)
        projectCosts.update({project : cost})  
        cost = 0  

    return projectCosts

def getProjectByComponent(componentIDs):
    circuits = set()
    projectIDs = set()
    for component in componentIDs:
        circuits = set.union(circuits, getCircuitsByComponentID(component))
    
    with open('maps/projects.dat') as f:
        lines = f.readlines()
        for line in lines:
            for circuit in circuits:
                if(circuit in line):
                    projectIDs.add(line[21:57])
    return projectIDs

def getCommonByProject(projectID1, projectID2):
    cs1 = getCircuitsByProjectID(projectID1)
    cs2 = getCircuitsByProjectID(projectID2)

    comps1 = set()
    comps2 = set()
    for c1 in cs1:
        compc1 = getComponentsOfCircuit(c1)
        comps1 = set.union(comps1, compc1)

    for c2 in cs2:
        compc2 = getComponentsOfCircuit(c2)
        comps2 = set.union(comps2, compc2)    

    common = set.intersection(comps1, comps2)
    return sorted(common)

def getCircuitByStudent(studentNames):

    studentCircuits = set()
    studentIDs = set()

    with open('maps/students.dat') as f:
        lines = f.readlines()
        for line in lines:
            for studentName in studentNames:
                if studentName in line:
                    studentIDs.add(line[44:55])
    
    if (studentIDs == ""):
        print("Student ID could not be found!")
        return ValueError   

    for file in os.listdir('circuits/'):
        with open(os.path.join("circuits/", file), 'r') as f:
            lines = f.readlines()
            for studentID in studentIDs:
                if(isParticipant(studentID, f.name)):
                    studentCircuits.add(f.name[17:24])
                else:
                    lines = ""
                    continue

    return studentCircuits

def getCircuitByComponent(componentIDs):
    circuits = set()
    for component in componentIDs:
        componentsCircuits = getCircuitsByComponentID(component)
        circuits = set.union(circuits, componentsCircuits)
    return circuits

# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################
if __name__ == '__main__':
# Write anything here to test your code .
    ex_project = '90BE0D09-1438-414A-A38B-8309A49C02EF'
    ex_project2 = 'FE647EE2-2EBD-4837-83F0-256C377365FE'
    ex_symbol = 'R'
    ex_name = 'Edwards, Rachel'
    ex_componentIds = {'PWR-658', 'QIC-567', 'CTI-951'}
    ex_studentNames = {'Campbell, Eugene', 'Butler, Julia', 'Clark, Joe'}
    # ----
    print(getComponentCountByProject(ex_project, ex_symbol))
    # print(getComponentCountByStudent(ex_name, ex_symbol))
    # print(getParticipationByStudent(ex_name))
    # print(getParticipationByProject(ex_project)) 
    # print(getCostOfProjects())
    # print(getProjectByComponent(ex_componentIds))
    print(getCircuitByStudent(ex_studentNames))
    print(getCircuitByComponent(ex_componentIds))
    print(getCommonByProject(ex_project, ex_project2))
    # ----
    a = getComponentPriceDict()
    # print(a)
    # print(getProjects())
    # print(getCircuitsByProjectID('90BE0D09-1438-414A-A38B-8309A49C02EF'))
    # print(getCostOfCircuit('51-9-16'))
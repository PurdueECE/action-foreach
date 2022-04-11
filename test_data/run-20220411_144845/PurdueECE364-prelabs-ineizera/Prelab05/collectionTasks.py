#! /opt/python3/3.8/bin/python3.8
# ######################################################
# Author : Insherah Neizer-Ashun
# email : ineizera@purdue.edu   
# ID : ee364a02
# Date : 02/13/22
# ######################################################
import os # List of module import statements
import sys
# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################

def projectHelper():
    file = open("maps/projects.dat", "r")
    lines = file.readlines()[2:]

    data = []

    for line in lines:
        data.append(line.split())
    
    return data

def circuitHelper(circuitID):
    file = open("circuits/circuit_" + circuitID + ".dat")
    lines = file.readlines()[2:]

    data = []
    components = []
    participants = []

    for line in lines:
        data.append(line.split())

    for i in [["Components:"], ["-------------"], []]:
        data.remove(i)

    for i in data:
        if len(i[0]) == 11:
            participants.append(i[0])
        elif len(i[0]) == 7:
            components.append(i[0])
        else:
            raise ValueError("Incorrect Data.")
    
    return participants, components

def componentHelper(compType):
    map = {"R": "resistors", "I": "inductors", "C": "capacitors", "T": "transistors"}

    file = open("maps/" + map[compType] + ".dat")
    lines = file.readlines()[3:]

    data = []
    dict = {}

    for line in lines:
        data.append(line.split())

    for i in data:
        dict[i[0]] = float(i[1][1:])
    
    return dict

def studentHelper():
    file = open("maps/students.dat")
    lines = file.readlines()[2:]
    
    data = {}

    for line in lines:
        line = line.split()
        if len(line) != 4:
            raise ValueError("Incorrect Data.")
        data[line[0] + " " + line[1]] = line[3]

    return data

def getComponentCountByProject(projectID, componentSymbol):
    proj = projectHelper()
    comp = componentHelper(componentSymbol)
    flag = 0

    cids = []

    for i in proj:
        if projectID == i[1]:
            flag = 1
            cids.append(i[0])            

    if flag == 0:
        raise ValueError("Project ID does not exist.")

    numComps = []

    for i in set(cids):
        _, components = circuitHelper(i)
        for j in components:
            if j in comp:
                numComps.append(j)

    return len(set(numComps))
    
def getComponentCountByStudent(studentName, componentSymbol) :
    stud = studentHelper()
    comp = componentHelper(componentSymbol)

    if studentName not in stud:
        raise ValueError("Student does not exist.")

    numComps = []

    proj = projectHelper()
    circs = []
    for i in proj:
        for j in i:
            if len(j) == 7:
                if j not in circs:
                    circs.append(j)
    circs = sorted(circs)

    for i in circs:
        participants, components = circuitHelper(i)
        if stud[studentName] in participants:
            for j in components:
                if j in comp:
                    numComps.append(j)

    return set(numComps)


def getParticipationByStudent(studentName):
    proj = projectHelper()
    stud = studentHelper()

    if studentName not in stud:
        raise ValueError("Student does not exist.")

    cids = []

    proj = projectHelper()
    circs = []
    for i in proj:
        for j in i:
            if len(j) == 7:
                if j not in circs:
                    circs.append(j)
    circs = sorted(circs)

    for i in circs:
        participants, _ = circuitHelper(i)
        if stud[studentName] in participants:
            cids.append(i)

    pids = []

    for i in proj:
        if i[0] in set(cids):
            pids.append(i[1])
            
    return set(pids)

def getParticipationByProject(projectID):
    proj = projectHelper()
    stud = studentHelper()
    flag = 0

    part = []
    names = []

    for i in proj:
        if i[1] == projectID:
            flag = 1
            participants, _ = circuitHelper(i[0])
            for j in participants:
                part.append(j)

    if flag == 0:
        raise ValueError("Project ID does not exist.")

    for i in set(part):
        for j in stud:
            if i == stud[j]:
                names.append(j)
            
    return set(names)

def getCostOfProjects():
    proj = projectHelper()

    comps = {}

    for i in [componentHelper("R"), componentHelper("I"), componentHelper("C"), componentHelper("T")]:
        comps.update(i)

    cost = {}

    for i in proj:
        cost[i[1]] = 0

    for i in proj:
        _, components = circuitHelper(i[0])
        for j in components:
            cost[i[1]] = float(format(comps[j] + cost[i[1]], ".2f"))

    return cost

def getProjectByComponent(componentIDs):
    proj = projectHelper()

    cids = getCircuitByComponent(componentIDs)

    projects = []

    for i in proj:
        if i[0] in cids:
            projects.append(i[1])
    return set(projects)

def getCommonByProject(projectID1, projectID2):
    proj = projectHelper()
    flag1 = 0
    flag2 = 0
    project1 = []
    project2 = []

    for i in proj:
        if i[1] == projectID1:
            flag1 = 1
            _, components = circuitHelper(i[0])
            for j in components:
                project1.append(j)
        elif i[1] == projectID2:
            flag2 = 1
            _, components = circuitHelper(i[0])
            for j in components:
                project2.append(j)

    if flag1 == 0:
        raise ValueError("1st Project ID does not exist.")
    elif flag2 == 0:
        raise ValueError("2nd Project ID does not exist.")
    
    comps = []

    for i in set(project1) and set(project2):
        comps.append(i)

    return sorted(comps)

def getComponentReport(componentIDs):
    proj = projectHelper()
    dict = {}

    for i in componentIDs:
        dict[i] = 0

    for i in proj:
        _, components = circuitHelper(i[0])
        for j in components:
            if j in componentIDs:
                dict[j] += 1

    return dict

def getCircuitByStudent(studentNames):
    stud = studentHelper()

    sids = []

    for i in studentNames:
        sids.append(stud[i])

    cids = []

    proj = projectHelper()
    circs = []
    for i in proj:
        for j in i:
            if len(j) == 7:
                if j not in circs:
                    circs.append(j)
    circs = sorted(circs)

    for i in circs:
        participants, _ = circuitHelper(i)
        for j in sids:
            if j in participants:
                cids.append(i)

    return set(cids)

def getCircuitByComponent(componentIDs):
    cids = []

    proj = projectHelper()
    circs = []
    for i in proj:
        for j in i:
            if len(j) == 7:
                if j not in circs:
                    circs.append(j)
    circs = sorted(circs)

    for i in circs:
        _, components = circuitHelper(i)
        for j in componentIDs:
            if j in components:
                cids.append(i)

    return set(cids)

# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################
if __name__ == "__main__":
    # Write anything here to test your code.
    t1 = projectHelper(); print(t1)
    t2 = circuitHelper("15-5-65"); print(t2)
    t3 = componentHelper("R"); print(t3)
    t4 = studentHelper(); print(t4)
    test1 = getComponentCountByProject("082D6241-40EE-432E-A635-65EA8AA374B6", "R"); print(test1)
    test2 = getComponentCountByStudent("Adams, Keith", "R"); print(test2)
    test3 = getParticipationByStudent("Adams, Keith"); print(test3)
    test4 = getParticipationByProject("082D6241-40EE-432E-A635-65EA8AA374B6"); print(test4)
    test5 = getCostOfProjects(); print(test5)
    test6 = getProjectByComponent(set(["CLQ-971", "BLL-583", "RNW-027", "BKT-189"])); print(test6)
    test7 = getCommonByProject("082D6241-40EE-432E-A635-65EA8AA374B6", "90BE0D09-1438-414A-A38B-8309A49C02EF"); print(test7)
    test8 = getComponentReport(set(["CLQ-971", "BLL-583", "RNW-027", "BKT-189"])); print(test8)
    test9 = getCircuitByStudent(set(["Adams, Keith", "Bailey, Catherine", "Campbell, Eugene"])); print(test9)
    test10 = getCircuitByComponent(set(["CLQ-971", "BLL-583", "RNW-027", "BKT-189"])); print(test10)
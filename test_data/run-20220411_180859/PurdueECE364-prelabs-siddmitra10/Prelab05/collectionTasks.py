#######################################################
# Author:
# email:
# ID:
# Date: 
# #######################################################
# import os  # List of module import statements 
# import sys # Each one on a line
from pprint import pprint as pp
import re
import os
####################################################### 
# # No Module -Level Variables or Statements!
# ONLY FUNCTIONS BEYOND THIS POINT! 
# #######################################################
################################################################################
################################################################################
################################################################################
def getProjectDict(projectID):
    projects = dict()
    invalidFlag = True
    with open("./maps/projects.dat", 'r') as projectFile:
        for line in projectFile.readlines()[2:]:
            data = line.split()
            if data[1] in projects.keys():
                projects[data[1]].append(data[0])    
            else:
                if projectID == data[1]: invalidFlag = False
                projects[data[1]] = [data[0]]
    if invalidFlag: raise ValueError("Provided ProjectID is invalid")
    return projects

def getComponentDict(componentSymbol):

    if(componentSymbol == 'R'): component = "resistors"
    elif(componentSymbol == 'C'): component = "capacitors"
    elif(componentSymbol == 'I'): component = "inductors"
    elif(componentSymbol == 'T'): component = "transistors"
    else: raise ValueError("Provided Component Symbol is invalid")

    components = dict()
    with open(f"./maps/{component}.dat", 'r') as componentFile:
        for line in componentFile.readlines()[3:]:
            data = line.split()
            components[data[0]] = data[1]
    return components

def getStudentID(studentName):
    invalid = True
    with open("./maps/students.dat") as studentsFile:
        for studentInfo in studentsFile:
            if studentName in studentInfo:
                invalid = False
                break;
    if invalid: raise ValueError("Given student name does not exist")
    pattern = r'\d+-\d+'
    studentID = re.search(pattern, studentInfo).group(0)
    return studentID

def makeProjectsDict():
    projects = dict()
    with open("./maps/projects.dat", 'r') as projectFile:
        for line in projectFile.readlines()[2:]:
            data = line.split()
            if data[1] in projects.keys():
                projects[data[1]].append(data[0])    
            else:
                projects[data[1]] = [data[0]]
    return projects

def makeAllComponentList():
    components = dict()
    for component in ["resistors", "capacitors", "transistors", "inductors"]:
        with open(f"./maps/{component}.dat", 'r') as componentFile:
            for line in componentFile.readlines()[3:]:
                data = line.split()
                components[data[0]] = data[1]
    return components
################################################################################
################################################################################
################################################################################
def getComponentCountByProject(projectID, componentSymbol):
    # projects = dict()
    # invalidFlag = True
    # with open("./maps/projects.dat", 'r') as projectFile:
    #     for line in projectFile.readlines()[2:]:
    #         data = line.split()
    #         if data[1] in projects.keys():
    #             projects[data[1]].append(data[0])    
    #         else:
    #             if projectID == data[1]: invalidFlag = False
    #             projects[data[1]] = [data[0]]
                
    projects = getProjectDict(projectID)

    # if invalidFlag: raise ValueError("Provided ProjectID is invalid")

    # if(componentSymbol == 'R'): component = "resistors"
    # elif(componentSymbol == 'C'): component = "capacitors"
    # elif(componentSymbol == 'I'): component = "inductors"
    # elif(componentSymbol == 'T'): component = "transistors"
    # else: raise ValueError("Provided Component Symbol is invalid")

    # components = dict()
    # with open(f"./maps/{component}.dat", 'r') as componentFile:
    #     for line in componentFile.readlines()[3:]:
    #         data = line.split()
    #         components[data[0]] = data[1]

    components = getComponentDict(componentSymbol)
    
    pattern = r'([A-Z]+-\d+)'
    count = 0
    for circuit in projects[projectID]:
        with open(f"./circuits/circuit_{circuit}.dat", 'r') as circuitFile:
            data = circuitFile.read()
            matches = re.findall(pattern, data)
            for match in matches:
                if match in components.keys(): 
                    count += 1
                    del components[match]
    # print(len(components))
    return count

def getComponentCountByStudent(studentName, componentSymbol):
    # invalid = True
    # with open("./maps/students.dat") as studentsFile:
    #     for studentInfo in studentsFile:
    #         if studentName in studentInfo:
    #             invalid = False
    #             break;

    # if invalid: raise ValueError("Given student name does not exist")

    # pattern = r'\d+-\d+'
    # studentID = re.search(pattern, studentInfo).group(0)
    studentID = getStudentID(studentName)
    components = getComponentDict(componentSymbol)
    
    pattern = r'([A-Z]+-\d+)'
    circuits = os.listdir("./circuits/")
    count = 0
    for circuit in circuits:
        with open(f"./circuits/{circuit}", 'r') as circuitFile:
            data = circuitFile.read()
            if studentID in data:
                matches = re.findall(pattern, data)
                for match in matches:
                    if match in components.keys(): 
                        count += 1
                        del components[match]
                
    return count

def getParticipationByStudent(studentName):
    studentID = getStudentID(studentName)
    circuits = os.listdir("./circuits/")
    pattern = r'\d+-\d+-\d+'
    circuitIDs = []
    for circuit in circuits:
        with open(f"./circuits/{circuit}", 'r') as circuitFile:
            data = circuitFile.read()
            if studentID in data:
                circuitID = re.search(pattern, circuit).group(0)
                circuitIDs.append(circuitID)
    projectSet = set()
    projectPattern = r'\w+-\w+-\w+-\w+-\w+'
    with open("./maps/projects.dat", 'r') as projectFile:
        for line in projectFile.readlines()[2:]:
            circuitID = re.search(pattern, line).group(0)
            if circuitID in circuitIDs:
                projectID = re.search(projectPattern, line).group(0)
                projectSet.add(projectID)

    return projectSet

def getParticipationByProject(projectID):
    projects = getProjectDict(projectID)
    ciruits = projects[projectID]
    pattern = r'\d+-\d+'
    studentSet = set()
    for circuit in ciruits:
        with open(f"./circuits/circuit_{circuit}.dat", 'r') as circuitFile:
            data = circuitFile.read()
            students = re.findall(pattern, data)
            for student in students:
                studentSet.add(student)
    
    studentNameSet = set()
    pattern = r'[A-Za-z]+,\s[A-Za-z]+'
    with open("./maps/students.dat", 'r') as studentsFile:
        for line in studentsFile.readlines()[2:]:
            for studentID in studentSet:
                if studentID in line:
                    studentName = re.search(pattern, line).group(0)
                    studentNameSet.add(studentName)

    return studentNameSet

def getCostOfProjects():
    projects = dict()
    with open("./maps/projects.dat", 'r') as projectFile:
        for line in projectFile.readlines()[2:]:
            data = line.split()
            if data[1] in projects.keys():
                projects[data[1]].append(data[0])    
            else:
                projects[data[1]] = [data[0]]

    components = dict()
    for component in ["resistors", "capacitors", "transistors", "inductors"]:
        with open(f"./maps/{component}.dat", 'r') as componentFile:
            for line in componentFile.readlines()[3:]:
                data = line.split()
                components[data[0]] = data[1]

    pattern = r'[A-Z]+-\d+'
    for project, circuits in projects.items():
        cost = float(0)
        # cost = []
        for circuit in circuits:
            with open(f"./circuits/circuit_{circuit}.dat", 'r') as circuitFile:
                data = circuitFile.read()
                componentList = re.findall(pattern, data)
                for component in componentList:
                    temp = float(components[component][1:])
                    cost += temp
                    # cost.append(temp)
                    # print(temp)
                    # cost += float(components[component][1:])
        projects[project] = round(cost, 2)
        # projects[project] = cost
    return projects

def getProjectByComponent(componentIDs):
    circuitSet = set()
    pattern = r'([A-Z]+-\d+)'
    circuitPattern = r'\d+-\d+-\d+'
    circuits = os.listdir("./circuits/")
    for circuit in circuits:
        with open(f"./circuits/{circuit}", 'r') as circuitFile:
            data = circuitFile.read()
            matches = re.findall(pattern, data)
            for match in matches:
                if match in componentIDs:
                    circuitSet.add(re.search(circuitPattern, circuit).group(0))
 
    # with open("./maps/projects.dat", 'r') as projectFile:
    projects = makeProjectsDict()
    # for project, circuits in projects.items():
    projectsSet = set()
    for circuit in circuitSet:
        for project, ids in projects.items():
            if circuit in ids: projectsSet.add(project)
    return projectsSet

def getCommonByProject(projectID1, projectID2):
    projects = makeProjectsDict()
    if projectID1 not in projects.keys() or projectID2 not in projects.keys():
        raise ValueError("Incorrect projectID provided")
    
    project1Components = []
    size1 = 0
    components = makeAllComponentList()
    pattern = r'([A-Z]+-\d+)'
    for circuit in projects[projectID1]:
        with open(f"./circuits/circuit_{circuit}.dat", 'r') as circuitFile:
            data = circuitFile.read()
            matches = re.findall(pattern, data)
            for match in matches:
                if match in components.keys(): 
                    project1Components.append(match)
                    size1 += 1
                    del components[match]
    
    project2Components = []
    size2 = 0
    components = makeAllComponentList()
    pattern = r'([A-Z]+-\d+)'
    for circuit in projects[projectID2]:
        with open(f"./circuits/circuit_{circuit}.dat", 'r') as circuitFile:
            data = circuitFile.read()
            matches = re.findall(pattern, data)
            for match in matches:
                if match in components.keys(): 
                    project2Components.append(match)
                    size2 += 1
                    del components[match]
    # print(size1, size2)
    # print(project1Components)
    # print(project2Components)
    # pp(projects[projectID1])
    # pp(projects[projectID2])
    if size1 < size2:
        return sorted([component for component in project1Components if component in project2Components])
    else:
        return sorted([component for component in project2Components if component in project1Components])

def getComponentReport(componentIDs):
    projects = makeProjectsDict()
    pattern = r'([A-Z]+-\d+)'
    componentDict = {componentID: int(0) for componentID in componentIDs}
    for circuits in projects.values():
        for circuit in circuits:
            with open(f"./circuits/circuit_{circuit}.dat", 'r') as circuitFile:
                data = circuitFile.read()
                matches = re.findall(pattern, data)
                for match in matches:
                    if match in componentIDs:
                        componentDict[match] += 1
    return componentDict

def getCircuitByStudent(studentNames):
    circuitIDs = set()
    studentIDs = []
    for name in studentNames:
        studentIDs.append(getStudentID(name))
    circuits = os.listdir("./circuits/")
    pattern = r'\d+-\d+'
    circuitPattern = r'\d+-\d+-\d+'
    for circuit in circuits:
        with open(f"./circuits/{circuit}", 'r') as circuitFile:
            data = circuitFile.read()
            matches = re.findall(pattern, data)
            for match in matches:
                if match in studentIDs: 
                    circuitIDs.add(re.search(circuitPattern, circuit).group(0))
    return circuitIDs

def getCircuitByComponent(componentIDs):
    circuits = os.listdir("./circuits/")
    pattern = r'([A-Z]+-\d+)'
    circuitPattern = r'\d+-\d+-\d+'
    circuitIDs = set()
    for circuit in circuits:
        with open(f"./circuits/{circuit}", 'r') as circuitFile:
            data = circuitFile.read()
            matches = re.findall(pattern, data)
            for match in matches:
                    if match in componentIDs:
                        circuitIDs.add(re.search(circuitPattern, circuit).group(0))

    return circuitIDs

##################################################################
# This block is optional and can be used for testing.
# We will NOT look into its content. 
# ####################################################### 

if __name__ == "__main__":

# 1
    # data = getComponentCountByProject("8C71F259-ECA8-4267-A8B3-6CAD6451D4CC", 'R')
    # pp(data)
    # data = getComponentCountByProject("177EBF38-1C20-497B-A2EF-EC1880FEFDF9", 'C')
    # pp(data)
    # data = getComponentCountByProject("08EDAB1A-743D-4B62-9446-2F1C5824A756", 'T')
    # pp(data)
    # data = getComponentCountByProject("D88C2930-9DA4-431F-8CDB-99A2AA2C7A05", 'I')
    # pp(data)

# 2 
    # data = getComponentCountByStudent("Adams, Keith", 'R')
    # pp(data)

# 3
    # data = getParticipationByStudent("Turner, Theresa")
    # pp(data)

# 4
    # data = getParticipationByProject("082D6241-40EE-432E-A635-65EA8AA374B6")
    # pp(data)

# 5
    # data = getCostOfProjects()
    # pp(data)

# 6
    # data = gtProjectByComponent({'LFC-108', 'DCB-178'})
    # pp(data)
    # pp(len(data))

# 7
    data = getCommonByProject("082D6241-40EE-432E-A635-65EA8AA374B6", "90BE0D09-1438-414A-A38B-8309A49C02EF")
    pp(data)
    print(len(data))

# 8
    # data = getComponentReport({'LFC-108', 'DCB-178'})
    # pp(data)

# 9
    # data = getCircuitByStudent({"Allen, Amanda", "Baker, Craig"})
    # pp(data)

# 10
    # data = getCircuitByComponent({'LFC-108', 'DCB-178'})
    # pp(data)
#######################################################
# Author : Aedan Frazier>
# email : frazie35@purdue.edu
# ID : ee364a06
# Date : 2/8/2022
#######################################################
import os # List of module import statements
import sys # Each one on a line
#######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
#######################################################
def getComponentCountByProject ( projectID : str , componentSymbol : str ) -> int :
    FILE = open("maps/projects.dat", "r")
    circuits = list()
    
    for line in FILE:
        circuit=line[4:20].strip()
        project=line[21:70].strip()
        #print("{} | {}".format(circuit, project))
        if(projectID == project):
            circuits.append(circuit)
    FILE.close()

    if(len(circuits) == 0):
        raise ValueError("Project under project ID \"{}\" does not exist".format(projectID))

    components = []
    for c in circuits:
        FILE = open("circuits/circuit_{}.dat".format(c), "r")
        for line in FILE:
            if len(line.strip()) == 7:
                components.append(line.strip())
                
    if(componentSymbol=="R"):
        FILE = open("maps/resistors.dat", "r")
    elif(componentSymbol=="I"):
        FILE = open("maps/inductors.dat", "r")
    elif(componentSymbol=="C"):
        FILE = open("maps/capacitors.dat", "r")
    elif(componentSymbol=="T"):
        FILE = open("maps/transistors.dat", "r")
    else:
        raise ValueError('componentSymbol Not Recognized\nNeeds to be one of the following, "R", "I", "C", "T"')

    componentlist = FILE.read()
    FILE.close()
    amount = 0
    
    for component in components:
        #print("Component: {}, In List: {}".format(component, component in componentlist))
        if component in componentlist:
            amount = amount + 1
        
    return amount  

def getComponentCountByStudent( studentName : str , componentSymbol : str) -> int : 
    FILE = open("maps/students.dat", "r")
    stuID = "INIT"

    for line in FILE:
        if studentName in line:
            stuID = line[44:55] 

    FILE.close()
    
    if(stuID == "INIT"):
        raise ValueError("Student with the name {} does not exist".format(studentName))


    circuitlist = os.listdir("circuits/")
    studentcircuits = list()

    for file in circuitlist:
        FILE = open("circuits/{}".format(file), "r")
        dump = FILE.read()
        FILE.close()
        if(stuID in dump):
            studentcircuits.append(file)

    megacomponentlist = list()
    for file in studentcircuits:
        FILE = open("circuits/{}".format(file), "r")
        for line in FILE:
            stript = line.strip()
            if(len(stript) == 7):
                megacomponentlist.append(stript)   
        FILE.close()
    
    
    componentlist = list()
    for component in megacomponentlist:
        if(component in componentlist):
            pass
        else:
            componentlist.append(component)
    
    if(componentSymbol=="R"):
        FILE = open("maps/resistors.dat", "r")
    elif(componentSymbol=="I"):
        FILE = open("maps/inductors.dat", "r")
    elif(componentSymbol=="C"):
        FILE = open("maps/capacitors.dat", "r")
    elif(componentSymbol=="T"):
        FILE = open("maps/transistors.dat", "r")
    else:
        raise ValueError('componentSymbol Not Recognized\nNeeds to be one of the following, "R", "I", "C", "T"')

    ls = FILE.read()
    FILE.close()
    amount = 0
    for component in componentlist:
        if component in ls:
            amount = amount + 1
        else:
            pass

    return amount

''' (#3)
Write a function called getParticipationByStudent(studentName) that takes in the full
student name and returns a set of the project IDs that the student has participated in. If the student
has not participated in any projects, return an empty set. If the student name passed does not exist,
raise a ValueError with a descriptive message
'''
def getParticipationByStudent(studentName : str) -> set():
    FILE = open("maps/students.dat", "r")
    stuID = "INIT"
    for line in FILE:
        if studentName in line:
            stuID = line[44:55] 
    FILE.close()
    if(stuID == "INIT"):
        raise ValueError("Student with the name {} does not exist".format(studentName))

    circuitlist = os.listdir("circuits/")
    studentcircuits = list()

    for file in circuitlist:
        FILE = open("circuits/{}".format(file), "r")
        dump = FILE.read()
        FILE.close()
        if(stuID in dump):
            studentcircuits.append(file[8:15])

    studentprojects = set()
    FILE = open("maps/projects.dat", "r")
    for line in FILE:
        for circuit in studentcircuits:
            if circuit in line:
                studentprojects.add(line[21:57])
    FILE.close()
    return studentprojects

''' 4. 
[5 pts] Write a function called getParticipationByProject(projectID) that takes in a project ID,
and returns a set of all the full names of the students who have participated in this project. If the
project ID provided does not exists, raise a ValueError with a descriptive message'''
def getParticipationByProject(projectID : str) -> set():
    FILE = open("maps/projects.dat", "r")
    
    circuits = list()
    for line in FILE:
        circuit=line[4:20].strip()
        project=line[21:70].strip()
        #print("{} | {}".format(circuit, project))
        if(projectID == project):
            circuits.append(circuit)
    FILE.close()

    if len(circuits) == 0:
        raise ValueError("Project Doesn't Exist")

    IDlist = list()
    for circuit in circuits:
        FILE = open("circuits/circuit_{}.dat".format(circuit), "r")
        for line in FILE:
            if len(line.strip()) == 11 and (line.strip() != "Components:"):
                IDlist.append(line.strip())
        FILE.close()

    studentlist = set()
    
    FILE = open("maps/students.dat", "r")
    for line in FILE:
        for ID in IDlist:
            if ID in line:
                studentlist.add(line.partition("|")[0].strip())
    FILE.close()

    return studentlist

'''5. 
Write a function called getCostOfProjects() that returns a {string: float} dictionary,
where the key is the project ID, and the value is the total cost of completing that project, rounded to
two decimals.'''
def getCostOfProjects() -> dict():
    
    megaprojectlist = list()
    FILE = open("maps/projects.dat")
    for line in FILE:
        megaprojectlist.append(line.partition("          ")[2])
    FILE.close()

    projectlist = list()
    for project in megaprojectlist:
        if(project.strip() in projectlist):
            pass
        else:
            if(project.strip() == "Project ID" or project.strip() == ""):
                pass
            else:
                projectlist.append(project.strip())

    FILE.close()

    circuitlist = os.listdir("circuits/")
    circuitcomponents = dict()
    for c in circuitlist:
        FILE = open("circuits/{}".format(c), "r")
        circuitcomponents[c[8:15]] = list()
        for line in FILE:
            if len(line.strip()) == 7:
                circuitcomponents[c[8:15]].append(line.strip())
        FILE.close()
    
    circuitprices = dict()
    for circuit in circuitcomponents:
        circuitprices[circuit] = 0
        for component in circuitcomponents[circuit]:
            capacitors = open("maps/capacitors.dat")
            for line in capacitors:
                if component in line:
                    circuitprices[circuit] += float(line.partition("$")[2])
            capacitors.close()
            resistors = open("maps/resistors.dat")
            for line in resistors:
                if component in line:
                    circuitprices[circuit] += float(line.partition("$")[2])
            resistors.close()
            inductors = open("maps/inductors.dat")
            for line in inductors:
                if component in line:
                    circuitprices[circuit] += float(line.partition("$")[2])
            inductors.close()
            transistors = open("maps/transistors.dat")
            for line in transistors:
                if component in line:
                    circuitprices[circuit] += float(line.partition("$")[2])
            transistors.close()
            
    circuitsbyproject = dict()
    FILE = open("maps/projects.dat")
    for project in projectlist:
        FILE = open("maps/projects.dat")
        circuitsbyproject[project] = list()
        for line in FILE:
            if project in line:
                circuitsbyproject[project].append((line.partition("          ")[0].strip()))
        FILE.close()

    pricesbyproject = dict()
    for project in circuitsbyproject:
        pricesbyproject[project] = 0
        for circuit in circuitsbyproject[project]:
            pricesbyproject[project] += circuitprices[circuit]
        pricesbyproject[project] = round(pricesbyproject[project], 2)
    
    return pricesbyproject
    
'''6.
 Write a function called getProjectByComponent(componentIDs) that takes in a set of component IDs, and returns set of the project IDs in which any of components passed has been used.
'''
def getProjectByComponent(componentIDs : set()) -> set():
    FILE = open("maps/projects.dat", "r")
    
    circuitsinprojects = dict()
    
    for line in FILE:
        if(not("Circuit" in line) and line !="------------------------------------------------------------\n"):
            circuit=line[4:20].strip()
            project=line[21:70].strip()
            # print("{} {}".format(project, circuit))
            circuitsinprojects[project] = []
    FILE.close()

    FILE = open("maps/projects.dat", "r")
    for line in FILE:
        if(not("Circuit" in line) and line !="------------------------------------------------------------\n"):
            circuit=line[4:20].strip()
            project=line[21:70].strip()
            # print("{} {}".format(project, circuit))
            circuitsinprojects[project].append(circuit)
    FILE.close()

    componentsinproject = dict()

    for project in circuitsinprojects:
        componentsinproject[project] = list()
        for circuit in circuitsinprojects[project]:
            FILE = open("circuits/circuit_{}.dat".format(circuit), "r")
            for line in FILE:
                stript = line.strip()
                if(len(stript) == 7):
                    componentsinproject[project].append(stript)   
            FILE.close()
    
    projects = set()
    for component in componentIDs:
        for project in componentsinproject:
            if component in componentsinproject[project]:
                projects.add(project)

    return(projects)

'''7.
Write a function called getCommonByProject(projectID1, projectID2) that returns a sorted
list of all the distinct components that have been used in both of the projects passed. If there were
no common components used between these projects, return an empty list, and if either of the project
IDs passed does not exist, raise a ValueError with a descriptive message.
'''
def getCommonByProject(projectID1 : str, projectID2 : str) -> list():
    FILE = open("maps/projects.dat", "r")
    circuits1 = list()
    circuits2 = list()
    for line in FILE:
        circuit=line[4:20].strip()
        project=line[21:70].strip()
        #print("{} | {}".format(circuit, project))
        if(projectID1 == project):
            circuits1.append(circuit)
        elif(projectID2  == project):
            circuits2.append(circuit)
    FILE.close()

    if(len(circuits1) == 0 ):
        raise ValueError("Project 1 Doesn't Exist")
    if(len(circuits2) == 0 ):
        raise ValueError("Project 2 Doesn't Exist")

    components1 = []
    for c in circuits1:
        FILE = open("circuits/circuit_{}.dat".format(c), "r")
        for line in FILE:
            if len(line.strip()) == 7:
                components1.append(line.strip())
        FILE.close()


    components2 = []
    for c in circuits2:
        FILE = open("circuits/circuit_{}.dat".format(c), "r")
        for line in FILE:
            if len(line.strip()) == 7:
                components2.append(line.strip())
        FILE.close()
  
    commonlist = list()

    for component in components1:
        if component in components2:
            commonlist.append(component)

    return commonlist

'''8.
Write a function called getComponentReport(componentIDs) that takes in a set of component
IDs, and returns a {string: int} dictionary, where the key is the component ID, and the value is the
total number of times that component has been used in all projects'''
def getComponentReport(componentIDs : set()) -> dict():
    FILE = open("maps/projects.dat", "r")
    circuitsinprojects = dict()
    
    for line in FILE:
        if(not("Circuit" in line) and line !="------------------------------------------------------------\n"):
            circuit=line[4:20].strip()
            project=line[21:70].strip()
            circuitsinprojects[project] = []
    FILE.close()

    FILE = open("maps/projects.dat", "r")
    for line in FILE:
        if(not("Circuit" in line) and line !="------------------------------------------------------------\n"):
            circuit=line[4:20].strip()
            project=line[21:70].strip()
            # print("{} {}".format(project, circuit))
            circuitsinprojects[project].append(circuit)
    FILE.close()

    componentsinproject = dict()

    for project in circuitsinprojects:
        componentsinproject[project] = list()
        for circuit in circuitsinprojects[project]:
            FILE = open("circuits/circuit_{}.dat".format(circuit), "r")
            for line in FILE:
                stript = line.strip()
                if(len(stript) == 7):
                    componentsinproject[project].append(stript)   
            FILE.close()
    
    componentcount = dict()
    for component in componentIDs:
        componentcount[component] = 0

    for component in componentIDs:
        for project in componentsinproject:
            if component in componentsinproject[project]:
                componentcount[component] += 1
        
    return componentcount

'''9.
Write a function called getCircuitByStudent(studentNames) that takes in a set of student
names, and returns a set of all the circuit IDs that any of students passed has worked on.
'''
def getCircuitByStudent(studentNames : set()) -> set():
    IDS = list()
    for student in studentNames:
        FILE = open("maps/students.dat", "r")
        for line in FILE:
            if student in line:
                IDS.append(line[44:55])
        FILE.close()
    
    #print(IDS)
    circuitlist = os.listdir("circuits/")
    circuitsmatch = set()

    for circuit in circuitlist:
        for ID in IDS:
            FILE = open("circuits/{}".format(circuit), "r")
            if ID in FILE.read():
                circuitsmatch.add(circuit[8:15])
            FILE.close()
    return(circuitsmatch)

'''10.
Write a function called getCircuitByComponent(componentIDs) that takes in a set of component IDs, and returns a set of all the circuit IDs that any of components passed are used in.
'''
def getCircuitByComponent(componentIDs : set()) -> set():
    circuitlist = os.listdir("circuits/")

    circuitset = set()

    for circuit in circuitlist:
        FILE = open("circuits/{}".format(circuit), "r")
        text = FILE.read()
        for component in componentIDs:
            if component in text:
                circuitset.add(circuit[8:15])
        FILE.close()

    return circuitset


# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################
if __name__ == "__main__" :
# Write anything here to test your code .
    print(getComponentCountByProject("082D6241-40EE-432E-A635-65EA8AA374B6","I")) # "082D6241-40EE-432E-A635-65EA8AA374B6"
    print( getComponentCountByStudent("Adams, Keith", "T"))
    print(getParticipationByStudent("Adams, Keith"))
    print(getParticipationByProject("082D6241-40EE-432E-A635-65EA8AA374B6"))
    print(getCostOfProjects())
    getProjectByComponent(("KWR-523", "HQC-193"))
    print(getCommonByProject("8E56417E-0D81-4F43-8137-F1F7AA005654","0F1FABFA-E112-4A66-A0B0-B7A2C14AD39A"))
    print(getComponentReport(set(("RHN-678",))))
    print(getCircuitByStudent(("Price, Dorothy", "Ross, Frances")))
    print(getCircuitByComponent(("KWR-523","LJX-173")))
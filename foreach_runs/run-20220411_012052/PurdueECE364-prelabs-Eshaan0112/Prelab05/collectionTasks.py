# ######################################################
# Author : Eshaan Minocha
# email : eminocha@purdue.edu
# ID : ee364b01
# Date : 2/12/2022
# ######################################################
import os # List of module import statements
import sys # Each one on a line
import re # Regex
from itertools import dropwhile
from decimal import ROUND_HALF_UP, Decimal
# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################

# P1
def getComponentCountByProject(projectID, componentSymbol):
    # get the circuit ids from maps / circuits.dat
    # go to circuits and look for the file with the circuit ids
    # get all component ids
    # check the symbol and go to the file 
    # compare the component ids with the ids in the file and increase count
    

    ''' Getting circuit IDs'''
    file_name = "maps/projects.dat" 
    circ_IDs = []
    #print("In function")
    i = 0 # To skip first two lines of the file
    flag  = 0
    with open (file_name,'r') as data:
            for line in data:
                if i >= 2:
                    #print(f'Line = {line}')
                    col = line.split()
                    #print(f'Col = {col}')
                    if (projectID == col[1]):
                        circ_IDs.append(col[0])
                        flag = 1
                i += 1
    if flag == 0:
        raise ValueError("ProjectID doesn't exist")
    #print(f"circ_IDs = {circ_IDs}")      

    ''' Get all component IDs '''
    component_ids = []
    directory = "circuits"
    for circ_file in os.listdir(directory):
        match = re.findall(r"\d\d-\d-\d\d",circ_file)
        if match[0] in circ_IDs:
            with open (f"circuits/{circ_file}",'r') as data_circ:
                dropped = dropwhile(lambda _line: 'Components:' not in _line, data_circ)
                next(dropped, '')
                for line in dropped:
                    #print(line)
                    if line.startswith("-") :
                        continue
                    else:
                        component_ids.append(line) 
    
    for i in range(len(component_ids)):
        component_ids[i] = (component_ids[i].strip())
    #print(f'component_ids = {component_ids}')        
    '''if componentSymbol == "I":
        componentSymbol = "L"
    check_unique = []
    count = 0
    for ID in component_ids:
        if ID not in check_unique and componentSymbol in ID:
            check_unique.append(ID)
            count += 1
    #print(f'Lenght of component ids = {len(component_ids)}')

    print(f'count_resistors = {count}')
    return count'''


    ''' Check the symbol and go to file'''
    if componentSymbol == "R":
        type_file = "maps/resistors.dat"
    elif componentSymbol == "I":
        type_file = "maps/inductors.dat"
    elif componentSymbol == "C":
        type_file = "maps/capacitor.dat"
    elif componentSymbol == "T":
        type_file = "maps/transistor.dat"
    
    check_unique = []
    i = 0 # To skip 3 lines
    count = 0 # To get unique coun
    with open (f"{type_file}",'r') as data_type:
            for line in data_type:
                if i >= 3:
                    line = line.split()
                    if line[0]not in check_unique and line[0] in component_ids:
                        check_unique.append(line[0])
                        count += 1
                i += 1
    print(f'count = {count}')
    return count 

# P2
def getComponentCountByStudent(studentName, componentSymbol):
    # get student id
    # In all circuit files, if the student id exists, then go 
    # to "Components" and add the component ids having the letter in a list
    # Filter the list to get unique ids 
    # get their length 

    #print(f'stu_name = {studentName}')
    file_name = "maps/students.dat" 
    #print("In function")
    i = 0 # To skip first two lines of the file
    flag  = 0
    with open (file_name,'r') as data:
            for line in data:
                if i >= 2:
                    #print(f'Line = {line}')
                    col = line.split()
                    #print(f'Col = {col}')
                    name = col[0]+ " "+col[1]
                    #print(f'name = {name}')
                    #print(f' col[3] = {col[3]}')
                    if (studentName == name):
                        #print("in")
                        stu_ID = (col[3])
                        flag = 1
                i += 1
    if flag == 0:
        raise ValueError("Student name doesn't exist")
    #print(f"stu_ID = {stu_ID}")   

    file_list = []
    component_IDs =[]
    directory = "circuits"
    for circ_file in os.listdir(directory):
        with open (f"circuits/{circ_file}") as data_circ:
            if stu_ID in data_circ.read():
                file_list.append(circ_file)
    
    #print(f"file = {file_list}")
    for file in file_list:
        file = f"circuits/{file}"
        #print(f'file = {file}')
        with open (f"{file}",'r') as file:
            dropped = dropwhile(lambda _line: 'Components:' not in _line, file)
            #next(dropped, '')
            for line in dropped:
                if line.startswith("-") :
                        continue
                elif componentSymbol in line:
                    component_IDs.append(line)

                    
    
    component_IDs = set(component_IDs)
    count = len(component_IDs)

    #print(component_IDs)
    #print(f'Count of R = {count}')
    return count

# P3
def getParticipationByStudent(studentName):
    # Get student id
    # Get circuit ids
    # iterate through projects to get project ids

    file_name = "maps/students.dat" 
    #print("In function")
    flag = 0
    i = 0 # To skip first two lines of the file
    with open (file_name,'r') as data:
            for line in data:
                if i >= 2:
                    #print(f'Line = {line}')
                    col = line.split()
                    #print(f'Col = {col}')
                    name = col[0]+ " "+col[1]
                    #print(f'name = {name}')
                    #print(f' col[3] = {col[3]}')
                    if (studentName == name):
                        #print("in")
                        stu_ID = (col[3])
                        flag = 1
                i += 1

    if flag == 0:
        raise ValueError("Student name doesn't exist")
    circ_list = []
    directory = "circuits"
    for circ_file in os.listdir(directory):
        with open (f"circuits/{circ_file}") as data_circ:
            if stu_ID in data_circ.read():
                match = re.findall(r"\d\d-\d-\d\d",circ_file)
                circ_list.append(match[0])
    
    new_f = "maps/projects.dat"
    proj_set = set()
    i = 0
    with open (f"{new_f}",'r') as data:
            for line in data:
                if i >= 2:
                    line = line.split()
                    if line[0] in circ_list:
                        proj_set.add(line[1])
                i += 1
    #print(f'proj_set = {proj_set}')
    return proj_set

# P4
def getParticipationByProject(projectID):
    file_name = "maps/projects.dat" 
    circ_IDs = []
    i = 0 # To skip first two lines of the file
    flag  = 0
    with open (file_name,'r') as data:
            for line in data:
                if i >= 2:
                    col = line.split()
                    if (projectID == col[1]):
                        circ_IDs.append(col[0])
                        flag = 1
                i += 1
    if flag == 0:
        raise ValueError("ProjectID doesn't exist")
    
    stu_IDs = []
    directory = "circuits"
    for circ_file in os.listdir(directory): 
        match = re.findall(r"\d\d-\d-\d\d",circ_file)
        if match[0] in circ_IDs:
            for line in open(f"circuits/{circ_file}","r"):
                match2 = re.compile(r"\d\d\d\d\d-\d\d\d\d\d")
                for m in re.finditer(match2, line):
                    stu_IDs.append(line)
    
    for i in range(len(stu_IDs)):
        stu_IDs[i] = (stu_IDs[i].strip())

    new_f = "maps/students.dat"
    name_set = set()
    i = 0
    with open (f"{new_f}",'r') as data:
            for line in data:
                if i >= 2:
                    line = line.split()
                    #print(f'line[3] = {line[3]}')
                    if line[3] in stu_IDs:
                        name_set.add(line[0]+" "+line[1])
                i += 1
    #print(f'name_set = {name_set}')
    return name_set


# P5
def getCostOfProjects():
    # Get the cost of every circuit
    res = {}
    circuit_cost = {}
    directory = "circuits"
    for circ_file in os.listdir(directory): 
        # Get all components 
        cost = component_cost(circ_file)
        match = re.findall(r"\d\d-\d-\d\d",circ_file)
        circuit_cost[match[0]] = cost
    
    proj_path = "maps/projects.dat"
    i = 0
    with open (proj_path,"r") as proj_data:
        for line in proj_data:
            if i >= 2:
                line = line.split()
                if line[1] not in res:
                    res[line[1]] = circuit_cost[line[0]]
                elif line[1] in res:
                    res[line[1]] += circuit_cost[line[0]]
            i += 1

    fin = {}
    k = 2
    for key in res:
        fin[key] = round(res[key],k)
    #print(fin)
    return fin

# Helper function for P5    
def component_cost(circ_file):
    comp_list = []
    with open (f"circuits/{circ_file}",'r') as file:
            dropped = dropwhile(lambda _line: 'Components:' not in _line,file)
            next(dropped, '')
            for line in dropped:
                if line.startswith("-") :
                        continue
                else:
                    comp_list.append(line)
    
    #print(f'comp_list = {comp_list[0]}')
    # comp_list has all component ids
    i = 0
    cost = 0
    list_of_files = ["maps/capacitors.dat", "maps/inductors.dat", "maps/transistors.dat", "maps/resistors.dat"]
    for file_path in list_of_files:
        with open (file_path, "r") as comp_data:
            for line in comp_data:
                line = line.split()
                if i >= 3:
                    if ("  "+line[0]) in comp_list:
                        line[1] = line[1].replace('$',"")
                        cost += float(line[1])
                i += 1
    return cost


# P6
def getProjectByComponent(componentIDs):
    circ_list = []
    proj_set = set()
    directory = "circuits"
    for id in componentIDs:
        for circ_file in os.listdir(directory): 
            with open (f"circuits/{circ_file}") as data_circ:
                if id in data_circ.read():
                    match = re.findall(r"\d\d-\d-\d\d",circ_file)
                    circ_list.append(match[0])
    i = 0
    new_f = "maps/projects.dat"
    for circ_id in circ_list:
        with open (new_f,"r") as proj_data:
                for line in proj_data:
                    if i >=2:
                        line = line.split()
                        if line[0] == circ_id:
                            proj_set.add(line[1])
                    i += 1
        
    print(f'proj_set = {proj_set}')
    return proj_set


# P7
def getCommonByProject(projectID1, projectID2):
    i = 0
    circ_list1 = []
    circ_list2 = []
    proj_path = "maps/projects.dat"
    flag = 0
    with open (proj_path,"r") as proj_data:
        for line in proj_data:
            if i >= 2:
                line = line.split()
                if line[1] == projectID1:
                    circ_list1.append(line[0])
                    flag = 1
                elif line[1] == projectID2:
                    circ_list2.append(line[0])
                    flag = 1
            i += 1
    if flag == 0:
        raise ValueError("ProjectIDs don't exist")
    
    comp_list1 = []
    comp_list2 = []
    directory = "circuits"
    for circ_file in os.listdir(directory): 
        match = re.findall(r"\d\d-\d-\d\d",circ_file)
        if match[0] in circ_list1:
            with open (f"circuits/{circ_file}",'r') as file:
                dropped = dropwhile(lambda _line: 'Components:' not in _line,file)
                next(dropped, '')
                for line in dropped:
                    if line.startswith("-") :
                        continue
                    else:
                        comp_list1.append(line)
    
    '''print(f"circ_list1 = {circ_list1}")
    print("-------------------------")
    print(f"circ_list2 = {circ_list2}")'''

    for circ_file in os.listdir(directory): 
        match = re.findall(r"\d\d-\d-\d\d",circ_file)
        if match[0] in circ_list2:
            with open (f"circuits/{circ_file}",'r') as file:
                dropped = dropwhile(lambda _line: 'Components:' not in _line,file)
                next(dropped, '')
                for line in dropped:
                    if line.startswith("-") :
                        continue
                    else:
                        comp_list2.append(line)
    
    #print(len(set(comp_list2)))
    intersection_list = [id for id in comp_list1 if id in comp_list2]
    intersection_list = [i.strip() for i in intersection_list]
    intersection_list = set(intersection_list)
    intersection_list = list(intersection_list)
    intersection_list = sorted(intersection_list)
    #print(f'Intersection list = {intersection_list}')
    return intersection_list

def getComponentReport(componentIDs):
    res = {}
    directory = "circuits"
    count = 0
    for id in componentIDs:
        for circ_file in os.listdir(directory): 
            count += 1
            with open (f"circuits/{circ_file}","r") as file:
                if id in file.read():
                    if id not in res:
                        res[id] = 1
                    else:
                        res[id] += 1

    
    #print(f'res = {res}')
    #print(count)
    return res  

# P9
def getCircuitByStudent(studentNames):
    i = 0
    circ_id_set = set()
    stu_path = "maps/students.dat"
    stu_id_set = set()
    for name in studentNames:
        with open (stu_path,"r") as stu_data:
            for line in stu_data:
                if i >= 2:
                    if line.startswith("-") :
                        continue
                    line = line.split()
                    #print(f' line = {line}')
                    if name == line[0]+" "+line[1]:
                        stu_id_set.add(line[3])
                i += 1
    #print(stu_id_set)
    directory = "circuits"
    for id in stu_id_set:
        for circ_file in os.listdir(directory):
            with open(f"circuits/{circ_file}","r") as data_circ:
                if id in data_circ.read():
                    match = re.findall(r"\d\d-\d-\d\d",circ_file)
                    circ_id_set.add(match[0])
    #print(f'circ_id_set = {circ_id_set}')
    return circ_id_set

 # P10
def getCircuitByComponent(componentIDs):
    circ_id_set = set()
    directory = "circuits"
    for comp_id in componentIDs:
        for circ_file in os.listdir(directory):
            with open(f"circuits/{circ_file}","r") as data_circ:
                if comp_id in data_circ.read():
                    match = re.findall(r"\d\d-\d-\d\d",circ_file)
                    circ_id_set.add(match[0])
    print(f'circ_id_set = {circ_id_set}')
    return circ_id_set

#getComponentCountByProject("D88C2930-9DA4-431F-8CDB-99A2AA2C7A05", 'I')
#getComponentCountByStudent("Adams, Keith", "R") # p2
#getParticipationByStudent("Turner, Theresa") # p3
#getParticipationByProject("082D6241-40EE-432E-A635-65EA8AA374B6") # p4
getCostOfProjects() # p5
'''componentIDs = {"UTH-014",
  "TKW-534", "TTV-875",  "QIC-567",  "YCX-527" # p6, p8, p10
  ,"CMN-194"
  ,"LFC-108"
  ,"RLE-280"
  ,"CGN-543"}'''
#getProjectByComponent({'LFC-108', 'DCB-178'}) # p6
#getCommonByProject("082D6241-40EE-432E-A635-65EA8AA374B6", "90BE0D09-1438-414A-A38B-8309A49C02EF") # p7 
#getComponentReport(comp_set) # p8
#studentNames = {"Butler, Julia", "Campbell, Eugene","Carter, Sarah"}
#getCircuitByStudent({"Allen, Amanda", "Baker, Craig"}) #p9
#getCircuitByComponent({'LFC-108', 'DCB-178'})# p10

# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################
'''if __name__ == " __main__ " :
# Write anything here to test your code .
    projectID = "082D6241-40EE-432E-A635-65EA8AA374B6"
    componentSymbol = "R"
    count = getComponentCountByProject(projectID, componentSymbol)
    print(count)
    #print("Hi") '''
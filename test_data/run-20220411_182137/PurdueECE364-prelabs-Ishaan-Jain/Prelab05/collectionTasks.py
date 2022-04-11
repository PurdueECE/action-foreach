# ######################################################
# Author : Ishaan Jain
# email : jain343@purdue.edu
# ID : ee364b04
# Date : 02/13/2022
# ######################################################
import os
from re import X
#import readline
from signal import pthread_kill # List of module import statements
import sys # Each one on a line
# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################
def getComponentCountByProject(projectID, componentSymbol) :

    projFile = "./maps/projects.dat"
    resFile = "./maps/resistors.dat"
    indFile = "./maps/inductors.dat"
    transFile = "./maps/transistors.dat"

    f = open(projFile,"r")

    l = f.readlines()[2:]

    proj_list = []
    circ_list = []
    comp_list = []
    proj_list1 = []


    for line in l:
        l_line = line.lstrip()
        l_line = l_line.split()
        proj_list.append(l_line)
        proj_list1.append(l_line[1])


    tupleList = [tuple(y) for y in proj_list if projectID in y]
    
    


    count = 1
    for x in proj_list1:
        if projectID == x:
            count = 0

    if count == 1:
        raise ValueError("Project ID not found")

    for h in tupleList:
        for cir in h:
            if len(cir) == 7:
                circ_list.append(cir)
      
    
    for x in circ_list:
        with open("./circuits/circuit_"+ str(x) + ".dat") as circ_f:
            for lines in circ_f:
                if "Components" in lines:
                    l = circ_f.readlines()[1:]
                    for lines in l:
                        b = lines.split()
                        comp_list.append(b)

    total = 0
    
    for x in comp_list:
        for y in x:
            total += helperFor1(componentSymbol,y)  


                        


    f.close()

    return total


def helperFor1(componentSymbol,componentID):
    

    component_list = []
    
    total = 0

    if componentSymbol == "I":
        
        f = open("./maps/inductors.dat","r")
        l = f.readlines()[3:]
        for line in l:
            stuff = line.split()
            component_list.append(stuff[0])

        for x in component_list:
            if componentID == x:
                total += 1

                
        f.close()        
    elif componentSymbol == "R":
        f = open("./maps/resistors.dat","r")
        l = f.readlines()[3:]
        for line in l:
            stuff = line.split()
            component_list.append(stuff[0])


        for x in component_list:
            if componentID == x:
                print(componentID)
                total += 1
              
        f.close()        
    elif componentSymbol == "T":
        f = open("./maps/transistors.dat","r")
        l = f.readlines()[3:]
        for line in l:
            stuff = line.split()
            component_list.append(stuff[0])

      

        for x in component_list:
            if componentID == x:
                total += 1 

        f.close()        
    elif componentSymbol == "C":
        f = open("./maps/capacitors.dat","r")
        l = f.readlines()[3:]
        for line in l:
            stuff = line.split()
            component_list.append(stuff[0])


        for x in component_list:
            if componentID == x:
                total += 1 
        f.close()          

    
    return total  

def getComponentCountByStudent(studentName, componentSymbol):

    StuFile = "./maps/students.dat"
    resFile = "./maps/resistors.dat"
    indFile = "./maps/inductors.dat"
    transFile = "./maps/transistors.dat"

    f = open(StuFile,"r")

    l = f.readlines()[2:]

    stu_list = []
    circ_list = []
    comp_list = []
    ID_list = []

    stu_dict = {}


    for line in l:
        #l_line = line.lstrip()
        key,val = line.strip().split('|')
        stu_dict.update({key:val})

    stu_dict = {y.replace(" ",""):v.replace(" ","") for y,v in stu_dict.items()}
    stu_dict = {x.replace(",",", "):v for x, v in stu_dict.items()}

    
    yes = 0
    for key in stu_dict:
        if key == studentName:
            yes = 1
            ID_list.append(stu_dict[key])

    if yes == 0:
        raise ValueError("Name does not exist")


    
    for cir_file in os.listdir("circuits/"):
        with open("circuits/"+str(cir_file)) as circ_f:
           for lines in circ_f:
               if stu_dict[studentName] in lines:
                   circ_list.append(cir_file)

    for files in circ_list:
        j = open("circuits/"+str(files),"r")
        for lines in j:
                if "Components" in lines:
                    l = j.readlines()[1:]
                    for lines in l:
                        b = lines.split()
                        comp_list.append(b)

    j.close()
                
    total = 0
    
    for x in comp_list:
        for y in x:
            total += helperFor1(componentSymbol,y)  


                        


    f.close()

    return total



   
def getParticipationByStudent(studentName):  
    StuFile = "./maps/students.dat"
    resFile = "./maps/resistors.dat"
    indFile = "./maps/inductors.dat"
    transFile = "./maps/transistors.dat"
    projFile = "./maps/projects.dat"

    f = open(StuFile,"r")
    f1 = open(projFile,"r")

    l = f.readlines()[2:]
    l1 = f1.readlines()[2:]

    stu_list = []
    circ_list = []
    comp_list = []
    ID_list = []
    proj_list = []
    proj_list1 = set()


    stu_dict = {}

    for line in l1:
        l_line = line.lstrip()
        l_line = l_line.split()
        proj_list.append(l_line)

      

    #tupleList = [tuple(y) for y in proj_list if projectID in y]    


    for line in l:
        #l_line = line.lstrip()
        key,val = line.strip().split('|')
        stu_dict.update({key:val})

    stu_dict = {y.replace(" ",""):v.replace(" ","") for y,v in stu_dict.items()}
    stu_dict = {x.replace(",",", "):v for x, v in stu_dict.items()}

    
    yes = 0
    for key in stu_dict:
        if key == studentName:
            yes = 1
            ID_list.append(stu_dict[key])

    if yes == 0:
        raise ValueError("Name does not exist")
    
    for cir_file in os.listdir("circuits/"):
        with open("circuits/"+str(cir_file)) as circ_f:
           for lines in circ_f:
               if stu_dict[studentName] in lines:
                   circ_list.append(cir_file)

    for cir in circ_list:
        for x in proj_list:
            if cir[8:15] == x[0]:
                proj_list1.add(x[1])
                        


    f.close()
    f1.close()

    return proj_list1                                          

def getProjectByComponent(componentIDs):

    comp_list = []
    ID_list = []
    proj_list = set()

    projFile = "./maps/projects.dat"

    for cir_file in os.listdir("circuits/"):
        with open("./circuits/"+ str(cir_file)) as circ_f:
            for lines in circ_f:
                if "Components" in lines:
                    l = circ_f.readlines()[1:]
                    for lines in l:
                        b = lines.split()
                        for x in componentIDs:
                            if b[0] == x:
                                ID_list.append(cir_file[8:15])

    f1 = open(projFile,"r")
    l1 = f1.readlines()[2:]

    for line in l1:
        l_line = line.lstrip()
        l_line = l_line.split()
        for x in ID_list:
            if x == l_line[0]:
                proj_list.add(l_line[1])

    f1.close()            
            

    return proj_list


def getCircuitByStudent(studentNames):
    StuFile = "./maps/students.dat"
    resFile = "./maps/resistors.dat"
    indFile = "./maps/inductors.dat"
    transFile = "./maps/transistors.dat"
    projFile = "./maps/projects.dat"

    f = open(StuFile,"r")
    f1 = open(projFile,"r")

    l = f.readlines()[2:]
    l1 = f1.readlines()[2:]

    stu_list = []
    circ_list = []
    comp_list = []
    ID_list = []
    proj_list = []
    proj_list1 = set()


    stu_dict = {}

    for line in l1:
        l_line = line.lstrip()
        l_line = l_line.split()
        proj_list.append(l_line)

      

    #tupleList = [tuple(y) for y in proj_list if projectID in y]    


    for line in l:
        #l_line = line.lstrip()
        key,val = line.strip().split('|')
        stu_dict.update({key:val})

    stu_dict = {y.replace(" ",""):v.replace(" ","") for y,v in stu_dict.items()}
    stu_dict = {x.replace(",",", "):v for x, v in stu_dict.items()}

    
    for cir_file in os.listdir("circuits/"):
        with open("circuits/"+str(cir_file)) as circ_f:
           for lines in circ_f:
               for x in studentNames:
                    if stu_dict[x] in lines:
                        circ_list.append(cir_file)

    for cir in circ_list:
        for x in proj_list:
            if cir[8:15] == x[0]:
                proj_list1.add(x[1])
                        


    f.close()
    f1.close()

    return proj_list1




def getCircuitByComponent(componentIDs):

    comp_list = []
    ID_list = set()


    projFile = "./maps/projects.dat"

    for cir_file in os.listdir("circuits/"):
        with open("./circuits/"+ str(cir_file)) as circ_f:
            for lines in circ_f:
                if "Components" in lines:
                    l = circ_f.readlines()[1:]
                    for lines in l:
                        b = lines.split()
                        for x in componentIDs:
                            if b[0] == x:
                                ID_list.add(cir_file[8:15])

            

    return ID_list
                    


    

    

                










# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################

# Write anything here to test your code .
#print("hi")
#total =getComponentCountByProject("8C71F259-ECA8-4267-A8B3-6CAD6451D4CC", "R")
id_list = {"TAZ-349","ORW-143"}

data = getCircuitByComponent(id_list)
print(data)


    

import os # List of module import statements
import sys # Each one on a line
import re
from helper import *

def getAllResistors():
    resistors = []

    with open('maps/resistors.dat') as f:
        lines = f.readlines()[3:]
        for line in lines:
            resistors.append(line[0:7])

    return resistors

def getAllInductors():
    inductors = []

    with open('maps/inductors.dat') as f:
        lines = f.readlines()[3:]
        for line in lines:
            inductors.append(line[0:7])

    return inductors

def getAllCapacitors():
    capacitors = []

    with open('maps/capacitors.dat') as f:
        lines = f.readlines()[3:]
        for line in lines:
            capacitors.append(line[0:7])

    return capacitors

def getAllTransistors():
    transistors = []

    with open('maps/transistors.dat') as f:
        lines = f.readlines()[3:]
        for line in lines:
            transistors.append(line[0:7])

    return transistors

def isParticipant(studentID, path):

    with open(str(path)) as f:
        lines = f.readlines()
        for line in lines:
            if(studentID in line):
                return True
            else:
                continue
    return False

def getStudentNameByID(studentID):

    with open('maps/students.dat') as f:
        lines = f.readlines()
        for line in lines:
            if(studentID in line):
                name = re.sub(' +', ' ', line[0:27])
                return name


def getComponentPriceDict():
    compPrice = {}

    with open('maps/resistors.dat') as f:
        lines = f.readlines()[3:]
        for line in lines:
            compPrice.update({line[0:7] : line[22:26]})
    with open('maps/capacitors.dat') as f:
        lines = f.readlines()[3:]
        for line in lines:
            compPrice.update({line[0:7] : line[22:26]})
    with open('maps/inductors.dat') as f:
        lines = f.readlines()[3:]
        for line in lines:
            compPrice.update({line[0:7] : line[22:26]})
    with open('maps/transistors.dat') as f:
        lines = f.readlines()[3:]
        for line in lines:
            compPrice.update({line[0:7] : line[22:26]})

    return compPrice   

def getProjects():
    projects = set()
    with open('maps/projects.dat') as f:
        lines = f.readlines()[3:]
        for line in lines:
            projects.add(line[21:57])
    print(projects)
    return projects                       

def getCircuitsByProjectID(projectID):
    circuits = set()

    with open('maps/projects.dat') as f:
        lines = f.readlines()[3:]
        for line in lines:
            if (projectID in line):
                circuits.add(line[4:11])

    return circuits

def getCostOfCircuit(circuitID):
    prices = getComponentPriceDict()
    cost = 0.0
    with open('circuits/circuit_' + circuitID + '.dat') as f:
        lines = f.readlines()
        for line in lines:
            for key in prices:
                if key in line:
                    price = float(prices[key])
                    cost = cost + price

    return cost

def getCircuitsByComponentID(componentID):
    circuits= set()
    for file in os.listdir('circuits/'):
        with open(os.path.join("circuits/", file), 'r') as f:
            lines = f.readlines()
            for line in lines:
                if(componentID in line):
                    circuits.add(f.name[17:24])

    return circuits

def getComponentsOfCircuit(circuitID):
    components = set()
    flag = 0
    with open('circuits/circuit_' + circuitID + '.dat') as f:
        lines = f.readlines()
        for line in lines:    
            if(flag == 1):
                components.add(line[0:7])
            if('Components' in line):
                flag = 1
                continue

    return components



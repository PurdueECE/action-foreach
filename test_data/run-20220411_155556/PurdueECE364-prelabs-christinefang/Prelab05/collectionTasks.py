# ######################################################
# Author : Lingyue Christine Fang
# email : fang245@purdue.edu
# ID : ee364b09
# Date : February 11, 2022
# ######################################################
import os # List of module import statements
import sys # Each one on a line
# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################
def getfilename(componentSymbol):
    if componentSymbol == 'R':
        filename = 'maps/resistors.dat'
    elif componentSymbol == 'C':
        filename = 'maps/capacitors.dat'
    elif componentSymbol == 'I':
        filename = 'maps/inductors.dat'
    elif componentSymbol == 'T':
        filename = 'maps/transistors.dat'
    l = []
    fy = open(filename)
    ln = fy.readlines()[3:]
    for line in ln:
        l += [line.split()]
    return l
def studentID(studentName):
    lst = []
    file = open('maps/students.dat')
    lines = file.readlines()[2:]
    for line in lines:
        lst += [line.split()]
    col = []
    for i in lst:
        name = i[0]+ ' ' +i[1]
        if name == studentName:
            col.append(i[3])
 
    if len(col) == 0:
        raise ValueError('student does not exist')
    return col[0]

def getprojectID(projectID):
    lst = []
    file = open('maps/projects.dat')
    lines = file.readlines()[2:]
    for line in lines:
        lst += [line.split()]
    col = []
    for i in lst:
        if i[1] == projectID:
            col.append(i[0])
    if len(col) == 0:
        raise ValueError('projectID does not exist')
    return col

def getComponentCountByProject (projectID, componentSymbol):
    l = getfilename(componentSymbol)
    proj = getprojectID(projectID)
    total = 0
    tot = set([])
    for i in l: #for each componenent in l
        for num in proj: #each circuit ID
            z = 'circuits/circuit_' + num + '.dat'
            fp = open(z,'r')
            for line in fp:
                line = line.strip()
                if i[0] == line:
                    tot.add(i[0])
    for i in tot:
        total +=1
    return total

def getComponentCountByStudent(studentName, componentSymbol):
    complist = getfilename(componentSymbol)
    col = studentID(studentName)
    total = 0
    tot = set([])
    for root,dirs,files in os.walk('circuits'): #searches directory
        for u in files: # searches filenames
            z = 'circuits/' + u
            file1 = open(z,'r')
            for line in file1: #searches through file
                line = line.strip()
                if col == line:
                    file2 = open(z,'r')
                    for l in file2: #searches through file
                        l = l.strip()
                        for i in complist: #for each componenent in l
                            if l == i[0]:
                                tot.add(l)
    for i in tot:
        total+=1
    return total

def getParticipationByStudent(studentName):
    col = studentID(studentName)
    projlist= []
    file2 = open('maps/projects.dat')
    li = file2.readlines()[2:]
    for lis in li:
        projlist += [lis.split()]

    out = set([])
    for root,dirs,files in os.walk('circuits'): #searches directory
        for u in files: # searches filenames
            z = 'circuits/' + u
            file1 = open(z,'r')
            for line in file1: #searches through file line by line
                line = line.strip()
                if col == line:
                    for column in projlist:
                        if column[0] in u:
                            out.add(column[1])
    return out

def getParticipationByProject(projectID):
    lst = []
    file = open('maps/students.dat')
    lines = file.readlines()[2:]
    for line in lines:
        lst += [line.split()]
    projlist = getprojectID(projectID)

    s = set([])
    for i in projlist:
        f = 'circuits/circuit_' + i + '.dat'
        file1 = open(f,'r')
        for line in file1: #searches through file
            line = line.strip()
            for j in lst:
                if j[3] == line:
                    z = j[0] + ' ' + j[1]
                    s.add(z)
    return s

def addComp(filename):
    filec = open(filename,'r')
    linec = filec.readlines()[3:]
    caps = []
    for lin in linec:
        caps += [lin.split()]
    return caps

def getCostOfProjects():
    my_dict = {}
    projIDlst = []
    file = open('maps/projects.dat')
    lines = file.readlines()[2:]
    for line in lines:
        projIDlst += [line.split()]
    for i in projIDlst:
        my_dict[i[1]] =0
        f = 'circuits/circuit_' + i[0] + '.dat'
        file1 = open(f,'r')
        for fileline in file1: #searches through file
            fileline = fileline.strip()
            #search capacitors
            caps = addComp('maps/capacitors.dat')
            for c in caps:
                if c[0] == fileline:
                    x = c[1].replace("$","")
                    x = float(x)
                    my_dict[i[1]] += x
                    my_dict[i[1]] = "{:.2f}".format(my_dict[i[1]])
                    my_dict[i[1]] = float(my_dict[i[1]])
            #search resistors
            res = addComp('maps/resistors.dat')
            for c in res:
                if c[0] == fileline:
                    x = c[1].replace("$","")
                    x = float(x)
                    my_dict[i[1]] += x
                    my_dict[i[1]] = "{:.2f}".format(my_dict[i[1]])
                    my_dict[i[1]] = float(my_dict[i[1]])
            #search inductors
            ind = addComp('maps/inductors.dat')
            for c in ind:
                if c[0] == fileline:
                    x = c[1].replace("$","")
                    x = float(x)
                    my_dict[i[1]] += x
                    my_dict[i[1]] = "{:.2f}".format(my_dict[i[1]])
                    my_dict[i[1]] = float(my_dict[i[1]])
            #search transistors
            trans = addComp('maps/transistors.dat')
            for c in trans:
                if c[0] == fileline:
                    x = c[1].replace("$","")
                    x = float(x)
                    my_dict[i[1]] += x
                    my_dict[i[1]] = "{:.2f}".format(my_dict[i[1]])
                    my_dict[i[1]] = float(my_dict[i[1]])

    return(my_dict)

def getProjectByComponent(componentIDs):
    out = set([])
    projIDlst = []
    l = set([])
    file = open('maps/projects.dat')
    lines = file.readlines()[2:]
    for line in lines:
        projIDlst += [line.split()]

    for i in componentIDs:
        for root,dirs,files in os.walk('circuits'): #searches directory
            for u in files: # searches filenames
                z = 'circuits/' + u
                file1 = open(z,'r')
                for line in file1: #searches through file
                    line = line.strip()
                    if line == i:
                        for j in projIDlst:
                            if j[0] in u:
                                out.add(j[1])
                                
    return out

def getCommonByProject(projectID1, projectID2):
    commonlist = set([])
    projIDlst = []
    file = open('maps/projects.dat')
    lines = file.readlines()[2:]
    for line in lines:
        projIDlst += [line.split()]
    p1 = set([])
    p2 = set([])
    for i in projIDlst:
        if i[1] == projectID1:
            f = 'circuits/circuit_' + i[0] + '.dat'
            file1 = open(f,'r')
            for line in file1: #searches through file
                if '  ' in line:
                    line = line.strip()
                    p1.add(line)
    if len(p1) == 0:
        raise ValueError('projectID does not exist')
    for i in projIDlst:
        if i[1] == projectID2:
            f = 'circuits/circuit_' + i[0] + '.dat'
            file1 = open(f,'r')
            for line in file1: #searches through file
                if '  ' in line:
                    line = line.strip()
                    p2.add(line)
    if len(p2) == 0:
        raise ValueError('projectID does not exist')

    common = p1.intersection(p2)
    commonlist = sorted(common)
    return commonlist

def getComponentReport(componentIDs):
    my_dict = {}
    for i in componentIDs:
        my_dict[i] = 0
        for root,dirs,files in os.walk('circuits'): #searches directory
            for u in files: # searches filenames
                z = 'circuits/' + u
                file1 = open(z,'r')
                for line in file1: #searches through file
                    line = line.strip()
                    if line == i:
                        my_dict[i] += 1
    return my_dict

def getCircuitByStudent(studentNames):
    circID = set([])
    projIDlst = []
    fp = open('maps/projects.dat','r')
    lines = fp.readlines()[2:]
    for line in lines:
        projIDlst += [line.split()]
    
    for i in studentNames:
        studID = studentID(i)
        for root,dirs,files in os.walk('circuits'): #searches directory
            for u in files: # searches filenames
                z = 'circuits/' + u
                file1 = open(z,'r')
                for line in file1: #searches through file
                    line = line.strip()
                    if studID == line:
                        for j in projIDlst:
                            if j[0] in u:
                                circID.add(j[0])
    return circID
        
def getCircuitByComponent(componentIDs):
    circID = set([])
    projIDlst = []
    fp = open('maps/projects.dat','r')
    lines = fp.readlines()[2:]
    for line in lines:
        projIDlst += [line.split()]
    for i in componentIDs:
        for root,dirs,files in os.walk('circuits'): #searches directory
            for u in files: # searches filenames
                z = 'circuits/' + u
                file1 = open(z,'r')
                for line in file1: #searches through file
                    line = line.strip()
                    if i == line:
                        for j in projIDlst:
                            if j[0] in u:
                                circID.add(j[0])
    return circID

# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################
if __name__ == "__main__":
    # Write anything here to test your code . 
    #num = getComponentCountByProject('082D6241-40EE-432E-A635-65EA8AA374B6', 'R')
    num = getComponentCountByStudent('Scott, Michael', 'I')

    #num = getParticipationByStudent("Adams, Keith")
    #num = getParticipationByProject('56B13184-D087-48DB-9CBA-84B40FE17CC5')

    #num = getCostOfProjects()
    components = set(['RHN-678','RFY-461'])
    #num = getProjectByComponent(components)
    #num = getCommonByProject('082D6241-40EE-432E-A635-65EA8AA374B6','075A54E6-530B-4533-A2E4-A15226BE588C')
    #num = getComponentReport(components)
    studentNames = set(['Adams, Keith', 'Baker, Craig', 'Clark, Joe','Bell, Kathryn'])
    #num = getCircuitByStudent(studentNames)
    #num = getCircuitByComponent(components)
    print(num)
    tot = 0
    #for i in num:
       # tot +=1
    #print(tot)
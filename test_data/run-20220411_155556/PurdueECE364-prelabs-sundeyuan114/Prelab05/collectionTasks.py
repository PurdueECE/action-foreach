#######################################################
# Author: Deyuan Sun    
# email: sun829@purdue.edu
# ID: ee364a04
# Date: 2/12/2022
#######################################################
from fileinput import filename
import os
import fnmatch
from unicodedata import name
#######################################################
# No Module -Level Variables or Statements!
# ONLY FUNCTIONS BEYOND THIS POINT!
#######################################################
def findComponentnumb(setComponent, componentSymbol):
    finalCount = 0
    if componentSymbol == "R":
        with open('./maps/resistors.dat', "r") as fp:
            Lines = fp.readlines()
            for line in Lines:
                if line[0:7] in setComponent:
                    #print(line[0:7])
                    finalCount = finalCount + 1
    elif componentSymbol == "I":
        with open('./maps/inductors.dat', "r") as fp:
            Lines = fp.readlines()
            for line in Lines:
                if line[0:7] in setComponent:
                    #print(line[0:7])
                    finalCount = finalCount + 1
    elif componentSymbol == "C":
        with open('./maps/capacitors.dat', "r") as fp:
            Lines = fp.readlines()
            for line in Lines:
                if line[0:7] in setComponent:
                    #print(line[0:7])
                    finalCount = finalCount + 1
    elif componentSymbol == "T":
        with open('./maps/transistors.dat', "r") as fp:
            Lines = fp.readlines()
            for line in Lines:
                if line[0:7] in setComponent:
                    #print(line[0:7])
                    finalCount = finalCount + 1
    return finalCount
    
def getComponentCountByProject(projectID, componentSymbol):
    isFound = False
    finalCount = 0
    with open('./maps/projects.dat', "r") as fp:
        listID = []
        Lines = fp.readlines()
        for line in Lines:
            if projectID in line:
                isFound = True
                listID.append(line[4:11])
        if isFound == False:
            raise ValueError('project ID not found') 
    listFile = []
    for file in os.listdir('./circuits'):
        for ID in listID:
            if fnmatch.fnmatch(file, "*"+ID+"*"):
                listFile.append(file)
    setComponent = set()
    for circuitFilename in listFile:
        with open('./circuits/'+circuitFilename, "r") as fp:
            Lines = fp.readlines()
            for line in Lines:
                if line[0:2] == "  ":
                    setComponent.add(line[2:9])
    if componentSymbol == "R":
        with open('./maps/resistors.dat', "r") as fp:
            Lines = fp.readlines()
            for line in Lines:
                if line[0:7] in setComponent:
                    finalCount = finalCount + 1
    elif componentSymbol == "I":
        with open('./maps/inductors.dat', "r") as fp:
            Lines = fp.readlines()
            for line in Lines:
                if line[0:7] in setComponent:
                    finalCount = finalCount + 1
    elif componentSymbol == "C":
        with open('./maps/capacitors.dat', "r") as fp:
            Lines = fp.readlines()
            for line in Lines:
                if line[0:7] in setComponent:
                    finalCount = finalCount + 1
    elif componentSymbol == "T":
        with open('./maps/transistors.dat', "r") as fp:
            Lines = fp.readlines()
            for line in Lines:
                if line[0:7] in setComponent:
                    finalCount = finalCount + 1
    return finalCount

def getComponentCountByStudent(studentName, componentSymbol):
    indicator = 0
    with open('./maps/students.dat', "r") as fp:
        Lines = fp.readlines()
        for line in Lines:
            if studentName in line:
                studentID = line[44:55]
                indicator = 1
        if not indicator:
            raise ValueError("student name not found")
        setComponent = set()
        for filename in os.listdir('./circuits/'):
            with open('./circuits/'+filename, "r") as fp:
                
                Lines = fp.readlines()
                res = [i for i in Lines if studentID in i]
                if res:
                    #print(filename) 
                    for line in Lines:
                        if line[0:2] == "  ":
                            setComponent.add(line[2:9])
        #print(setComponent)
        return(findComponentnumb(componentSymbol= componentSymbol, setComponent= setComponent))
def getParticipationByStudent(studentName):
    setA = set()
    studentID = getStudentIDbyName(studentName)
    setFilename = getCircuitFilenameByStudentID(studentID)
    with open('./maps/projects.dat', "r") as fp:
        Lines = fp.readlines()
        for line in Lines:
            for filename in setFilename:
                if filename[8:15] in line:
                    setA.add(line[21:57])
    return setA

            # if projectID in line:
            #     isFound = True
            #     listID.append(line[4:11])

def getCircuitFilenameByStudentID (studentID):
    setFilename = set()
    for filename in os.listdir('./circuits/'):
        with open('./circuits/'+filename, "r") as fp:
              
            Lines = fp.readlines()
            res = [i for i in Lines if studentID in i]
            if res:
                setFilename.add(filename)
    #print(setFilename)
    return setFilename
def getStudentIDbyName (studentName):
    indicator = 0
    with open('./maps/students.dat', "r") as fp:
        Lines = fp.readlines()
        for line in Lines:
            if studentName in line:
                studentID = line[44:55]
                indicator = 1
        if not indicator:
            raise ValueError("student name not found")
    return studentID
def getParticipationByProject(projectID):
    isFound = False
    finalCount = 0
    with open('./maps/projects.dat', "r") as fp:
        circuitID = []
        Lines = fp.readlines()
        for line in Lines:
            if projectID in line:
                isFound = True
                circuitID.append(line[4:11])
        if isFound == False:
            raise ValueError('project ID not found') 
        #print(circuitID)
    setStudentID = set()
    for file in os.listdir('./circuits'):
        for ID in circuitID:
            if fnmatch.fnmatch(file, "*"+ID+"*"):
                with open('./circuits/'+file, "r") as fp:
                    Lines = fp.readlines()
                    for line in Lines:
                        #print(line[0:2] + line[6])
                        if (line[0:2] != "  ") and (line[0:2] != "--") and (line[0:2] != "Pa") and (line[0:2] != "Co"):
                            setStudentID.add(line[0:11])
    setStudentID.remove("\n")
    return(geNameByStudentID(setStudentID))
def geNameByStudentID(setStudentID):
    setStudentName = set()
    # print(len(setStudentID))
    # print(setStudentID)
    count = 0
    with open('./maps/students.dat', "r") as fp:
        Lines = fp.readlines()
        for line in Lines:
            if line[44:55] in setStudentID:
                tempStr = ""
                spaceCount = 0
                for letter in line:
                    if letter == " ":
                        spaceCount = spaceCount + 1
                    if spaceCount == 2:
                        break
                    tempStr = tempStr + letter
                setStudentName.add(tempStr)

    return setStudentName
def getCostOfProjects(): #DONEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
    # first get component of project
    dictA = {}
    setProjectID = set()
    with open('./maps/projects.dat', "r") as fp:
        Lines = fp.readlines()
        for line in Lines:
            if line[21:57] not in setProjectID:
                setProjectID.add(line[21:57])
    setProjectID.remove('         Project ID               \n')
    setProjectID.remove('------------------------------------')
    for projectID in setProjectID:
        circuitList = getCircuitListByProject(projectID)
        componentList = getComponentListByCircuitList(circuitList)
        money = round(getTotalPriceOfAComponentList(componentList),2)
        dictA[projectID] = money
    return dictA
    #print(dictComponent)
    #在这里 dictComp 是一个对应所有元件与其数量信息的元素
    #接下来找到每一个元件的价格相乘就获得最终的dict

    #print(setProjectID)
    # print(len(setProjectID))

    pass
def getTotalPriceOfAComponentList (componentList):
    money = 0
    for comp in componentList:
##  
        with open('./maps/resistors.dat', "r") as fp:
            Lines = fp.readlines()
            for line in Lines:
                if comp in line:
                    money += float(line[22:27])
        with open('./maps/inductors.dat', "r") as fp:
            Lines = fp.readlines()
            for line in Lines:
                if comp in line:
                    money += float(line[22:27])
        with open('./maps/capacitors.dat', "r") as fp:
            Lines = fp.readlines()
            for line in Lines:
                if comp in line:
                    money += float(line[22:27])
        with open('./maps/transistors.dat', "r") as fp:
            Lines = fp.readlines()
            for line in Lines:
                if comp in line:
                    money += float(line[22:27])
    return money
######
    pass
def getComponentListByCircuitList(listID):
    componentList = []
    for file in os.listdir('./circuits'):
        for ID in listID:
            if fnmatch.fnmatch(file, "*"+ID+"*"):
                with open('./circuits/'+file, "r") as fp:
                    Lines = fp.readlines()
                    for line in Lines:
                        #print(line[0:2] + line[6])
                        if (line[0:2] == "  "):
                            componentList.append(line[2:9])                    
    #print(componentList)    
    return componentList            
    
def getCircuitListByProject(projectID):
    indicator = 0
    with open('./maps/projects.dat', "r") as fp:
        circuitIDlist = []
        Lines = fp.readlines()
        for line in Lines:
            if projectID in line:
                indicator = 1
                circuitIDlist.append(line[4:11])
        if '-------' in circuitIDlist:
            circuitIDlist.remove('-------')
    if not indicator:
        raise ValueError('project ID not found') 
    return circuitIDlist

    pass
def getProjectByComponent(componentIDs):
    totalset = set()
    for componenetID in componentIDs:
        setCircuitID = set()
        for filename in os.listdir('./circuits/'):
            with open('./circuits/'+filename, "r") as fp: 
                Lines = fp.readlines()
                res = [i for i in Lines if componenetID in i]
                if res:
                    setCircuitID.add(filename[8:15])
        with open('./maps/projects.dat', "r") as fp:
            setProjectID = set()
            Lines = fp.readlines()
            for line in Lines:
                for circuitID in setCircuitID:
                    if circuitID in line:
                        setProjectID.add(line[21:57])
        totalset.update(setProjectID)
    return totalset
def getCommonByProject(projectID1, projectID2):
    list1 = getCircuitListByProject(projectID1)
    list2 = getCircuitListByProject(projectID2)
    compList1 = getComponentListByCircuitList(list1)
    compList2 = getComponentListByCircuitList(list2)
    rtList = []
    for elementofList1 in compList1:
        if elementofList1 in compList2:
            rtList.append(elementofList1)
        rtList.sort()
    return rtList
    
    pass

def getComponentReport(componentIDs):
    totalComponentList = []
    setProjectID = set()
    with open('./maps/projects.dat', "r") as fp:
        Lines = fp.readlines()
        for line in Lines:
            if line[21:57] not in setProjectID:
                setProjectID.add(line[21:57])
    setProjectID.remove('         Project ID               \n')
    setProjectID.remove('------------------------------------')
    for projectID in setProjectID:
        circuitList = getCircuitListByProject(projectID)
        componentList = getComponentListByCircuitList(circuitList)
        totalComponentList += componentList
    dictA = {}
    for component in componentIDs:
        tempCount = totalComponentList.count(component)
        dictA[component] = tempCount
    return dictA

def getCircuitByStudent(studentNames):
    circuitSet = set()
    listStudentID = []
    for student in studentNames:
        listStudentID.append(getStudentIDbyName(student))
    for studentID in listStudentID:
        for filename in os.listdir('./circuits/'):
                    with open('./circuits/'+filename, "r") as fp:
                        Lines = fp.readlines()
                        res = [i for i in Lines if studentID in i]
                        if res:
                            circuitSet.add(filename[8:15]) 
    return circuitSet
    
def getCircuitByComponent(componentIDs):
    circuitSet = set()
    for comp in componentIDs:
        for filename in os.listdir('./circuits/'):
                    with open('./circuits/'+filename, "r") as fp:
                        Lines = fp.readlines()
                        res = [i for i in Lines if comp in i]
                        if res:
                            circuitSet.add(filename[8:15]) 
    return circuitSet
    pass

# This block is optional and can be used for testing.
# We will NOT look into its content.
#######################################################
if __name__ == "__main__":
# Write anything here to test your code.
    # print(getComponentCountByProject("082D6241-40EE-432E-A635-65EA8AA374B6", "R"))
    # print(getComponentCountByProject("082D6241-40EE-432E-A635-65EA8AA374B6", "I"))
    # print(getComponentCountByProject("082D6241-40EE-432E-A635-65EA8AA374B6", "C"))
    # print(getComponentCountByProject("082D6241-40EE-432E-A635-65EA8AA374B6", "T"))
    #print(getComponentCountByStudent("Adams, Keith", "R"))
    #print(getParticipationByStudent("Alexander, Carlos"))
    #print(getParticipationByProject("082D6241-40EE-432E-A635-65EA8AA374B6"))
    #print(getCostOfProjects())
    # listA = ["88-4-47"]
    # print(getTotalPriceOfAComponentList(getComponentListByCircuitList(listA)))
    #print(getCommonByProject("082D6241-40EE-432E-A635-65EA8AA374B61", "96CC6F98-B44B-4FEB-A06B-390432C1F6EA"))
    # listComps = ["CLQ-971", "LCD-472"]
    # print(getComponentReport(listComps))
    # studentset = {"Adams, Keith", "Alexander, Carlos"}
    # print(getCircuitByStudent(studentset))
    # studentset = ["Adams, Keith", "Alexander, Carlos"]
    # print(getCircuitByStudent(studentset))
    studentset = {"TAK-481"}
    print(getCircuitByComponent(studentset))
    pass
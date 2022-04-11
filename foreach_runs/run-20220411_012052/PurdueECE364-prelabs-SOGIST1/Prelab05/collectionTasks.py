#################################################################
#		Author: Luke Chigges
#		email:  lchigges@gmail.com
#		ID:     ee364b02
#		Date:   2/13/2022
#################################################################

import os 		# List of module import statements
import sys 		# Each one of a line
import re		# regular expressions

#################################################################
#		No Module-Level Variables or Statements!
#		ONLY FUNCTIONS BEYOND THIS POINT!
#################################################################

def getComponentCountByProject(projectID: str, componentSymbol: str) -> int:
	# get all unique circuitIDs associated with the projectID
	circuitIDs = set()
	with open("maps/projects.dat", "r") as projects:
		lines = projects.readlines()
		for line in lines:
			if(projectID in line):
				circuitIDs.add(line.split()[0])	

	# if projectID does not exist
	if(len(circuitIDs) == 0):
		raise ValueError("project ID provided does not exist.")
				
	# convert to circuit file names
	circuit_file_names = []
	for ID in circuitIDs:
		circuit_file_names.append("circuits/circuit_"+ID+".dat")
		
	# look through each circuit file and find each unique component relating to componentSymbol
	component_file = {"R":"maps/resistors.dat", "I":"maps/inductors.dat", "C":"maps/capacitors.dat", "T":"maps/transistors.dat", "L":"maps/inductors.dat"}
	components = set()
	with open(component_file[componentSymbol], "r") as component_data:
		data_lines = component_data.readlines()
		for file in circuit_file_names:
			with open(file, "r") as circuits:
				circuit_lines = circuits.readlines()
				for line in circuit_lines:
					for data in data_lines:
						if((line.strip() in data) and (re.search("[A-Z]", line.strip()) is not None)): # if there's a match and it is not file formatting
							components.add(line.strip())
	return len(components)

def getComponentCountByStudent(studentName: str, componentSymbol: str) -> int:
	# get student's ID
	studentID = ""
	with open("maps/students.dat", "r") as students:
		lines = students.readlines()
		for line in lines:
			if(studentName in line):
				studentID = line.split()[3]

	# find circuit files containing the studentID
	circuits = []
	for i in os.listdir("./circuits/"):
		if(re.search("circuit", i) is not None):
			circuits.append(i)
	for i in range(len(circuits)):
		circuits[i] = "./circuits/" + circuits[i]

	student_circuit_files = []
	for files in circuits:
		with open(files, "r") as circuit:
			lines = circuit.readlines()
			for line in lines:
				if(studentID in line):
					student_circuit_files.append(files)

	# if student has no circuit files raise ValueError
	if(len(student_circuit_files) == 0):
		raise ValueError("Student has not participated in any projects.")

	# get count of components
	component_file = {"R":"maps/resistors.dat", "I":"maps/inductors.dat", "C":"maps/capacitors.dat", "T":"maps/transistors.dat", "L":"maps/inductors.dat"}
	components = set()
	with open(component_file[componentSymbol], "r") as component_data:
		data_lines = component_data.readlines()
		for file in student_circuit_files:
			with open(file, "r") as circuits:
				circuit_lines = circuits.readlines()
				for line in circuit_lines:
					for data in data_lines:
						if((line.strip() in data) and (re.search("[A-Z]", line.strip()) is not None)): # if there's a match and it is not file formatting
							components.add(line.strip())
	return len(components)

def getParticipationByStudent(studentName: str) -> set:
	# get student's ID
	studentID = ""
	with open("maps/students.dat", "r") as students:
		lines = students.readlines()
		for line in lines:
			if(studentName in line):
				studentID = line.split()[3]
	if(studentID == ""):
		raise ValueError("Student name passed does not exist")

	# find circuit files containing the studentID
	circuits = []
	for i in os.listdir("./circuits/"):
		if(re.search("circuit", i) is not None):
			circuits.append(i)
	for i in range(len(circuits)):
		circuits[i] = "./circuits/" + circuits[i]

	student_circuit_files = []
	for files in circuits:
		with open(files, "r") as circuit:
			lines = circuit.readlines()
			for line in lines:
				if(studentID in line):
					student_circuit_files.append(files)
	
	# get circuitIDs from file names
	circuitIDs = []
	for i in range(len(student_circuit_files)):
		circuitIDs.append(student_circuit_files[i][19:26:])
	print(circuitIDs)

	# get unique projectID from circuitIDs
	projectIDs = set()
	with open("maps/projects.dat", "r") as projects:
		lines = projects.readlines()
		for line in lines:
			for circuitID in circuitIDs:
				if(circuitID in line):
					projectIDs.add(line.split()[1])	
	return projectIDs

def getParticipationByProject(projectID: str) -> set:
	# get circuitIDs
	circuitIDs = set()
	with open("maps/projects.dat", "r") as projects:
		lines = projects.readlines()
		for line in lines:
			if(projectID in line):
				circuitIDs.add(line.split()[0])

	# if project id does not exist raise value error
	if(len(circuitIDs) == 0): 
		raise ValueError("Project ID does not exist.")

	# get student's ID
	circuits = []
	for i in os.listdir("./circuits/"):
		if(re.search("circuit", i) is not None):
			circuits.append(i)
	for i in range(len(circuits)):
		circuits[i] = "./circuits/" + circuits[i]

	studentIDs = set()
	for files in circuits:
		with open(files, "r") as circuit:
			lines = circuit.readlines()
			for line in lines:
				if(re.search("\d+-\d+", line) is not None):
					studentIDs.add(line[0:11:]) #[0:11:] gets rid of newline character
	
	# get student names from studentIDs
	student_names = set()
	with open("maps/students.dat", "r") as students:
			lines = students.readlines()
			for line in lines:
				for ID in studentIDs:
					if(ID in line):
						student_names.add(line.split()[0]+" "+line.split()[1])
	return student_names

def getCostOfProjects() -> dict:
	# get all projectIDs and use them as keys for dict
	projectID_to_circuits = {}
	with open("maps/projects.dat", "r") as projects:
		lines = projects.readlines()
		for line in lines:
			if(re.search("\d+-\d-\d+", line) is not None):
				projectID_to_circuits[line.split()[1]] = []

	# get all project IDs as a list as values for dict
	with open("maps/projects.dat", "r") as projects:
		lines = projects.readlines()
		for line in lines:
			for key in projectID_to_circuits.keys():
				if(key in line):
					projectID_to_circuits[line.split()[1]].append(line.split()[0])

	# get circuits for each project ID
	# convert to circuit file names
	for key in projectID_to_circuits.keys():
		circuit_files = []
		for circuit in projectID_to_circuits[key]:
			circuit_files.append("circuits/circuit_" + circuit + ".dat")
		projectID_to_circuits[key] = circuit_files
		
	# look through each circuit file and find each unique component relating to componentSymbol
	component_files = ["maps/resistors.dat", "maps/inductors.dat", "maps/capacitors.dat", "maps/transistors.dat", "maps/inductors.dat"]
	for key in projectID_to_circuits.keys():
		grand_total = 0.00
		for component_file in component_files:
			with open(component_file, "r") as component_data:
				data_lines = component_data.readlines()
				for file in projectID_to_circuits[key]:
					with open(file, "r") as circuits:
						circuit_lines = circuits.readlines()
						for line in circuit_lines:
							for data in data_lines:
								if((line.strip() in data) and (re.search("[A-Z]", line.strip()) is not None)): # if there's a match and it is not file formatting
									grand_total += float(data.split()[1][1::])
		projectID_to_circuits[key] = round(grand_total, 2)
	return projectID_to_circuits

def getProjectByComponent(componentIDs: set) -> set:
	# get student's ID
	circuits = []
	for i in os.listdir("./circuits/"):
		if(re.search("circuit", i) is not None):
			circuits.append(i)
	for i in range(len(circuits)):
		circuits[i] = "./circuits/" + circuits[i]

	circuits_with_comp = set()
	for files in circuits:
		with open(files, "r") as circuit:
			lines = circuit.readlines()
			for line in lines:
				for componentID in componentIDs:
					if(componentID in line):
						circuits_with_comp.add(files[19:26:])

	projects_with_circuit = set()
	with open("maps/projects.dat", "r") as projects:
		lines = projects.readlines()
		for line in lines:
			for circuitID in circuits_with_comp:
				if(circuitID in line):
					projects_with_circuit.add(line.split()[1])

	return projects_with_circuit

def getCommonByProject(projectID1: str, projectID2: str) -> list:
	# get circuitIDs
	circuitIDs1 = set()
	with open("maps/projects.dat", "r") as projects:
		lines = projects.readlines()
		for line in lines:
			if(projectID1 in line):
				circuitIDs1.add(line.split()[0])

	circuitIDs2 = set()
	with open("maps/projects.dat", "r") as projects:
		lines = projects.readlines()
		for line in lines:
			if(projectID2 in line):
				circuitIDs2.add(line.split()[0])

	# if project id does not exist raise value error
	if(len(circuitIDs1) == 0): 
		raise ValueError("Project ID 1 does not exist.")
	if(len(circuitIDs2) == 0): 
		raise ValueError("Project ID 2 does not exist.")

	# convert to circuit file names
	circuit_file_names1 = []
	for ID in circuitIDs1:
		circuit_file_names1.append("circuits/circuit_"+ID+".dat")
	circuit_file_names2 = []
	for ID in circuitIDs2:
		circuit_file_names2.append("circuits/circuit_"+ID+".dat")
		
	# look through each circuit file and find each unique component relating to componentSymbol
	components1 = set()
	for file in circuit_file_names1:
		with open(file, "r") as circuits:
			circuit_lines = circuits.readlines()
			for line in circuit_lines:
				if(re.search("[A-Z]", line.strip()) is not None): # if there's a match and it is not file formatting
					components1.add(line.strip())

	components2 = set()
	for file in circuit_file_names2:
		with open(file, "r") as circuits:
			circuit_lines = circuits.readlines()
			for line in circuit_lines:
				if(re.search("[A-Z]", line.strip()) is not None): # if there's a match and it is not file formatting
					components2.add(line.strip())
	
	intersection = list(components1.intersection(components2)).sort()
	return intersection

def getCircuitByStudent(studentNames: set) -> set:
	# get student's ID
	studentIDs = set()
	for studentName in studentNames:
		with open("maps/students.dat", "r") as students:
			lines = students.readlines()
			for line in lines:
				if(studentName in line):
					studentIDs.add(line.split()[3])

	# find circuit files containing the studentID
	circuits = []
	for i in os.listdir("./circuits/"):
		if(re.search("circuit", i) is not None):
			circuits.append(i)
	for i in range(len(circuits)):
		circuits[i] = "./circuits/" + circuits[i]

	student_circuit_files = set()
	for studentID in studentIDs:
		for files in circuits:
			with open(files, "r") as circuit:
				lines = circuit.readlines()
				for line in lines:
					if(studentID in line):
						student_circuit_files.add(files)

	# if student has no circuit files raise ValueError
	if(len(student_circuit_files) == 0):
		raise ValueError("Students have not participated in any projects.")
	
	circuits = set()
	for circuit_file in student_circuit_files:
		circuits.add(circuit_file[19:26:])
		
	return circuits
	
def getCircuitByComponent(componentIDs: set) -> set:
	# get circuits with componenets
	circuits = []
	for i in os.listdir("./circuits/"):
		if(re.search("circuit", i) is not None):
			circuits.append(i)
	for i in range(len(circuits)):
		circuits[i] = "./circuits/" + circuits[i]

	circuits_with_comp = set()
	for files in circuits:
		with open(files, "r") as circuit:
			lines = circuit.readlines()
			for line in lines:
				for componentID in componentIDs:
					if(componentID in line):
						circuits_with_comp.add(files[19:26:])

	return circuits_with_comp

def getComponentReport(componentIDs: set) -> dict:
	projectIDs = set()
	with open("maps/projects.dat", "r") as projects:
		lines = projects.readlines()
		for line in lines:
			if(re.search("\d+-\d-\d+", line) is not None):
				projectIDs.add(line.split()[1])

	# get all unique circuitIDs associated with any projectID
	circuitIDs = set()
	with open("maps/projects.dat", "r") as projects:
		lines = projects.readlines()
		for line in lines:
			if(re.search("\d+", line) is not None):
				circuitIDs.add(line.split()[0])	

	# convert to circuit file names
	circuit_file_names = []
	for ID in circuitIDs:
		circuit_file_names.append("circuits/circuit_"+ID+".dat")
		
	# look through each circuit file and find count of each unique component
	comp_dict = dict()
	components = set()
	for file in circuit_file_names:
		for componentID in componentIDs:
			component_count = 0
			with open(file, "r") as circuits:
				circuit_lines = circuits.readlines()
				for line in circuit_lines:
					if(componentID in line): # if there's a match and it is not file formatting
						component_count += 1
			comp_dict[componentID] = component_count
	return comp_dict


#	This block is optional and can be used for testing.
#	We will NOT look into its content.
#################################################################
if __name__ == "__main__" :
	# Write anything here to test your code.
	#print(getComponentCountByProject("082D6241-40EE-432E-A635-65EA8AA374B6", "L"))
	#print(getComponentCountByStudent("Adams, Keith", "R"))
	#print(getParticipationByStudent("Adams, Keith"))
	#print(getParticipationByProject("082D6241-40EE-432E-A635-65EA8AA374B6"))
	#print(getCostOfProjects())
	#print(getProjectByComponent(set("RNW-027")))
	#print(getCommonByProject("082D6241-40EE-432E-A635-65EA8AA374B6", "96CC6F98-B44B-4FEB-A06B-390432C1F6EA"))
	#print(getCircuitByStudent({"Adams, Keith", "Scott, Michael"}))
	#print(getCircuitByComponent({"RNW-027", "HRK-348"}))
	print(getComponentReport({"RNW-027", "HRK-348"}))


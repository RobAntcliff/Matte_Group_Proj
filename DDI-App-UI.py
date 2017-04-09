import subprocess
import sys
import csv

from DDI.merge import *
from DDI.pmlTX import *
from DDI.pml_analysis import *
from DDI.utils import *
from DDI.parser_utils import *

commands = {}
drug_list = []
ddi = []
running = True
path = " "
mock = " "

def loadPMLFile():
	global path
	path = " "
	entered = " "
	while entered == " ":
		entered = input("\n------------------------------------------------------\n"+
				"\nTo select a PML file enter"+
				"\n  1:  if you wish to use your own PML file\n"+
				"\n  Or enter to choose from our selection of PML files"+
				"\n  2:  for Lab_Assessment.pml"+
				"\n  3:  for drugs.pml"+
				"\n  4:  for error.pml"+
				"\n  5:  for clash1.pml"+
				"\n  6:  for task.pml"+
				"\n  7:  for nodrugs.pml"+
				"\n  8:  for noname.pml"+
				"\n  9:  for spaced_drugs.pml"+
				"\n  return:  to return to main menu\n"+
				"\n\nEnter your choice here: ")
	
		if entered == "1":
			entered = input("\n------------------------------------------------------\n"+
					"\nEnter the absolute path to the PML file you wish to use or enter return to return to main menu.\n")
			if entered == "return": 
				printHelp()
				return
			else:
				path = entered
		elif entered == "2":
			path = "DDI/pmlfiles/Lab_Assessment.pml"

		elif entered == "3":
			path = "DDI/pmlfiles/drugs.pml"

		elif entered == "4":
			path = "DDI/pmlfiles/error.pml"
	
		elif entered == "5":
			path = "DDI/pmlfiles/clash1.pml"

		elif entered == "6":
			path = "DDI/pmlfiles/task.pml"

		elif entered == "7":
			path = "DDI/pmlfiles/nodrugs.pml"
		
		elif entered == "8":
			path = "DDI/pmlfiles/noname.pml"

		elif entered == "9":
			path = "DDI/pmlfiles/spaced_drugs.pml"
		
		elif entered == "return":
			print("\n    Returning to menu.\n")
			return
		else:
			print("\nUnrecognised input, if you would like to entered a customised path please enter 1\n")
			entered = " "

	initLogFile(path)
	global error_li
	error_li = run(open(path, 'r'))

	global task_list
	task_list = findTaskUsed()
	runCheck()

	global drug_list
	drug_list = getDrugs()


	all_dict = getDrugsTimeAndFrequency()
	printDTF(all_dict)

	delays = getDel()
	printDels(delays)


def printDels(dels):
	if not dels:
		print("No Delays specified in PML file")
	else:
		for key, val in dels.items():
			actNum = key 
			delay = val[0] 
			print("Delay of " + str(delay) + " -> Action " + str(key))


def printDTF(di):
	if not di:
		print("No drugs in PML file.")
	else:
		for i in di:
			x = di[i]
			print("Drug found in PML file -> " + str(x))

def printTasks():
	if not task_list:
		print("Task construct not used in PML file.")
	else:
		print("Task construct is now deprecated, please use Sequence in its place.")
		if len(task_list) > 1:
			print("Task was used at lines ")
			for i in task_list:
				print([i][1]) 
				print(" ")
		else:
			print("Task was used at line " + str(task_list[0][1]) + ".")

def printDelays(list):
    for i in list:
    	print ("Delay found in PML file -> " + i)


def printDrugsFrequencyAndTime():
	if not all_list:
		print("\nNo drugs in PML File\n")
	elif len(all_list) == 1:
		print("\nDrug found in PML File -> " + all_list[0])
	else: 
		print("\n")
		for i in range(len(all_list)):
			print("Drug found in PML File -> " + all_list[i])

def printTime():
	if not time_list:
		print("\nNo time in PML File\n")
	elif len(drug_list) == 1:
		print("\nTime found in PML File -> " + time_list[0])
	else: 
		print("\n")
		for i in range(len(time_list)):
			print("Time found in PML File -> " + time_list[i])

def printFreq():
	if not freq_list:
		print("\nNo freq in PML File\n")
	elif len(drug_list) == 1:
		print("\nfreq found in PML File -> " + freq_list[0])
	else: 
		print("\n")
		for i in range(len(freq_list)):
			print("Freq found in PML File -> " + freq_list[i])

def printErrors():
	if not error_li:
		print("\nFile parsed.")
	elif len(error_li) == 1:
		print("\nError Report :: " + str(error_li[0]))
	else:
		print("\n")
		for i in range(len(error_li)):
			print("Error Report :: " + str(error_li[i])+"\n")
	
def loadMock():
	global mock
	mockread = " "
	usr_input = " "

	while usr_input == " ":
		usr_input = input("\nTo select a mock DINTO file.\n\nEnter:"+
				  "\n  1:  if you wish to use your own mock DINTO file"+
				  "\n\nOr enter to choose from our selection of mock DINTO files"+
				  "\n  2:  for DDI.csv"+
				  "\n  return:  to return to main menu\n"+
				  "\n\nEnter your choice here: ")

		if usr_input == "1":
			entered = input("\n------------------------------------------------------\n"+
					"\nEnter the path to the PML file you wish to use or enter return to return to main menu.\n")

			if entered == "return": 
				printHelp()
				return
			else:
				mock = entered

		elif usr_input == "return":
			printHelp()
			return

		elif usr_input == "2":
			mock = "DDI/mockfiles/DDI.csv"		
	
		else:
			print("\nUnrecognised input, if you would like to entered a customised path please enter 1\n")
			entered = " "
	
	print("\n    You have selected " + str(mock) + "\n")
	
	mockread = "\nBelow are the contents of " + str(mock) + "\n     -- Drug 1 - Drug 2 - DDI Type - Time - Unit --\n"
	with open(mock) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			mockread += str("        " + row['Drug 1'] + " - " + row['Drug 2'] + " - " + row['DDI Type'] + " - " + row['Time'] +  " - " + row['Unit'] + "\n")
		
		initLogFile(mock)
		updateLogFile(mock, mockread)
		print(mockread)

def runCheck():
	global path

	if path == " ":
		print("\n    WARNING: No PML file has been selected. Please load a file and try again\n")
		printHelp
		return
	else:
		print("\n    The PML file " +str(path) + " is being checked.\n"+
		      "\nCheck performed. Report is as follows:\n")
		updateLogFile(path, "\nCheck performed. Report is as follows:\n")
		printErrors()
		findConsClash()
		printTasks()
		savePMLFile(getFileName(path)[:-4]+"_backup", open(path, 'r').read())
		print("\nA backup version of the selected file has been saved in the New_Pathways folder:\n"+
		      "    Matte_Group_Proj -> New_Pathways -> your_file_backup.pml\n")

def ddiCheck():
	global mock
	global path
	global ddi
	i = 0

	mockread = ""

	if mock == " ":
		print("\n    WARNING: No mock DINTO file has been selected. Please load a file and try again\n")
		return
	elif path == " ":
		print("\n    WARNING: No PML file has been selected. Please load a file and try again\n")
		return
	else: 
		if(len(drug_list) > 1):
			for x in drug_list:
				with open(mock) as csvfile:
					reader = csv.DictReader(csvfile)
					for row in reader:	
						if(row['Drug 1'] == x):
							for y in drug_list:
								if(y != x):
									if(row['Drug 2'] == y):
										ddi += [(x, y, row['DDI Type'], row['Time'], row['Unit'])]		

		elif (len(drug_list) == 1):
			print("\nThere is only one drug in the PML file, no need to check for any drug interactions\n")
			return
		else:
			print("\nThere is no drugs in the PML file.\n")
			return

	if(len(ddi) != 0):
		print("\n    Here are all the DDIs that were identified:\n")
		for x in ddi:
			print("\n    Here: {0}".format(x))
	else:
		print("\n    There are no DDIs in this PMLs.\n")
	#updateLogFile(mock, ddi)

def checkMergeFile(the_file):
	global error_li
	error_li = run(open(the_file, 'r'))

	global task_list
	task_list = findTaskUsed()
	printErrors()
	findConsClash()
	printTasks()

	if not error_li:
		print("\n\nErrors discovered in file, returning to main menu.\nPlease fix the errors before retrying or enter a valid PML file.")
	

def mergePML():
	usr_input = input("\n------------------------------------------------------\n"+
			  "\n\nPlease make a choice from the options below by entering the number beside it:"+
			  "\n\n       1: Merge the drugs.pml file and the branch.pml file"+
			  "\n       2: Merge two valid files of your choosing, if errors are present please cancel and try again"+
			  "\n       3: Cancel this action"+
			  "\n\nEnter your choice: ")
	if usr_input == "1":
		merge("DDI/pmlfiles/drugs.pml", "DDI/pmlfiles/branch.pml")
	elif usr_input == "2":
		file_one = input("\n\n------------------------------------------------------\n"+
				 "\nPlease enter the absolute path to the first file or cancel to exit: ")
		if file_one == "cancel":
			return
		checkMergeFile(file_one)

		file_two = input("\n\nPlease enter the absolute path to the second file: ")

		if file_two == "cancel":
			return
		checkMergeFile(file_two)		
		cont = input("\n\nIf no errors have been found simply press Enter to merge the files.\nOr type \'cancel\' to return to main menu.\n\nContinue?")
		if cont == "cancel":
			return
		merge(file_one, file_two)

def loadOwl():
	loadDinto = 'DDI/loadDINTOClass.py'
	subprocess.call(['python',loadDinto])

def exitApplication():
	global running
	running = False

def printHelp():
	print(  "\n------------------------------------------------------\n"+
		"\nTo run a command enter"+
		"\n  help:           to display this list of commands at any time"+
		"\n  load pml:       to load a PML file to be worked with"+
		"\n  merge pathways: to select two pml files t merge into  a single pathway"+
		"\n  load owl:       to load an OWL ontology and find a specific class within it"+
		"\n  load mock:      to load a mock DINTO file to be used to identify DDIs"+
		"\n  check ddi:      to search the loaded mock DINTO file for any DDIs related to drugs from the loaded PML file"+
		"\n  quit:           to close the application\n")


def printErr(err):
	print("The following errors were found:\n\n"+err)

commands = {"help"         : printHelp,
            "load owl"	   : loadOwl,
            "quit"         : exitApplication,
	    	"load pml"     : loadPMLFile,
		"load mock" : loadMock,
		"check ddi" : ddiCheck,
		"merge pathways" : mergePML
	    	}
print("\n\n------------------------------------------------------\n"+
      "\nApplication started, see available commands below:")
printHelp()
while running:
	usr_command = input("\n------------------------------------------------------\n"+"\nPlease enter a command: ")
	if usr_command in commands:
		commands[usr_command]()
	else:
		print("\nCommand not found.\n\nPlease enter a valid command from the list below.\n")
		printHelp()

import subprocess
import sys
import csv

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
				"\n  6:  for branch.pml"+
				"\n  7:  for nodrugs.pml"+
				"\n  8:  for noname.pml"+
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
			path = "DDI/pmlfiles/branch.pml"

		elif entered == "7":
			path = "DDI/pmlfiles/nodrugs.pml"
		
		elif entered == "8":
			path = "DDI/pmlfiles/noname.pml"
		
		elif entered == "return":
			print("\n    Returning to menu.\n")
			return
		else:
			print("\nUnrecognised input, if you would like to entered a customised path please enter 1\n")
			entered = " "

	initLogFile(path)
	drugLi = run(open(path, 'r'))
	runCheck()

	global drug_list
	drug_list = getDrugs()
	print(drug_list)
	

def loadMock():
	global mock
	usr_input = " "

	while usr_input == " ":
		usr_input = input("\nTo select a mock DINTO file ente"+
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
	initLogFile(mock)

def runCheck():
	global path

	if path == " ":
		print("\n    WARNING: No PML file has been selected. Please load a file and try again\n")
		printHelp
		return
	else:
		try:
			#pml_check = 'DDI/Check/pmlcheck'
			#check_results = subprocess.check_output([pml_check, path])
			check_results_str = "TODO: Errors & Warnings should go here" #check_results.decode("utf-8")
			print("\n    The PML file " +str(path) + " is being checked.\n")
			findTaskUsed()
			findConsClash()
			updateLogFile(path, "\nCheck performed. Report is as follows.\n")

		except subprocess.CalledProcessError as e:
			check_results_str = "\nCheck performed: The following errors were found in the selected PML file: Invalid Syntax\n"+e.output
		updateLogFile(path, check_results_str)

def ddiCheck():
	global mock
	global path
	global ddi
	i = 0

	mockread = "The mock will now be displayed below in the form:\n     -- Drug 1 - Drug 2 - DDI Type - Time - Unit -- \nBelow are the contents of your chosen mock DDI file:\n"

	if mock == " ":
		print("\n    WARNING: No mock DINTO file has been selected. Please load a file and try again\n")
		return
	elif path == " ":
		print("\n    WARNING: No PML file has been selected. Please load a file and try again\n")
		return
	else: 
		with open(mock) as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				mockread += str("        " + row['Drug 1'] + " - " + row['Drug 2'] + " - " + row['DDI Type'] + " - " + row['Time'] +  " - " + row['Unit'] + "\n")
		
		updateLogFile(mock, mockread)

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


def loadOwl():
	loadDinto = 'DDI/loadDINTOClass.py'
	subprocess.call(['python',loadDinto])

def exitApplication():
	global running
	running = False

def printHelp():
	print(  "\n------------------------------------------------------\n"+
		"\nTo run a command enter"+
		"\n  help:  to display this list of commands at any time"+
		"\n  load pml:  to load a PML file to be worked with"+
		"\n  load owl:  to load an OWL ontology and find a specific class within it"+
		"\n  load mock:  to load a mock DINTO file to be used to identify DDIs"+
		"\n  ddi check:  to search the loaded mock DINTO file for any DDIs related to drugs from the loaded PML file"+
		"\n  quit:  to close the application\n")


def printErr(err):
	print("The following errors were found:\n\n"+err)

commands = {"help"         : printHelp,
            "load owl"	   : loadOwl,
            "quit"         : exitApplication,
	    	"load pml"     : loadPMLFile,
		"load mock" : loadMock,
		"ddi check" : ddiCheck
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

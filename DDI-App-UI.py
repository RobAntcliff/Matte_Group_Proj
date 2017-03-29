import subprocess
import sys
import csv

from DDI.pml_analysis import *
from DDI.utils import *
from DDI.parser_utils import *

commands = {}
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
				"\n  5:  for nodrugs.pml"+
				"\n  6:  for branch.pml"+
				"\n  7:  for clash1.pml"+
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
			path = "DDI/pmlfiles/nodrugs.pml"

		elif entered == "6":
			path = "DDI/pmlfiles/branch.pml"

		elif entered == "7":
			path = "DDI/pmlfiles/clash1.pml"
		
		elif entered == "8":
			path = "DDI/pmlfiles/nonames.pml"
		
		elif entered == "return":
			print("\n    Returning to menu.\n")
			return
		else:
			print("\nUnrecognised input, if you would like to entered a customised path please enter 1\n")
			entered = " "

	initLogFile(path)
	run(open(path, 'r'))
	runCheck()
	

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
			pml_check = 'DDI/Check/pmlcheck'
			check_results = subprocess.check_output([pml_check, path])
			check_results_str = check_results.decode("utf-8")
			print("\n    The PML file " +str(path) + " is being checked.\n")
			findTaskUsed()
			findUnnamedC()
			findConsClash()
			updateLogFile(path, "\nCheck performed. Report is as follows.\n")

		except subprocess.CalledProcessError as e:
			check_results_str = "\nCheck performed: The following errors were found in the selected PML file: Invalid Syntax\n"+e.output
		updateLogFile(path, check_results_str)

def readMock():
	global mock
	mockread = ""
	if mock == " ":
		print("\n    WARNING: No mock DINTO file has been selected. Please load a file and try again\n")
		return

	else:
		print("\nThe mock will now be displayed below in the form:\n"+
                      "\n    -- Drug 1 - Drug 2 - DDI Type - Time - Unit -- \n"+
                      "\nBelow are the contents of your chosen mock DDI file:\n")
		with open(mock) as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				mockread += str("     " + row['Drug 1'] + " - " + row['Drug 2'] + " - " + row['DDI Type'] + " - " + row['Time'] +  " - " + row['Unit'] + "\n")
	
	print(mockread)
	updateLogFile(mock, mockread)


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
		"\n  read mock:  to read the loaded mock DINTO file"+
		"\n  quit:  to close the application\n")


def printErr(err):
	print("The following errors were found:\n\n"+err)

commands = {"help"         : printHelp,
            "load owl"	   : loadOwl,
            "quit"         : exitApplication,
	    	"load pml"     : loadPMLFile,
		"load mock" : loadMock,
		"read mock" : readMock
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

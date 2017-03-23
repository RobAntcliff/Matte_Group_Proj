import subprocess
from DDI_App.pml_analysis import runParser
#import DDI_App.loadDINTOClass
from DDI_App.logGen import *

commands = {}
running = True
path = " "

def runParse():
	if path == " ":
		print("\nNo PML file has been selected.\nPlease enter the \'load PML\' command.")
	else:
		runParser(open(path, 'r'))

def findDrugs():
	if path == " ":
                print("\nNo PML file has been selected.\nPlease enter the \'load PML\' command.")
	else:
		run(open(path, 'r'))

def loadPMLFile():
	global path
	path = " "
	while path == " ":
		usr_input = input("\nNow choose a file to load using the options below:"+
				  "\n\nEnter 1 for a test file with drugs"+
				  "\nEnter 2 for a test file without drugs"+
				  "\nEnter 3 for a test file with errors"+
				  "\nEnter the path to the relevant file in the form path/to/file.pml\n"+

				  "\nEnter cancel to cancel this action"+
				  "\n\nEnter your choice here: ")
		if usr_input == "1":
			path = 'DDI_App/pmlfiles/drugs.pml'
		elif usr_input == "2":
			path = 'DDI_App/pmlfiles/nodrugs.pml'
		elif usr_input == "3":
			path = 'DDI_App/pmlfiles/error2.pml'
		elif usr_input == "cancel":
			return
		else:
			path = usr_input
	split_path = path.split("/")
	initLogFile(split_path[len(split_path)-1], path)

def runCheck():
	global path
	if path == " ":
		print("\nNo PML file has been selected.\nPlease enter the \'loadPML\' command.")
	else:
		#check_results = subprocess.check_output(pml_check)
		#check_results_str = check_results.decode("utf-8")
		check_results_str = runParser(open(path, 'r'))

		if check_results_str != "No errors found":
			check_results_str = "The following errors were found while checking the selected PML file:\n\n"+check_results_str

		updateLogFile(path, check_results_str)
		print(check_results_str)

def loadOwl():
	print("hello")
	#runLoadSeq()

def exitApplication():
	global running
	running = False

def printHelp():
	print(
	"\n\n----------------------------------------------------------"+
	"\nhelp:       Display this list of commands"+
	"\nloadPML:   Load a PML file to be worked with"+
	"\ncheckPML:  Check a loaded PML file for errors"+
	"\nloadOWL:   Load an owl onthology and search it for a class"+
	"\nquit:       Close the application"+
	"\n----------------------------------------------------------\n\n")

commands = {"help"      : printHelp,
            "checkPML" : runCheck,
            "loadOWL"	: loadOwl,
            "quit"      : exitApplication,
	    "loadPML"  : loadPMLFile
	   }
print("\nApplication started, see available commands below:")
printHelp()
while running:
	usr_command = input("\n----------------------------------------------------------\n"+
			    "\nPlease enter a command: ")
	if usr_command in commands:
		commands[usr_command]()
	else:
		print("Command not found.\nPlease enter a valid command from the list below.")
		printHelp()

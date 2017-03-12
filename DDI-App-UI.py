import subprocess
import time
from pml_analysis import *

commands = {}
running = True
path = " "
timestr = time.strftime("%Y-%m-%d-%H-%M-%S")

def findDrugs():
	f = open('pmlfiles/drugs.pml', 'r')
	run(f)

def loadPMLFile():
	global path
	path = input("Choose an option :\n Enter 1 for Lab_Assessment.pml \n Enter 2 for drugs.pml \n Enter 3 for error.pml \n Enter 4 for nodrugs.pml \n")

def runCheck():
	global path
	if path == " ":
		print("No PML file has been selected.\nPlease enter the \'select\' command.")
	else:
		with open('DDI-App/log_folder/test' + timestr + '.log', 'w') as f:
			if path == "1":
				path = "DDI-App/Lab_Assessment.pml"
			if path == "2":
				path = "pmlfiles/drugs.pml"
			if path == "3":
				path = "pmlfiles/error.pml"
			if path == "4":
				path = "pmlfiles/nodrugs.pml"
			try:
				pml_check = 'DDI-App/Check/pmlcheck'
				check_results = subprocess.check_output([pml_check, path])
				check_results_str = check_results.decode("utf-8")
				#str(check_results, 'utf-8')
			except subprocess.CalledProcessError as e:
				check_results_str = "The following errors were found in the selected PML file: Invalid Syntax"
			f.write(check_results_str)
			#print(check_results_str)

def loadOwl():
	loadDinto = 'DDI-App/loadDINTOClass.py'
	subprocess.call(['python',loadDinto])

def exitApplication():
	global running
	running = False

def printHelp():
	print("help: Display this list of commands\nload PML:  Load a PML file to be worked with\ncheck PML: Check a loaded PML file for errors\nload OWL: Load an owl onthology and search it for a class\nfind drugs: Find drugs in PML file\nquit: Close the application")

commands = {"help"      : printHelp,
            "check PML" : runCheck,
            "load OWL"	: loadOwl,
            "quit"      : exitApplication,
	    	"load PML"  : loadPMLFile,
	    	"find drugs": findDrugs
	    	}
print("Application started, see available commands below:")
printHelp()
while running:
	usr_command = input("Please enter a command: ")
	if usr_command in commands:
		commands[usr_command]()
	else:
		print("Command not found.\nPlease enter a valid command from the list below.")
		printHelp()

import subprocess
import time
import utils
from pml_analysis import *

commands = {}
running = True
path = " "
timestr = time.strftime("%Y-%m-%d-%H-%M-%S")

def findTask():
	usr_input = input("Enter 1 or 2 to run on a particular file. Press 0 to return to main menu: ")
	if usr_input == "1":
		f = open('pmlfiles/branch.pml', 'r')
		out = findTaskUsed(f)
		findTask()
	elif usr_input == "2":
		f = open('pmlfiles/clash1.pml', 'r')
		out = findTaskUsed(f)
		findTask()
	elif usr_input == "0":
		return
	else:
		findTask()

def findClash():
	usr_input = input("Enter 1 or 2 to run on a particular file. Press 0 to return to main menu: ")
	if usr_input == "1":
		f = open('pmlfiles/clash1.pml', 'r')
		out = findConsClash(f)
		findClash()
	elif usr_input == "2":
		f = open('pmlfiles/clash1.pml', 'r')
		out = findConsClash(f)
		findClash()
	elif usr_input == "0":
		return
	else:
		findClash()

def findUnnamed():
	usr_input = input("Enter 1 or 2 to run on a particular file. Press 0 to return to main menu: ")
	if usr_input == "1":
		f = open('pmlfiles/drugs.pml', 'r')
		out = findUnnamedC(f)
		printErr()
		findUnnamed()
	elif usr_input == "2":
		f = open('pmlfiles/noname.pml', 'r')
		out = findUnnamedC(f)
		printErr()
		findUnnamed()
	elif usr_input == "0":
		return
	else:
		findUnnamed()

def findDrugs():
	usr_input = input("Enter 1 or 2 to run on a particular file. Press 0 to return to main menu: ")
	if usr_input == "1":
		f = open('pmlfiles/drugs.pml', 'r')
		run(f)
		findDrugs()
	elif usr_input == "2":
		f = open('pmlfiles/nodrugs.pml', 'r')
		run(f)
		findDrugs()
	elif usr_input == "0":
		return
	else:
		findDrugs()

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
	print("help: Display this list of commands\nload PML:  Load a PML file to be worked with\ncheck PML: Check a loaded PML file for errors\nload OWL: Load an owl onthology and search it for a class\nfind drugs: Find drugs in PML file\nfind task: Check PML file to see if deprecated Task construct is used\nfind clash: Analyses PML file and checks for construct name clash\nfind unnamed: Scan the file for errors\nquit: Close the application")

def printErr():
	print("No errors in PML file")

commands = {"help"         : printHelp,
            "check PML"    : runCheck,
            "load OWL"	   : loadOwl,
            "quit"         : exitApplication,
	    	"load PML"     : loadPMLFile,
	    	"find drugs"   : findDrugs,
	    	"find clash"   : findClash,
	    	"find task"    : findTask,
	    	"find unnamed" : findUnnamed
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

import subprocess
import time
import utils
from pml_analysis import *

commands = {}
running = True
path = " "

datestr = time.strftime("%Y-%m-%d")
timestr = time.strftime("%H:%M:%S")

logfile = open('log_folder/PML/'+ timestr + '_' + datestr + '.log', 'w')

def findTask():
	global path

	if path == " ":
		print("\n    WARNING: No PML file has been selected. Please load a file and try again.\n")
		printHelp()
		return
		
	else:
		f = open(path, 'r')
		out = findTaskUsed(f)
	
	printHelp()
	return

def findClash():
	global path

	if path == " ":
		print("\n    WARNING: No PML file has been selected. Please load a file and try again.\n")
		printHelp()
		return
		
	else:
		f = open(path, 'r')
		out = findConsClash(f)
	
	printHelp()
	return
		
def findUnnamed():
	global path

	if path == " ":
		print("\n    WARNING: No PML file has been selected. Please load a file and try again.\n")
		printHelp()
		return
		
	else:
		f = open(path, 'r')
		out = findUnnamedC(f)
		printErr()
	
	printHelp()
	return


def findDrugs():
	global path
	if path == " ":
		print("\n   WARNING: No PML file has been selected. Please load a file and try again.\n")

	else:
		fn = open(path, 'r')
		run(fn)
	
	printHelp()
	return

def loadPMLFile():
	global path

	entered = input("\nTo select a PML file enter \n  1:  if you wish to use your own PML file\nOr enter to choose from our selection of PML files\n  2:  for Lab_Assessment.pml \n  3:  for drugs.pml \n  4:  for error.pml \n  5:  for nodrugs.pml\n  6:  for branch.pml\n  7:  for clash1.pml\n  return:  to return to main menu\n")
	
	if entered == "1":
		entered = input("\nEnter the path to the PML file you wish to use or enter return to return to main menu.\n")
		if entered == "return": 
			printHelp()
			return
		else:
			path = entered
	elif entered == "2":
		path = "pmlfiles/Lab_Assessment.pml"

	elif entered == "3":
		path = "pmlfiles/drugs.pml"

	elif entered == "4":
		path = "pmlfiles/error.pml"
	
	elif entered == "5":
		path = "pmlfiles/nodrugs.pml"

	elif entered == "6":
		path = "pmlfiles/branch.pml"

	elif entered == "7":
		path = "pmlfiles/clash1.pml"

	elif entered == "return":
		print("\n    Returning to menu.\n")
		printHelp()
		return
	else:
		loadPMLFile()
	print("\n    You have selected " + str(path) + "\n")
	logfile.write(str(path) + "loaded. \n")	

	printHelp()
	return

def runCheck():
	global path
	global logfile

	if path == " ":
		print("\n    WARNING: No PML file has been selected. Please load a file and try again\n")
		printHelp
		return
	else:
		try:
			pml_check = 'DDI/Check/pmlcheck'
			check_results = subprocess.check_output([pml_check, path])
			check_results_str = check_results.decode("utf-8")
			print("    The PML file " +str(path) + " has been checked, and has no errors\n")
			logfile.write("\nCheck performed. No errors found\n")
			#str(check_results, 'utf-8')

		except subprocess.CalledProcessError as e:
			check_results_str = "\nCheck performed: The following errors were found in the selected PML file: Invalid Syntax\n"
		logfile.write(check_results_str)
		#print(check_results_str)

def loadOwl():
	loadDinto = 'DDI/loadDINTOClass.py'
	subprocess.call(['python',loadDinto])

def exitApplication():
	global running
	running = False

def printHelp():
	print("\nTo run a command enter \n  help:  to display this list of commands at any time\n  load pml:  to load a PML file to be worked with\n  check pml:  to check a loaded PML file for errors\n  find drugs:  to search for drugs in a loaded PML file\n  find task:  Check PML file to see if deprecated Task construct is used\n  find clash:  Analyses PML file and checks for construct name clash\n  find unnamed:  Scan the file for errors\n  load owl:  to load an OWL ontology\n  quit:  to close the application\n")


def printErr():
	print("No errors in PML file")

commands = {"help"         : printHelp,
            "check pml"    : runCheck,
            "load owl"	   : loadOwl,
            "quit"         : exitApplication,
	    	"load pml"     : loadPMLFile,
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
		print("\nCommand not found.\nPlease enter a valid command from the list below.\n")
		printHelp()

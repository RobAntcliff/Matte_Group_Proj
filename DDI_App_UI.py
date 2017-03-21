import subprocess
import DDI_App.pml_analysis
import DDI_App.loadDINTOClass
import DDI_App.logGen

commands = {}
logs = {}
running = True
path = " "

def runParse():
	if path == " ":
		print("No PML file has been selected.\nPlease enter the \'load PML\' command.")
	else:
		runParser(open(path, 'r'))

def findDrugs():
	if path == " ":
                print("No PML file has been selected.\nPlease enter the \'load PML\' command.")
	else:
		run(open(path, 'r'))

def loadPMLFile():
	path = " "
	while path == " ":
		usr_input = input("Enter 1 for file with drugs, Enter 2 for file without drugs: ")
		if usr_input == "1":
			path = 'DDI_App/pmlfiles/drugs.pml'
		elif usr_input == "2":
			path = 'DDI_App/pmlfiles/nodrugs.pml'
		else:
			print("Invalid file choice.\nEnter a valid option from the choices below to continue")
	split_path = path.split("/")
	initLogFile(splitPath[len(split_path)-1])

def runCheck():
	global path
	if path == " ":
		print("No PML file has been selected.\nPlease enter the \'load PML\' command.")
	else:
		try:
			pml_check = 'DDI_App/Check/pmlcheck'
			check_results = subprocess.check_output([pml_check, path])
			check_results_str = check_results.decode("utf-8")
		except subprocess.CalledProcessError as e:
			check_results_str = "The following errors were while checking the selected PML file:"
		updateLogFile(path, check_results_str)
		#print(check_results_str)

def loadOwl():
	runLoadSeq()

def exitApplication():
	global running
	running = False

def printHelp():
	print("help: Display this list of commands"+
	"\nload PML:  Load a PML file to be worked with"+
	"\ncheck PML: Check a loaded PML file for errors"+
	"\nload OWL: Load an owl onthology and search it for a class"+
	"\nfind drugs: Find drugs in PML file"+
	"\nrun parse: Scan the file for errors"+
	"\nquit: Close the application")

commands = {"help"      : printHelp,
            "check PML" : runCheck,
            "load OWL"	: loadOwl,
            "quit"      : exitApplication,
	    "load PML"  : loadPMLFile,
	    "find drugs": findDrugs,
	    "run parse" : runParse
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

import subprocess
import time

commands = {}
running = True
path = " "
timestr = time.strftime("%Y-%m-%d-%H-%M-%S")

def loadPMLFile():
	global path
	path = input("Choose an option or enter absolute path to the PML file:\n 1: DDI-App/Lab_Assessment.pml \n")

def runCheck():
	global path
	if path == " ":
		print("No PML file has been selected.\nPlease enter the \'select\' command.")
	else:
		with open('DDI-App/log_folder/test' + timestr + '.log', 'w') as f:
			if path == "1":
				path = "DDI-App/Lab_Assessment.pml"
			try:
				pml_check = 'DDI-App/Check/pmlcheck'
				check_results = subprocess.check_output([pml_check, path])
				#str(check_results, 'utf-8')
			except subprocess.CalledProcessError as e:
				check_results = "The following errors were found in the selected PML file:" + e.output.decode("utf-8")
			check_results_str = check_results.decode("utf-8")
			f.write(check_results_str)
			#print(check_results_str)
def loadOwl():
	loadDinto = 'DDI-App/loadDINTOClass.py'
	subprocess.call(['python',loadDinto])

def exitApplication():
	global running
	running = False

def printHelp():
	print("help:      Display this list of commands\nload PML:  Load a PML file to be worked with\ncheck PML: Check a loaded PML file for errors\nload Owl: Load an owl onthology and search it for a class\nexit:      Close the application")

commands = {"help"      : printHelp,
            "check PML" : runCheck,
            "load Owl"	: loadOwl,
            "exit"      : exitApplication,
	    "load PML"  : loadPMLFile,}
print("Application started, see available commands below:")
printHelp()
while running:
	usr_command = input("Please enter a command: ")
	if usr_command in commands:
		commands[usr_command]()
	else:
		print("Command not found.\nPlease enter a valid command from the list below.")
		printHelp()

import subprocess

commands = {}
running = True
path = " "

def loadPMLFile():
	global path
	path = input("Please enter absolute path to the PML file:\n")

def runCheck():
	global path
	if path == " ":
		print("No PML file has been selected.\nPlease enter the \'select\' command.")
	else:
		try:
			pml_check = 'Check/pmlcheck'
			check_results = subprocess.check_output([pml_check, path])
			#str(check_results, 'utf-8')
		except subprocess.CalledProcessError as e:
			check_results = "The following errors were found in the selected PML file:" + e.output
		print(check_results)

def exitApplication():
	global running
	running = False

def printHelp():
	print("help:      Display this list of commands\nload PML:  Load a PML file to be worked with\ncheck PML: Check a loaded PML file for errors\nexit:      Close the application")

commands = {"help"      : printHelp,
            "check PML" : runCheck,
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

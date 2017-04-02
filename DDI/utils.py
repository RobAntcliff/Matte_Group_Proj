import time
from DDI.pml_analysis import *

logs = {}

def getLogLocation(path):
	path_length = len(path)
	fileType = path[path_length-3:path_length]
	logLocation = ""
	if fileType == "csv":
		return "MOCK/"
	elif fileType == "owl":
		return "DINTO/"
	elif fileType == "pml":
		return "PML/"

def getFileName(path):
	path_split = path.split('/')
	name = path_split[len(path_split)-1]
	return name

def replaceNewLineWithTimestamp(content, timestamp):
	content_list = content.split('\n')
	new_content = ""
	for line in content_list:
		new_content += "\n"+timestamp+": " + line
	return new_content

def initLogFile(path):
	fileName = getFileName(path)
	current_time = time.strftime("%Y-%m-%d-%H-%M-%S")
	logFileName = fileName[:-4] + '_' + current_time + '.log'

	with open('DDI/log_folder/'+getLogLocation(fileName) + logFileName, 'w') as f:
		f.write(current_time + ': ' + fileName + ' was selected for use.\n')
	logs[path] = logFileName

def updateLogFile(filePath, entry):
	fileName = logs[filePath]

	with open('DDI/log_folder/'+ getLogLocation(filePath) + fileName, 'a') as f:
		f.write(replaceNewLineWithTimestamp(entry, time.strftime("%Y-%m-%d-%H-%M-%S")))

def findTask(path):
        if path == " ":
                print("\n    WARNING: No PML file has been selected. Please load a file and try again.\n")

        else:
                f = open(path, 'r')
                findTaskUsed(f)

def findClash(path):
        if path == " ":
                print("\n    WARNING: No PML file has been selected. Please load a file and try again.\n")

        else:
                f = open(path, 'r')
                findConsClash(f)

def findUnnamed(path):
        if path == " ":
                print("\n    WARNING: No PML file has been selected. Please load a file and try again.\n")

        else:
                f = open(path, 'r')
                findUnnamedC(f)


def findDrugs(path):
        if path == " ":
                print("\n   WARNING: No PML file has been selected. Please load a file and try again.\n")

        else:
                fn = open(path, 'r')
                run(fn)


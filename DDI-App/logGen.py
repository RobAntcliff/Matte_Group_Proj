import subprocess
import sys

def generateLogFile():
	with open('log_folder/test.log', 'w') as f:
	    process = subprocess.Popen(['Check/pmlcheck', '../peos-master/compiler/models/eggs.pml'], stdout=subprocess.PIPE)
	    for c in iter(lambda: process.stdout.read(1), ''):
	        f.write(c)



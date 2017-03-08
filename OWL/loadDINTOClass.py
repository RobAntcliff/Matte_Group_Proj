import ontospy
import datetime

logfile = open("loadOntologyLog.txt","w+")

def getTime():
	now = datetime.datetime.now()
	time = "%s/%s/%s at %s:%s:%s" % (now.day,now.month,now.year, now.hour, now.minute, now.second) 
	return time

def getClasses():
	model = ontospy.Ontospy("DINTO/DINTO1.2/DINTO 1.2 additional material/DINTO 1.2 subsets/OAE_DINTO_subset.owl")
	classList = model.classes
	now = datetime.datetime.now()
	output = ("%s :: Classes loaded from model OAE_DINTO_subset.owl \n" %(getTime()))
	logfile.write(output)
	return classList

def findClass(className):
	classList = getClasses()
	length = len(classList)
	found = False
	i = 0
	output = ("%s :: Searching for class %s \n" % (getTime(),className))
	logfile.write(output)
	while found != True and i < length:
		classDets = classList[i].serialize()
		if className in classDets:
			output = ("%s :: Found class %s \n" %(getTime(),className))
			logfile.write(output)
			print classDets
			output = ("%s :: Printing class details to console \n" %(getTime()))
			logfile.write(output)
			found = True
		i = i + 1
	if found == False:
		output = ("%s :: Did not find class %s \n" %(getTime()))
		logfile.write(output)

className = raw_input("What class do you want to find:")
output = ("%s :: User selected finding class %s \n" %(getTime(),className))
logfile.write(output)
findClass(className)
output = ("%s :: Exiting application \n" %(getTime()))
logfile.write(output)
logfile.close()



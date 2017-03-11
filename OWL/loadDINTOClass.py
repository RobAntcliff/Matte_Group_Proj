import ontospy
import datetime
import rdflib

logfile = open("loadDINTOLog.log","w+")

def getTime():
	now = datetime.datetime.now()
	time = "%s/%s/%s at %s:%s:%s" % (now.day,now.month,now.year, now.hour, now.minute, now.second) 
	return time
	
def getClasses(owl):
	model = ontospy.Ontospy(owl)
	classList = model.classes
	now = datetime.datetime.now()
	output = ("%s :: Classes loaded from model at %s \n" %(getTime(),owl))
	logfile.write(output)
	return classList

def printDetails(currentClass):
	output = ["Label: ", "Description: ", "Alternate Term: ", "Definition Source: ", "SubClass of: ", "Term Editor: ", "See Also:", "Type: "]
	for x in currentClass.triples:
		if "#label" in unicode(x[1]):
			output[0] = output[0] + unicode(x[2])
		elif "IAO_0000115" in unicode(x[1]):
			output[1] = output[1] + unicode(x[2])
		elif "IAO_0000118" in unicode(x[1]):
			output[2] = output[2] + unicode(x[2])
		elif "IAO_0000119" in unicode(x[1]):
			output[3] = output[3] + unicode(x[2])
		elif "#subClassOf" in unicode(x[1]):
			output[4] = output[4] + unicode(x[2])
		elif "IAO_0000117" in unicode(x[1]):
			output[5] = output[5] + unicode(x[2])
		elif "#seeAlso" in unicode(x[1]):
			if len(output[6]) > 9:
				output[6] = output[6] + ", " + unicode(x[2])
			else:
				output[6] = output[6] + unicode(x[2])	
		else:
			output[7] = output[7] + unicode(x[2])	
	for triple in output:
		print triple

def findClass(className,classList):
	length = len(classList)
	found = False
	i = 0
	output = ("%s :: Searching for class %s \n" % (getTime(),className))
	logfile.write(output)
	while found != True and i < length:
		classDets = classList[i].serialize()
		label = "label \"%s\"" %(className)
		if label in classDets:
			output = ("%s :: Found class %s \n" %(getTime(),className))
			logfile.write(output)
			logfile.write(classDets)
			output = ("%s :: Printing class details to console \n" %(getTime()))
			logfile.write(output)
			found = True
			printDetails(classList[i])
		i = i + 1
	if found == False:
		output = ("%s :: Did not find class %s \n" %(getTime(), className))
		print "Sorry, could not find a class by that name"
		logfile.write(output)

def main():
	modelName = raw_input("Which owl onthology would you like to view:\n1. OAE_DINTO1.2_subset.owl\n")
	if modelName == "OAE_DINTO_subset.owl" or modelName == "1":
		modelName = "DINTO/DINTO1.2/DINTO 1.2 additional material/DINTO 1.2 subsets/OAE_DINTO_subset.owl"
		output = ("%s :: Loading in owl file at %s \n" %(getTime(),modelName))
		logfile.write(output)
		classList = getClasses(modelName)
		quit = False
		while quit == False:
			className = raw_input("Choose a class or enter quit to exit the application:")
			if className == "quit":
				quit = True
			else:	
				output = ("%s :: User selected finding class %s \n" %(getTime(),className))
				logfile.write(output)
				findClass(className,classList)
		output = ("%s :: Exiting application \n" %(getTime()))
		logfile.write(output)
		logfile.close()
	else:
		print "That is not a valid owl onthology"
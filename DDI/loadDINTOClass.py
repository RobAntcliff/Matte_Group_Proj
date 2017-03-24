import ontospy
import datetime
import rdflib
import os 
import time

datestr = time.strftime("%Y-%m-%d")
timestr = time.strftime("%H:%M:%S")

logfile = open("log_folder/DINTO/" + timestr + "_" + datestr + ".log","w+")

def getTime():
	now = datetime.datetime.now()
	time = "%s/%s/%s at %s:%s:%s" % (now.day,now.month,now.year, now.hour, now.minute, now.second) 
	return time

def printHelp():
	print("\nTo run a command enter \n  help:  to display this list of commands at any time\n  load pml:  to load a PML file to be worked with\n  check pml:  to check a loaded PML file for errors\n  find drugs:  to search for drugs in a loaded PML file\n  run parse:  to scan the file for errors\n  load pml: to load an OWL ontology\n  quit:  to close the application\n")
	
def getClasses(owl):
	model = ontospy.Ontospy(owl)
	classList = model.classes
	if classList != []:
		output = ("%s :: Classes loaded from model at %s \n" %(getTime(),owl))
	else:
		output = ("%s :: Error - Classes not loaded from %s. Invalid owl file \n" %(getTime(),owl))
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
	print ("\n")
	for triple in output:
		print (triple)
	print ("\n")

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
		print ("Sorry, could not find a class by that name")
		logfile.write(output)

def main():
	choice = raw_input("\n To choose an OWL ontology to work with you can enter \n  1:  to use the OAE  subset\n  2:  to use the BRO subset\n  3:  to use PKO subset\n  4:  to use the error.owl\n  5:  to use your own OWL file\n  return:  to return to main menu\n")

	if choice == "return":
		output = ("%s :: Exiting application \n" %(getTime()))
		logfile.write(output)
		logfile.close()
		return

	elif choice == "1":
		modelName = 'owlfiles/OAE_DINTO_subset.owl'
	
	elif choice == "4":
		modelName = 'owlfiles/error.owl'

	elif choice == "3":
		modelName = 'owlfiles/BRO_DINTO_subset.owl'

	elif choice == "2":
		modelName = 'owlfiles/PKO_DINTO_subset.owl'

	elif choice == "5":
		choice = input("\nEnter the path of the OWL file you wish to use or enter return to return to main menu\n")
		if choice == "return":
			output = ("%s :: Exiting application \n" %(getTime()))
			logfile.write(output)
			logfile.close()
			return	

		else:
			modelName = choice
		
	else: 
		main()

	print("\nLoading " + str(modelName) +"\n")
	output = ("%s :: Loading in owl file at %s \n" %(getTime(),modelName))
	logfile.write(output)
	classList = getClasses(modelName)

	if classList != []:
		quit = False

		while quit == False:
			className = raw_input("\nEnter a class to search for or enter return to return to main menu\n")
			if className == "return":
				printHelp()
				quit = True
			else:	
				output = ("%s :: User selected finding class %s \n" %(getTime(),className))
				logfile.write(output)
				findClass(className,classList)
		output = ("%s :: Exiting application \n" %(getTime()))
		logfile.write(output)
		logfile.close()
	else:
		print ("\nCannot read that file. Please try again\n")
		main()

if __name__ == '__main__':
   main()

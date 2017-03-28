def savePMLFile(name, content):
	the_file = open(name+'.pml', 'w')
	the_file.write(content)

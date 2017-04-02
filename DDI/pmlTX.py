def savePMLFile(name, content):
	the_file = open("New_Pathways/"+name+'.pml', 'w')
	the_file.write(content)

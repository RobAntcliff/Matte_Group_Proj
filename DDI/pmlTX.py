def savePMLFile(name, content):
	the_file = open("New_Pathways/"+name, 'w')
	pretty_pml = prettyPML(content)
	the_file.write(pretty_pml)
	print("\n\nYour new pathway is now available in the New_Pathways folder:"+
	      "\n\n                Matte_Group_Proj -> New_Pathways -> " + name)

containers = {
	      "process",
	      "action",
	      "iteration",
	      "branch",
	      "sequence",
	      "manual"
	     }

def prettyPML(pml_string):
	pml_list = pml_string.split()
	i = 0
	pretty_string = ""
	indent = ""
	names_list = []
	name_ext = 2
	while i < len(pml_list):
		current = pml_list[i]
		current_string = ""

		if current == '{':
			if pml_list[i-1] in containers:
				indent += "      "
				current_string = current + '\n' + indent
			elif i > 1:
				if pml_list[i-2] in containers:
					indent += "      "
					current_string = current + '\n' + indent
				else:
					current_string = current + ' '

		elif current == '}':
			if pml_list[i-1] == '}':
				pretty_string = pretty_string[:-6]
				indent = indent[:-6]
			current_string = current + '\n' + indent

		elif current[0] == '{' and len(current) > 1:
			pml_list.insert(i+1, '{')
			pml_list.insert(i+2, current[1:])

		elif current[len(current)-1] == '}' and len(current) > 1:
			pml_list.insert(i+1, current[:-1])
			pml_list.insert(i+2, '}')

		else:
			if pml_list[i-1] in containers:
				if current in names_list:
					current = current+"_"+str(name_ext)
					name_ext += 1
				else:
					names_list.append(current)
			current_string = current + ' '
		pretty_string += current_string
		i += 1

	return pretty_string

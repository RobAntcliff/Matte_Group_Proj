#to run: "python3 merge.py pmlfiles/drugs.pml pmlfiles/branch.pml" from DDI folder
#resulting file goes into pmlfiles folder with name of both ie "drugsbranchmerge.pml"
#can be pmlchecked using main app to make sure result is valid

import sys
import os
from DDI.pmlTX import *

#way to indent text
try:
    import textwrap
    textwrap.indent
except AttributeError:  # undefined function (wasn't added until Python 3.3)
    def indent(text, amount, ch=' '):
        padding = amount * ch
        return ''.join(padding+line for line in text.splitlines(True))
else:
    def indent(text, amount, ch=' '):
        return textwrap.indent(text, amount * ch)

#make sure pmlfiles subdirectory exists
subdirectory = "pmlfiles"
try:
  os.mkdir(subdirectory)
except Exception:
  pass

#function to get filename alone for sticking into names
def getFileNameWithoutExtension(path):
  return path.split('\\').pop().split('/').pop().rsplit('.', 1)[0]

def merge(file_one, file_two):
	#load source files + contents
	file_1 = open(file_one)
	file_2 = open(file_two)

	name_1 = getFileNameWithoutExtension(file_1.name)
	name_2 = getFileNameWithoutExtension(file_2.name)

	#read contents and change top level process to iteration of our merged branch
	#and append name of sourcefile to action names to avoid nameclash
	file_1_contents = file_1.read()
	file_1_contents = file_1_contents.replace("process","iteration",1)
	#file_1_contents = file_1_contents.replace("action ","action "+name_1+"_")
	file_2_contents = file_2.read()
	file_2_contents = file_2_contents.replace("process","iteration",1)
	#file_2_contents = file_2_contents.replace("action ","action "+name_2+"_")

	#create new file from name of source files
	full_name = name_1 + '_' + name_2 + '_' + "merge.pml"

	#name top-level process after input files
	myfile = "process "+name_1+"_"+name_2+"_merge {\n"
	myfile += indent("branch merged {\n", 2)

	myfile += indent(file_1_contents, 4)

	myfile += "\n"

	myfile += indent(file_2_contents, 4)

	myfile += indent("}\n", 2)
	myfile += "}"
	
	savePMLFile(full_name, myfile)



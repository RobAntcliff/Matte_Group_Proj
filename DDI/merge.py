#to run: "python3 merge.py pmlfiles/drugs.pml pmlfiles/branch.pml" from DDI folder
#resulting file goes into pmlfiles folder with name of both ie "drugsbranchmerge.pml"
#can be pmlchecked using main app to make sure result is valid

import sys
import os

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

#load source files + contents
file_1 = open(sys.argv[1])
file_2 = open(sys.argv[2])

name_1 = getFileNameWithoutExtension(file_1.name)
name_2 = getFileNameWithoutExtension(file_2.name)

#read contents and change top level process to iteration of our merged branch
#and append name of sourcefile to action names to avoid nameclash
file_1_contents = file_1.read()
file_1_contents = file_1_contents.replace("process","iteration",1)
file_1_contents = file_1_contents.replace("action ","action "+name_1)
file_2_contents = file_2.read()
file_2_contents = file_2_contents.replace("process","iteration",1)
file_2_contents = file_2_contents.replace("action ","action "+name_2)

#create new file from name of source files
full_name = name_1 + name_2 + "merge.pml"
filepath = os.path.join(subdirectory, full_name)
merged_file = open(filepath, 'w')

#slam contents of both files into new file
with open(filepath, "a") as myfile:

  #name top-level process after input files
  myfile.write("process "+name_1+"_"+name_2+"_merge {\n")
  myfile.write(indent("branch merged {\n", 2))

  myfile.write(indent(file_1_contents, 4))

  myfile.write("\n")

  myfile.write(indent(file_2_contents, 4))

  myfile.write(indent("}\n", 2))
  myfile.write("}")



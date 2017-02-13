from subprocess import call

# This takes in a file path from the user
# You can use absolute pathing or use '../' to reach the repo root dir
file_path = input("Please enter path to PML file: ")

# This calls the peos pml check on the selected file
# We can change this to whatever command is needed
pml_check = "../peos-master/pml/check/pmlcheck"
call([pml_check, file_path])

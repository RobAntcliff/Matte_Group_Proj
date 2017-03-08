# Matte_Group_Proj
The group project repository for team Matte

---
## Installation & Testing
### PEOS
1. Clone the Matte_Group_Proj repository with : `git clone --recursive https://github.com/RobAntcliff/Matte_Group_Proj.git`
1. In the root directory where dependencies.sh can be found run `./dependencies.sh ` This script will install all dependencies needed for PEOS
1. From the peos-master directory run : `pml/check/pmlcheck compiler/models/eggs.pml` eggs.pml can be replaced with any PML file from the models folder

### OWL
1. Navigate to OWL/Protege-5.1.0
1. Run `./run.sh` This will open the protege GUI
1. Use File -> Open to select one of the DINTO .owl files from the DINTO folder. Protege will automatically report a large amount of metrics about the ontology on the right side of the GUI

---
## Features
### PML File Selection

1. In the File-Selector, run `python slector-ui.py`
2. You will then be prompted to enter the file path (surrounded by single quotations) of the desired PML file you want to select. You can either use the absolute pathing, or it is possible to use ../ to reach the root of this repository and add the rest of the pathing to that, for example `'../peos-master/compiler/models/eggs.pml'`
1. Running `./test_selector.sh` will test the file selector on various PML files. As these are all verified PML files, we can see if the file selector fails to recognise PML files correctly

### Load Owl Ontology
1. Open your command line terminal, and navigate to the folder /OWL
2. Run `./dependencies.sh` in this folder to install the dependencies for loading OWL onthologies via the command line
3. Once the installation is complete, navigate to  the folder containing your OWL onthology (for this project either follow the path /OWL/DINTO/DINTO 1 or /OWL/DINTO/DINTO1.2 down until you have a .owl file)
4. Enter the command `ontospy "X.owl"` with X being your desired OWL file, and include the quotes when running the command
1. Running `./test_loadowl.sh` will run tests that will attempt to load and run through the class hierarchies of owl onthologies in the DINTO folder

### PML Log-file Generation
1. While in the peos-master folder, run `python logGen.py`
1. This will run PML check on the fill eggs.pml and log the result in the file test.log

 ---

## Credit
PEOS - https://github.com/jnoll/peos/tree/start
DINTO - https://github.com/labda/DINTO
Protege - http://protege.stanford.edu

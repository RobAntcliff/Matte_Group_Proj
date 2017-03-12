# Matte_Group_Proj
The group project repository for team Matte

---
## Installation & Testing
### PEOS
1. Clone the Matte_Group_Proj repository with : `git clone --recursive https://github.com/RobAntcliff/Matte_Group_Proj.git`
2. In the root directory where dependencies.sh can be found run `./dependencies.sh echo yyyyyyyyy` This script will install all dependencies needed for PEOS
3. From the peos-master directory run : `pml/check/pmlcheck compiler/models/eggs.pml` eggs.pml can be replaced with any PML file from the models folder

### OWL
1. Navigate to OWL/Protege-5.1.0
2. Run `./run.sh` This will open the protege GUI
3. Use File -> Open to select one of the DINTO .owl files from the DINTO folder. Protege will automatically report a large amount of metrics about the ontology on the right side of the GUI

---
### Running the Application
1. Once in the Matte_Group_Proj folder, run the command 'python3 DDI-App-UI.py' to start the application
2. By following the on screen instructions, you can select a PML file to load into the application and run check on it
3. The PML file check will generate a log file of the analysed PML file. If there is a syntaxical error, that will be reported on screen for immediate notice
4. Loading OWL file will allow you to search the ontology for a class. We recommend searching for `lung AE` or `sore throat AE` 
5. PML log files can be found in DDI-App/log_folder, and the DINTO log is in the DDI-App folder
6. The function 'find drugs' will analysis and identify drugs from a PML file. Entering 1 will run on the file drugs.pml, 2 will run on nodrugs.pml

### Testing
1. To test the PML file loading and checking, nagivate to the tests folder in the directory, and go to the pml folder there. Running `./labassessmenttest.sh`, `./drugstest.sh` or `./nodrugstest.sh` will test the application with the corresponding PML file and output their log file. Running `./errortest.sh` will show us in it's log the case of incorrect syntax in a PML file



 ---

## Credit
PEOS - https://github.com/jnoll/peos/tree/start
DINTO - https://github.com/labda/DINTO
Protege - http://protege.stanford.edu

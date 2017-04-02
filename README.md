## Matte_Group_Proj
The group project repository for team Matte

---
### Installation
1. Clone the Matte_Group_Proj repository with : `git clone --recursive https://github.com/RobAntcliff/Matte_Group_Proj.git`
2. In the root directory where dependencies.sh can be found run `./dependencies.sh` This script will install all dependencies needed

### Running the Application
1. In the Matte_Group_Proj folder, run the command 'python3 DDI-App-UI.py' to start the application
2. The app will open into the main menu, with a list of commands to select from 
3. To select a main menu command, simply type the command name i.e to use 'load pml' type in `load pml`
4. Submenus can be selected from using the number of the list item you wish to select i.e in 'load pml' entering `3` will select drugs.pml
5. Entering `quit` in the main menu will exit the app, and `return` in submenus will return to the main menu

#### Release One

##### PML File Selection + Loading
1. From the list of commands in the DDI app, select command 'load pml' to load a PML file
2. The app will ask you to select a PML file from our list of pre-loaded PMLs, or whether you want to use your own file
3. If you select to use your own file, you will be prompted to enter the path to that file
4. You can access all of our PML files in the `pmlfiles` folder 

##### Identify Drugs in PML + On Screen PML Reporting
1. From the list of commands in the DDI app, select command 'find drugs' to search the selected PML file for drugs
2. If any drugs are found in the app, they will be reported on screen
3. To test this feature, load drugs.pml into the app and use this function. The app will report it found 
>['capecitabine', 'bupropion']

##### PML Error and Warning Highlights + PML Log-file generation
1. While using the DDI app, if a PML is not loaded before actions are performed on a pml file, the app will prompt the user that no PML has been selected, and one is needed
2. From the list of commands in the DDI app, select command 'check pml' to run a syntax check on the selected PML file. Any errors found will be printed on screen to alert you
3. Error information is also written to the PML logfile, found in `log_folder/PML/`
4. If no errors are found, the logfile will update with an analysis of the PML file
5. To test this feature, load error.pml into the app and use this function. The app will report it found 
>pmlfiles/error.pml:1: syntax error at bacon

##### Select Specific OWL Ontology + Load Selected Ontology
1. From the list of commands in the DDI app, select command 'load owl' to select an OWL ontology
2. The app will ask you to select OWL file from our list of pre-loaded ontologies, or whether you want to use your own file
3. 3. If you select to use your own file, you will be prompted to enter the path to that file
4. You can access all of our OWL files in the `owlfiles` folder 

##### Identify Drugs in DINTO + On Screen DINTO Reporting
1. Once the selected OWL file is finished loading, the app will prompt you to search for a drug class in the DINTO
2. The app will search for the entered class, and report its findings
3. To test this feature, load OAE_DINTO_subset.owl into the app and use this function. When prompted for a class, enter `lung AE`. The app will report 
>Label: lung AE
>Description: a respiratory system AE which has an outcome of lung disorder
>Alternate Term: lung disorder AE
>Definition Source:
>SubClass of: http://purl.obolibrary.org/obo/OAE_0000378
>Term Editor: YH
>See Also:HPO: HP_0006552, MedDRA: 10025082, SIDER: C0024115
>Type: http://www.w3.org/2002/07/owl#Class


##### DINTO Error and Warning Highlights + DINTO Logfile Generation
1. When an OWL file is selected, an analysis of this file will be reported on in its logfile, found in `log_folder/DINTO/`
2. Any errors in the OWL file will be reported on screen and in the logfile
3. To test this feature, load error.owl into the app. The app will report 
>Fatal error parsing graph (tried using RDF serialization: ['xml', 'turtle', 'n3', 'nt', 'trix', 'rdfa'])

#### Release Two
##### Adding Time to PML
##### Mock DDI Characterisation Data
##### Lookup Drugs in Mock
##### Identify DDIs
##### Report un-named PML construct
##### Report PML construct name-clash
##### Report use of task construct
##### Specify Delay
##### Merging Clinical Pathways written in PML
##### PML-TX Save PML to File
>Upon loading a file, a backup is saved to the New_Pathways folder in the Matte_Group_Proj folder.
>This is simply for testing until the merge feature has been completed.
 ---

### Credit
DINTO - https://github.com/labda/DINTO

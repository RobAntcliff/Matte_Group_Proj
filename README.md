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
> Drug found in PML file -> ['capecitabine', '9pm', 'weekly']
> Drug found in PML file -> ['fluoxetine', '11pm', 'monthly']
> Drug found in PML file -> ['erythromycin', 'weekly']
> Drug found in PML file -> ['capecitabine']

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
> Label: lung AE
> Description: a respiratory system AE which has an outcome of lung disorder
> Alternate Term: lung disorder AE
> Definition Source:
> SubClass of: http://purl.obolibrary.org/obo/OAE_0000378
> Term Editor: YH
> See Also:HPO: HP_0006552, MedDRA: 10025082, SIDER: C0024115
> Type: http://www.w3.org/2002/07/owl#Class


##### DINTO Error and Warning Highlights + DINTO Logfile Generation
1. When an OWL file is selected, an analysis of this file will be reported in its logfile, found in `log_folder/DINTO/`
2. Any errors in the OWL file will be reported on screen and in the logfile
3. To test this feature, load error.owl into the app. The app will report 
> Fatal error parsing graph (tried using RDF serialization: ['xml', 'turtle', 'n3', 'nt', 'trix', 'rdfa'])

#### Release Two
##### Adding Time to PML
1. To check for the syntax of the time in PML, go to DDI/pmlfiles/drugs.pml
2. To test this feature, load drugs.pml into the app. The app will report
> Drug found in PML file -> ['capecitabine', '9pm', 'weekly']
> Drug found in PML file -> ['fluoxetine', '11pm', 'monthly']
> Drug found in PML file -> ['erythromycin', 'weekly']
> Drug found in PML file -> ['capecitabine']

##### Mock DDI Characterisation Data
1. New mock DDI Data can be found in the mockfiles folder in the directory /DDI/

##### Lookup Drugs in Mock
1. From the list of commands in the DDI app, select command 'load mock' to select an Mock DINTO file
2. The app will ask you to select mock DINTO file from our list of pre-loaded CSVs, or whether you want to use your own file
3. If you select to use your own file, you will be prompted to enter the path to that file
4. The contents of the mock DINTO file will be reported on screen and in it's logfile, found in `log_folder/MOCK/`
4. To test this feature, load DDI.csv into the app. The app will report
> Below are the contents of DDI/mockfiles/DDI.csv
>     -- Drug 1 - Drug 2 - DDI Type - Time - Unit --
>        coke - pepsi - bad - 5 - sec
>        coke - 7up - bad - 2 - min
>        pepsi - flat7up - good - 3 - hr
>        paracetamol - alcohol - good - 1 - day
>        caffeine - alcohol - bad - 1 - week
>        coke - alcohol - good - 52 - week
>        capecitabine - bupropion - bad - 2 - hr

##### Identify DDIs
1. From the list of commands in the DDI app, select command 'check ddi' to search the selected mock DINTO file for drugs found in the PML file
2. If any drugs are found in the app, they will be reported on screen
3. To test this feature, load drugs.pml and DDI.csv into the app and use this function. The app will report it found 
> ['capecitabine', 'bupropion', 'bad', '2', 'hr']

##### Report un-named PML construct
1. This error is checked while parsing and will report unnamed constructs.
2. If no such constructs exist, no report is printed.
3. To test this feature, load noname.pml into the app. The app will report
> Error Report :: Type -> Action : Line Number -> 9 : Expecting -> ID, Received -> {
> Error Report :: Type -> Left Bracket : Line Number -> 9 : Expecting -> LEFTBRACKET, Received -> script 

##### Report PML construct name-clash
1. This error is checked while parsing and will report constructs with the same name.
2. If no such constructs exist the user is told on screen.
3. To test this feature, load clash1.pml into the app. The app will report
> Construct name clash occured : Name -> act1
> Construct Type -> action : Line number -> 2.
> Construct Type -> action : Line number -> 16.
> Task construct not used in PML file.


##### Report use of task construct
1. This error is checked while parsing and will report the use of task constructs.
2. If no such constructs exist the user is informed through on screen print.
3. To test this feature, load branch.pml into the app. The app will report
> Task construct is now deprecated, please use Sequence in its place.
> Task was used at line 2.


##### Specify Delay
1. To add a delay, add "delay { "x" }", with the x replaced by the time period, for exapmle, 30 minutes, 6 hours, 3 days, and so on.
2. To see if a pml file contains a delay, select "load pml" from the list of commands in the DDI app.
3. Then choose the pml file you wish to check for delays.
4. If a file contains delays, they will be reported, with the associated action number included in the report, otherwise the app will output "No Delays specified in PML file".
5. Running on "drugs.pml" the app will report 
> Delay of 20 minutes -> Action 1
> Delay of 6 hours -> Action 3
> Delay of 10 minutes -> Action 6
 
##### Merging Clinical Pathways written in PML
1. From DDI folder, run "python3 merge.py pmlfiles/filename1.pml pmlfiles/filename2.pml". Try using "drugs.pml" and "branch.pml" as most others have intentional errors for testing.
2. Resulting file is saved in pmlfiles folder with the name of both ie "filename1filename2merge.pml"
3. Can be pmlchecked using main app to make sure result is valid. Simply run load pml and choose to use your own file, then paste in the path of the new merged file.

##### PML-TX Save PML to File
1. Upon loading a file, a backup is saved to the New_Pathways folder in the Matte_Group_Proj folder.
2. This is simply for testing until the merge feature has been completed.
 ---

### Credit
DINTO - https://github.com/labda/DINTO

# Matte_Group_Proj
The group project repository for team Matte

---
## Installation & Testing
### PEOS
1. Clone the Matte_Group_Proj repository with : `git clone --recursive https://github.com/RobAntcliff/Matte_Group_Proj.git`
1. In the root directory where dependencies.sh can be found run :
`sh dependencies.sh ` This bash script will install all dependencies needed for PEOS, and will compile
1. From the root directory run : `pml/check/pmlcheck compiler/models/eggs.pml` eggs.pml can be replaced with any pml file from the models folder

### OWL
1. Navigate to OWL/Protege-5.1.0
1. Run `./run.sh` This will open the protege GUI
1. Use File -> Open to select one of the DINTO .owl files from the DINTO folder. Protege will automatically report a large amount of metrics about the ontology on the right side of the GUI

---

## Credit
PEOS - https://github.com/jnoll/peos/tree/start
DINTO - https://github.com/labda/DINTO
Protege - http://protege.stanford.edu

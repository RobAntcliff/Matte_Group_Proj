#!/bin/bash

cd ..
python3 DDI-App-UI.py <<!
load OWL
OWL/DINTO/DINTO1.2/DINTO 1.2 additional material/DINTO 1.2 subsets/OAE_DINTO_subset.owl
lung AE
!

echo  "
Test on Dinto Subset for class Lung AE ran. Check logfile"

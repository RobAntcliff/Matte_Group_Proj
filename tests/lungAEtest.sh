#!/bin/bash

cd ..
python3 DDI-App-UI.py <<!
load OWL
OAE_DINTO_subset.owl
lung AE
quit
quit
!

echo  "
Test on Dinto Subset for class Lung AE ran. Check logfile"

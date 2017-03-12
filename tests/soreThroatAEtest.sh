#!/bin/bash

cd ..
python3 DDI-App-UI.py <<!
load OWL
OAE_DINTO_subset.owl
sore throat AE
quit
quit
!

echo  "
Test on Dinto Subset for class sore throat AE ran. Check logfile"

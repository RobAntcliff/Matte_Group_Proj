#!/bin/bash

cd ..
python3 DDI-App-UI.py <<!
load PML
4
check PML
quit
!

echo "
Test on nodrugs.pml with Check ran. See logfiles."

#!/bin/bash

cd ..
python3 DDI-App-UI.py <<!
load PML
1
check PML
quit
!

echo "
Test on Lab Assessment.pml with Check ran. See logfiles."

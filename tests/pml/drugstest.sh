#!/bin/bash

cd ..
cd ..
python3 DDI-App-UI.py <<!
load PML
2
check PML
quit
!

echo "
Test on drugs.pml with Check ran. See logfiles."

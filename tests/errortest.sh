#!/bin/bash

cd ..
python3 DDI-App-UI.py <<!
load PML
3
check PML
quit
!

echo "
Test on error.pml with Check ran. See logfiles."

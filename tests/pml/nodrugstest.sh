#!/bin/bash

cd ..
cd ..
python3 DDI-App-UI.py <<!
load PML
4
check PML
quit
!

echo "
Test on nodrugs.pml with Check ran.
This test should throw an error, as the pml syntax is incorrect.
 See logfiles."

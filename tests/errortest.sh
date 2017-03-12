#!/bin/bash

cd ..
python3 DDI-App-UI.py <<!
load OWL
OWL/DINTO/DINTO 1/DINTO_1.owl
!

echo  "
Test on Dinto 1 ontolgy. This should throw errors. Check logfile"

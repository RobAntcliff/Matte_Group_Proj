#!/bin/bash

ontospy DINTO/DINTO1.2/DINTO\ 1.2\ additional\ material/DINTO\ 1.2\ subsets/OAE_DINTO_subset.owl
if [ $? -eq 0 ]; then
    echo "TEST 1  : PASS"
else
    echo "TEST 1  : FAIL"
fi 

ontospy DINTO/DINTO\ 1/DINTO\ 1\ additional\ material/DINTO\ 1\ subsets/PKO_DINTO_subset.owl
if [ $? -eq 0 ]; then
    echo "TEST 2  : PASS"
else
    echo "TEST 2  : FAIL"
fi
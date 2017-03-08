#!/bin/bash


python selector-ui.py <<EOF
'../peos-master/compiler/models/eggs.pml' 
EOF

python selector-ui.py <<EOF
'../peos-master/compiler/models/branch.pml'
EOF

python selector-ui.py <<EOF
'../peos-master/compiler/models/martini.pml'
EOF


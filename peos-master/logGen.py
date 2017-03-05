import subprocess
import sys
with open('test.log', 'w') as f:
    process = subprocess.Popen(['pml/check/pmlcheck', 'compiler/models/eggs.pml'], stdout=subprocess.PIPE)
    for c in iter(lambda: process.stdout.read(1), ''):
        sys.stdout.write(c)
        f.write(c)
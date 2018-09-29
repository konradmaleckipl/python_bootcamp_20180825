import sys
import os.path
from os import scandir

assert len(sys.argv) > 1, 'Prosze podac sciezke do katalogu'
start_dir = sys.argv[1]
assert os.path.isdir(start_dir), 'Podana sciezka nie jest katalogiem'

def scan_path(path, level=1):
    for entry in scandir(path):
        if os.path.isdir(entry):
            scan_path(entry, level+1)
        else:
            print(str('-'*level)+' '+str(entry))

scan_path(start_dir)
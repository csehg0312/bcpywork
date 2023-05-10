
import pathlib
print(pathlib.Path(__file__).parent.resolve())

import subprocess

print(subprocess.check_output('python -m pip uninstall cffi', stderr=subprocess.STDOUT, shell=True).decode('utf-8'))

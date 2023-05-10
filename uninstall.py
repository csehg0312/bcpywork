import subprocess

dependencies = ["dataclasses","collections","PySimpleGUI","pyperclip","keyboard","winshell","python-magic", "pathlib", "Tk", "pywin32-ctypes", "win32api", "pywin32-stubs","libmagic", "python_magic_bin-0.4.14-py2.py3-none-win_amd64.whl", "python-magic-bin", "psutil", "decorator" ,"cffi","cachetools", "pywin32"]

for i in range(len(dependencies)):
    cmdCommand = f"python -m pip uninstall {dependencies[i]}"
    process = subprocess.run(cmdCommand.split(),stdout=subprocess.PIPE, input='Y', encoding='ascii')  
    print(process.returncode)
    


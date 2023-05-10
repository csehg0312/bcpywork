import subprocess

dependencies = ["--upgrade pip","decorator" ,"cffi","cachetools","shutil", "os","time","dataclasses","collections","PySimpleGUI","pyperclip","keyboard","winshell","python-magic", "pathlib", "Tk", "pywin32-ctypes", "win32api", "pywin32-stubs","libmagic", "python_magic_bin-0.4.14-py2.py3-none-win_amd64.whl", "python-magic-bin", "psutil"]

for i in range(len(dependencies)):
    cmdCommand = f"python -m pip install {dependencies[i]}"
    process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE, universal_newlines=True)
    output, error = process.communicate()
    print(output)


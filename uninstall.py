import subprocess

dependencies = ["dataclasses","collections","PySimpleGUI","pyperclip","keyboard","winshell", "pathlib", "Tk", "pywin32", "win32api", "pywin32-stubs", "python_magic_bin-0.4.14-py2.py3-none-win_amd64.whl", "python-magic-bin"]

for i in range(len(dependencies)):
    cmdCommand = f"python -m pip uninstall {dependencies[i]}"
    process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE, universal_newlines=True)
    output, error = process.communicate()
    print(output)
    
    print(error)


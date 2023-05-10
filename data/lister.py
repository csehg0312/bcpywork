
import pathlib
print(pathlib.Path(__file__).parent.resolve())

import subprocess


str_to_lsplit:str = "altgraph asttokens backcall cachetools cffi colorama comm dataclasses debugpy decorator distlib executing filelock ipykernel ipython jedi jupyter_client jupyter_core keyboard libmagic matplotlib-inline nest-asyncio parso pathlib pefile pickleshare platformdirs prompt-toolkit psutil pure-eval py2exe pycparser Pygments pyinstaller-hooks-contrib pyperclip PySimpleGUI python-dateutil python-magic python-magic-bin pywin32 pywin32-ctypes pywin32-stubs PyYAML pyzmq six stack-data style tk tornado traitlets wcwidth winshell"
list_split = str_to_lsplit.split(" ")
print(list_split)

import subprocess

for i in range(len(list_split)):
    cmdCommand = f"python -m pip uninstall {list_split[i]}"
    process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE, universal_newlines=True)
    output, error = process.communicate()
    print(output)
    
    print(error)
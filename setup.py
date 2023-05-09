import subprocess

dependencies = ["--upgrade pip","shutil", "os","time","dataclasses","collections","PySimpleGUI","pyperclip","keyboard","winshell","python-magic", "pathlib", "tkinter"]

for i in range(len(dependencies)):
    cmdCommand = f"pip install {dependencies[i]}"
    process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output)


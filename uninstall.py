import subprocess

dependencies = ["--upgrade pip","cffi","shutil", "os","time","dataclasses","collections","PySimpleGUI","pyperclip","keyboard","winshell","python-magic", "pathlib", "Tk", "pywin32", "win32api", "pywin32-stubs", "python_magic_bin-0.4.14-py2.py3-none-win_amd64.whl", "python-magic-bin"]

for i in range(len(dependencies)):
    cmdCommand = f"python -m pip install {dependencies[i]}"
    try:
        process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        print(output)
    except:
        print(error)


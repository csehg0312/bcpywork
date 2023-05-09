import yaml
import subprocess


cmdCommand = "pip install --upgrade pip"   #specify your cmd command
process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
print(output)

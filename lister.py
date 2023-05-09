import os

path = "./icon"

print(os.listdir(path))

import pathlib
print(pathlib.Path(__file__).parent.resolve())
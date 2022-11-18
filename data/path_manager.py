import os
import disk_manager as dm

#print(dm.drives)


for item in dm.drives:
    onprint = os.listdir(item)
    #print(onprint)
    #print('-----------')
    onprint = ""

''' onprint = os.listdir(path)
print(onprint) '''

if __name__ == '__main__':
    splitter()
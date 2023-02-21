import os
#import data.dspace_manager as ds
from data.dspace_manager import *
from data.disk_manager import *
import PySimpleGUI as psg

Packed:list

def set_key():
    for item in range(len(disks_data)):
        set_num = item
        set_text = f'-PRB{set_num}-'
        print(set_text)

def create_layout(m_val:int, DName:str, ky:str):
    prelayout = [[psg.Text(DName)],
                 [psg.ProgressBar(max_value=m_val, visible=True, key=ky), psg.Text(f'Max disk space {m_val}')]
                 ]
    text = set_key()
    return prelayout

# d2 = popper(disk)
# def Used(d2):
#     for item in range(len(popper())):
#         print('run')
#         #print(disks_data.keys())
#         DictDisk01 = disks_data.popitem()
#         #print(DictDisk01)
#         #print(type(DictDisk01))
#         DiskToUnpack = DictDisk01[1]
#         print(str(DiskToUnpack))
#         print(type(DiskToUnpack))
#         used, free = DiskToUnpack['used'], DiskToUnpack['free']
#         var_list = []	
#         var_list.append(used)
#         var_list.append(free)
#     return var_list

def Unpack():

    Counter = 0
    PackedLayout = []
    for item in range(len(disks_data)):
        #print(disks_data.keys())
        DictDisk01 = disks_data.popitem()
        #print(DictDisk01)
        #print(type(DictDisk01))
        DiskToUnpack = DictDisk01[1]
        print(str(DiskToUnpack))
        print(type(DiskToUnpack))
        total, used, free = DiskToUnpack['total'], DiskToUnpack['used'], DiskToUnpack['free']
        disk = DiskToUnpack['disk']
        Counter = Counter + 1
        key = f'-PRB{item}-'
        playout = create_layout(total, disk, key)
        PackedLayout.append(playout)
        print(str(PackedLayout))
        #print(total, used, free)
        #print(Counter)
    return PackedLayout

#dlayout = [psg.StatusBar('Disk', key='-ST01-', size=(15,1), enable_events=True, visible=False), psg.ProgressBar(max_value=250, visible=True)]

if __name__ == '__main__':
    #Packed:list
    Packed = Unpack()
    print(type(Packed))
    clearlayout = [[psg.Text('Hello', enable_events=True)]]
    #frlayout = [psg.Frame('', clearlayout)]
#     
#     for i in range(len(Packed)):
#         clearlayout.extend(Packed[i])
#         
window = psg.Window('Window', clearlayout)

ran = False
while True:
    event, values = window.read(timeout=500)
    window.reappear()
    
#     lst = Used()
#     print(lst)
    
    if ran == False:
        for i in range(len(Packed)):
            window.extend_layout(window, Packed[i])
            print(str(window))
        ran = True
        
    if drive_inserted() != 0:
        window.disappear()
    
    if event == psg.WIN_CLOSED:
        break

window.close()
    
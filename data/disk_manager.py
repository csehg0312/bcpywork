import shutil
import os
import time
from dataclasses import dataclass,field
from collections import deque

def calculateSize(num:int):
    return round(num / (2**30), 1)

start = time.perf_counter()

@dataclass
class Drive:
    DSZK:str
    TeliBit:int
    FoglaltBit:int
    
    def __post_init__(self):
        self.Teljes: int = field(default_factory=calculateSize(self.TeliBit))
        self.Foglalt: int = field(default_factory=calculateSize(self.FoglaltBit))

# def diferencia(ls1,ls2):
#     ls_diferencia = [item for item in ls1 if item not in ls2]
#     if len(ls1) != len(ls_diferencia): 
#         return True
#     else:
#         return False


# drives_saved = []

def kinyeres():
    dl = 'CDEFGHIJKLMNOP'
    drives = ['{}:'.format(d) for d in dl if os.path.exists('{}:'.format(d))]
    # if diferencia(drives_saved, drives):
    #     drives_saved.extend(drives)
    # elif diferencia(drives_saved, drives):
    #     ...
    d_nev:deque = deque([])
    d_teljes:deque = deque([])
    d_foglalt:deque = deque([])
    for d in range(len(drives)):
        teli, foglalt, _ = shutil.disk_usage(drives[d])
        D:Drive = Drive(drives[d], teli, foglalt)
        
        d_nev.append(D.DSZK)
        
        d_teljes.append(D.Teljes.default_factory)

        d_foglalt.append(D.Foglalt.default_factory)
    
    return d_nev, d_teljes, d_foglalt        
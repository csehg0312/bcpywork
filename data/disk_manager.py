import shutil
import os
import time
from dataclasses import dataclass,field
from collections import deque

def calculateSize(num:int):
    return int(num // (2**30))

start = time.perf_counter()

@dataclass
class Drive:
    DSZK:str
    TeliBit:int
    FoglaltBit:int
    SzabadBit:int
    
    def __post_init__(self):
        self.Teljes: int = field(default_factory=calculateSize(self.TeliBit))
        self.Foglalt: int = field(default_factory=calculateSize(self.FoglaltBit))
        self.Szabad: int = field(default_factory=calculateSize(self.SzabadBit))

def diferencia(ls1,ls2):
    ls_diferencia = [item for item in ls1 if item not in ls2]
    return ls_diferencia

dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]

def kinyeres():
    d_nev:deque = deque([])
    d_teljes:deque = deque([])
    d_foglalt:deque = deque([])
    for d in range(len(drives)):
        teli, foglalt, szabad = shutil.disk_usage(drives[d])
        D:Drive = Drive(drives[d], teli, foglalt, szabad)
        
        d_nev.append(D.DSZK)
        
        d_teljes.append(D.Teljes.default_factory)

        d_foglalt.append(D.Foglalt.default_factory)
    
    return d_nev, d_teljes, d_foglalt        
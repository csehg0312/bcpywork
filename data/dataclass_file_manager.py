from dataclasses import dataclass, field
from time import strftime, gmtime
import os
#dataclass_file()

# def calcSizeifHuge(num:int):
#     if num >= 10240:
#         num = num / 1024
#         return round(num,2)
#     else:
#         return num

def calcSize(P:str, val):
    j = os.path.join(P,val)
    T = os.path.getsize(j)
    return T

def calname(val):
    N, _ = os.path.splitext(val)
    return N
    
def caltype(val):
    _, E = os.path.splitext(val)
    return E
    
def caldate(P:str, val):
    j = os.path.join(P,val)
    T = os.path.getmtime(j)
    CTV = strftime('%d %b %Y %H:%M', gmtime(T))
    return f'{CTV}'


@dataclass
class File:
    ut: str
    fajl: str
    
    def __post_init__(self):
        self.hely:str
        self.meret:int = field(default_factory=calcSize(self.ut, self.fajl))
        self.egysege:str
        self.modositdate:str = field(default_factory=caldate(self.ut, self.fajl))
        self.nev: str = field(default_factory=calname(self.fajl))
        self.bovitmeny: str = field(default_factory=caltype(self.fajl))
        

# afajl = File('C:/Users/csehg/pytry', 'dataclass_file.py')
# print(f'{afajl.nev.default_factory} {afajl.bovitmeny.default_factory}')
#         



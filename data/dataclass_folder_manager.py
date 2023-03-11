import os
from dataclasses import dataclass, field
from time import strftime, gmtime

def caldate(P:str, val:str):
    j = os.path.join(P,val)
    C = os.path.getmtime(j)
    CTV = strftime('%d %b %Y %H:%M', gmtime(C))
    return f'{CTV}'

@dataclass
class Folder:
    szulout:str
    mappa:str
    
    def __post_init__(self):
        self.megnevez:str = field(default_factory='Mappa')
        self.modisitasdate:str = field(default_factory=caldate(self.szulout,self.mappa))
        

# amappa = Folder('C:/Users/csehg', 'pytry')
# print(amappa.mappalista.default_factory)
        


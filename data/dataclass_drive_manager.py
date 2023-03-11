from dataclasses import dataclass,field
#import shutil
import time

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
    
# teljes, foglalt, szabad = shutil.disk_usage('C:')
#     
# disk1 = Drive('F:', teljes, foglalt, szabad)
# elapsed = time.perf_counter()
# print(f'{disk1.Teljes.default_factory} {disk1.Foglalt.default_factory} {disk1.Szabad.default_factory}')
# print(f'{elapsed - start}')

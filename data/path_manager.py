from dataclasses import dataclass
import os

@dataclass
class Jelen_EleresiUt:
    szulo:str 
    
    def Atiras(self):
        if os.getcwd() != self.szulo:
            self.szulo = os.getcwd()
    
    def SzuloUtvonal(self):
        self.nagyszulo, _ = os.path.split(self.szulo)
        self.szulo = self.nagyszulo
        os.chdir(self.szulo) 
        
    def JelenlegiDiszk(self):
        self.diszk = self.szulo[0] + self.szulo[1] + self.szulo[2]
        return self.diszk
    
    def Frissites(self, csatolt):
        self.csatolt = csatolt
        if os.path.exists(self.csatolt):
            try:
                self.szulo = self.csatolt
                os.chdir(self.szulo)
            except (PermissionError, FileNotFoundError, WindowsError):
                nsz, _ = os.path.split(self.szulo)
                self.szulo = nsz
                os.chdir(self.szulo)
        else:
            os.chdir(self.szulo)
from dataclasses import dataclass
import PySimpleGUI as psg
import pyperclip
import os

@dataclass
class EventHandler:
    bejovo: str
    data:dict
    eventlist:int
    
    def compare(self):
        
            
        if 'c' and self.eventlist == 17:
            fo = self.data.get('fo')
            file = self.data.get('jelolt')
            bov = self.data.get('bovitmenye')
            print(bov)
            pyperclip.copy(f'{os.path.normcase(os.path.join(fo,file))}{bov}')
            psg.popup_ok('Copied to clipboard', auto_close_duration=2)
                    
            
        match self.bejovo:
                
            case 'x':
                ...
            case other:
                ...
                
            
            
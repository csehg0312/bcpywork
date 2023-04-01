from dataclasses import dataclass
import PySimpleGUI as psg

@dataclass
class EventHandler:
    bejovo: str
    ablak:str
    data:dict
    
    def compare(self):
            
        match self.bejovo:
            
            case 'c':
                window = psg.Window('Copy', layout=[[psg.Listbox(['Copy File', 'Copy Path'], enable_events=True, key='-UCOPY-')]], 
                                    return_keyboard_events=True)
                while True:
                    event, values = window.read()
                    if event == psg.WIN_CLOSED or event == 'Escape:27':
                        break
                    
                window.close()
                
            case 'z':
                ...
            case 'x':
                ...
            case other:
                ...
                
            
            
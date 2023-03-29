from dataclasses import dataclass

@dataclass
class EventHandler:
    bejovo: str
    ablak:str
    
    def compare(self):
        if self.bejovo == 'Back':
            print('Back')
        
        elif self.bejovo == 'Cut':
            print('Cut')
            ...
        elif self.bejovo == 'Copy path...':
            ...
        
        else:
            ...
            
        match self.bejovo:
            
            case 'c':
                ...
            case 'z':
                ...
            case 'x':
                ...
            case other:
                ...
                
            
            
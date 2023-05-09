from dataclasses import dataclass
import PySimpleGUI as psg
import pyperclip
import os
from data.file_folder_managing import remove_folder_or_file, create_path_or_folder, renaming, open_file
from gui import create_writer

@dataclass
class EventHandler:
    bejovo: str
    data:dict
    refresh_bool:bool = False
    
    def compare(self):
            
        # if 'c' and self.eventlist == 17:
        #     fo = self.data.get('fo')
        #     file = self.data.get('jelolt')
        #     bov = self.data.get('bovitmenye')
        #     print(bov)
        #     pyperclip.copy(f'{os.path.normcase(os.path.join(fo,file))}{bov}')
        #     psg.popup_ok('Copied to clipboard', auto_close_duration=2)
        if self.bejovo in ('Athelyezes::-FOLDER-', 'Athelyezes megadott mappaba...::-FOLDER-', 'Athelyezes megadott mappaba...::-FILE-', 'Athelyezes::-FILE-', 'Atnevezes::-FILE-', 'Atnevezes::-FOLDER-'):
            match self.bejovo:
                case 'Athelyezes::-FOLDER-':
                    ...
                case 'Athelyezes::-FILE-':
                    ...
                case 'Athelyezes megadott mappaba...::-FOLDER-':
                    ...
                case 'Athelyezes megadott mappaba...::-FILE-':
                    ...
                case 'Atnevezes::-FOLDER-':
                    ...
                case 'Atnevezes::-FILE-':
                    self.refresh_bool = True
                    real_path, head, tail = self.data.get('fo'), self.data.get('jelolt'), self.data.get('bovitmenye')
                    val = psg.popup_get_text('A fajl atnevezese:', default_text=f'{head}{tail}', keep_on_top=True,)
                    print(f'{val}')
                    if val != f'{head}{tail}' and val != '':
                        ...
                        # message_out = renaming(os.path.join(real_path, f'{head}{tail}'), os.path.join(real_path, val))
                        # print(message_out)
                        # psg.popup_notify(message_out)
                        # return refresh
                        
        if self.bejovo in ('Megnyitas Writerben', 'Eleresi ut masolasa', 'Masolas'):
            match self.bejovo:
                case 'Megnyitas Writerben':
                    fajl, bov = self.data.get('jelolt'), self.data.get('bovitmenye')
                    if os.path.exists(os.path.join(self.data.get('fo'), f'{fajl}{bov}')): 
                        fajl_text:str = open_file(os.path.join(self.data.get('fo'), f'{fajl}{bov}'))
                        write_window = create_writer(fajl_text)
                case 'Eleresi ut masolasa':
                    ...
                case 'Masolas':
                    ...

                
            
            
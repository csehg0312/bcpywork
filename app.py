import os
import interface.controller as c
import data.dataclass_drive_manager
from gui import create_ablak, create_search_window, make_second_window, create_disk_window
from data.disk_manager import kinyeres
import PySimpleGUI as psg
from keyboard import is_pressed
from collections import deque
import logging
writerup:bool = False
search_up:bool = False
disk_selectorup:bool = False

os.chdir(os.path.expanduser('~'))


window = create_ablak()
window.set_icon(icon="icon/icov1.ico")

while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED:
        break
    com = values['-COMBO-']
    
    
    
    
    if event == 'Writer' and writerup == False:
        writerup = True
        window2 = make_second_window()
        while True:
            event2,values2 = window2.read(timeout=100)
            
            if event2 in ('X', psg.WIN_CLOSED):
                #logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
                #logging.warning(f'The Writer has been closed, Event: {event2}')
                break
        window2.close()
        writerup=False
        
    if event == '-SEARCH-' and search_up == False:
        search_up = True
        window3 = create_search_window()
        while True:
            window3['-SEARCHING-'].set_focus=True
            event3,values3 = window3.read(timeout=100)
            
            
            if (event3 == psg.WIN_CLOSED) or (is_pressed('esc') == True):
                break
            if is_pressed('enter'):
                window3['-FOUND-'].update(values3['-SEARCHING-'])
                
        window3.close()
        search_up=False
    
    if event == '-DISK_WIN-' and disk_selectorup == False:
        disk_selectorup = True
        disk_nev, disk_teljes, disk_foglalt = kinyeres()
        window4 = create_disk_window(len(disk_nev), disk_nev, disk_teljes)
        while True:
            event4, values4 = window4.read(timeout=100)
            
            if (event4 == psg.WIN_CLOSED) or (is_pressed('esc')):
                break
            for d in range(len(disk_nev)):
               window4[f'-DISK_WIN{d}-'].update_bar(disk_foglalt[d])
        
        window4.close()
        disk_selectorup = False
            
        
        
    com = values['-COMBO-']
    #print(f'{event} and Combo val: {com}')
window.close()
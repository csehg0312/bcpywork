import os
import interface.controller as c
from data.file_folder_managing import create_twoD_list, kereses
from gui import create_ablak, create_search_window, make_second_window, create_disk_window
from data.disk_manager import kinyeres
import PySimpleGUI as psg
from keyboard import is_pressed
from collections import deque
from data.binaris_search import binaris_atvitel
import logging
writerup:bool = False
search_up:bool = False
disk_selectorup:bool = False

os.chdir(os.path.expanduser('~'))


window = create_ablak()
window.set_icon(icon="icon/icov1.ico")
eventlist:deque = deque([])
while True:
    event, values = window.read()
    
    if event == psg.WIN_CLOSED:
        break
    
    if event == 'Control_L:17':
        eventlist.append(17)
    
    
    # if event == '__TIMEOUT__':
    #     event, values = window.read()
    
    
    # com = values['-COMBO-']
    # print(os.getcwd())
    vals:list = create_twoD_list(os.getcwd())
    window['-TABLE01-'].Update(values=vals)
    
    if event == '-Organize-' and is_pressed('enter') and os.path.exists(values['-Organize-']):
        os.chdir(values['-Organize-'])
        vals.clear()
        vals:list = create_twoD_list(os.getcwd())
        window['-TABLE01-'].Update(values=vals)
    
    
    if (event == 'Writer' and writerup == False) or (event == 'w' and eventlist[0] == 17 and writerup == False ):
        eventlist.clear()
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
        
    if (event == '-SEARCH-' and search_up == False) or (event == 's' and eventlist[0] == 17 and search_up == False ):
        eventlist.clear()
        search_up = True
        window3 = create_search_window()
        while True:
            window3['-SEARCHING-'].set_focus=True
            event3,values3 = window3.read()
            if (event3 == psg.WIN_CLOSED) or (event3 == 'Escape:27'):
                break
            
            if values3['-SEARCHING-'] != "":
                window3['-FOUND-'].update(binaris_atvitel(sorted(os.listdir(os.getcwd())), values3['-SEARCHING-']))
            
            else:
                window3['-FOUND-'].update(os.listdir(os.getcwd()))
                
                
        window3.close()
        search_up=False
    
    if (event == '-DISK_WIN-' and disk_selectorup == False) or (event == 'd' and eventlist[0] == 17 and disk_selectorup == False ):
        eventlist.clear()
        disk_selectorup = True
        disk_nev, disk_teljes, disk_foglalt = kinyeres()
        window4 = create_disk_window(len(disk_nev), disk_nev, disk_teljes)
        while True:
            event4, values4 = window4.read(timeout=100)
            
            if (event4 == psg.WIN_CLOSED) or (event4 == 'Escape:27'):
                break
            for d in range(len(disk_nev)):
               window4[f'-DISK_WIN{d}-'].update_bar(disk_foglalt[d])
        
        window4.close()
        disk_selectorup = False
            
        
        
    com = values['-COMBO-']
    #print(f'{event} and Combo val: {com}')
window.close()
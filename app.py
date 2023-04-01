import os
import interface.controller as c
from data.file_folder_managing import create_twoD_list, kereses
from gui import create_ablak, create_search_window, make_second_window, create_disk_window
from data.disk_manager import kinyeres
import PySimpleGUI as psg
from keyboard import is_pressed
from collections import deque
from data.binaris_search import binaris_atvitel
#from event_handler import EventHandler
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
    
   
    
    
    if (event == 'Writer' and writerup == False) or (event == 'w' and eventlist[0] == 17 and writerup == False ):
        eventlist.clear()
        writerup = True
        writer_window = make_second_window()
        while True:
            writer_event,writer_values = writer_window.read(timeout=100)
            
            if writer_event in ('X', psg.WIN_CLOSED) or (event == None):
                #logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
                #logging.warning(f'The Writer has been closed, Event: {writer_event}')
                break
        writer_window.close()
        writerup=False
        
    if (event == '-SEARCH01-' and search_up == False) or (event == 's' and eventlist[0] == 17 and search_up == False ):
        eventlist.clear()
        search_up = True
        search_window = create_search_window()
        while True:
            search_window['-SEARCHING-'].set_focus=True
            search_event,search_values = search_window.read()
            if (search_event == psg.WIN_CLOSED) or (search_event == 'Escape:27') or (event == None):
                break
            
            if search_values['-SEARCHING-'] != "":
                search_window['-FOUND-'].update(binaris_atvitel(sorted(os.listdir(os.getcwd())), search_values['-SEARCHING-']))
            
            else:
                search_window['-FOUND-'].update(os.listdir(os.getcwd()))
                
                
        search_window.close()
        search_up=False
    
    if (event == '-DISK_WIN-' and disk_selectorup == False) or (event == 'd' and eventlist[0] == 17 and disk_selectorup == False ):
        eventlist.clear()
        disk_selectorup = True
        disk_nev, disk_teljes, disk_foglalt = kinyeres()
        disk_window = create_disk_window(len(disk_nev), disk_nev, disk_teljes)
        while True:
            disk_event, disk_values = disk_window.read(timeout=100)
            
            if (disk_event == psg.WIN_CLOSED) or (disk_event == 'Escape:27') or (event == None):
                break
            
            for d in range(len(disk_nev)):
               disk_window[f'-DISK_WIN{d}-'].update_bar(disk_foglalt[d])
               
            if disk_event.rfind('-BM') != -1:
               
                match disk_event:
                    case '-BM0-':
                        match disk_values['-BM0-']:
                            case 'Asztal1::-INT1-':
                                val:str = disk_window['-TX0-'].get()
                                vales:list = create_twoD_list(f'{val}/')
                                window['-TABLE01-'].update(vales)
                                os.chdir(f'{val}/')
                            case 'Asztal2::-INT2-':
                                val:str = disk_window['-TX0-'].get()
                                vales:list = create_twoD_list(f'{val}/')
                                window['-TABLE02-'].update(vales)
                                os.chdir(f'{val}/')
                    case '-BM1-':
                        match disk_values['-BM1-']:
                            case 'Asztal1::-INT1-':
                                 val:str = disk_window['-TX1-'].get()
                                 vales:list = create_twoD_list(f'{val}/')
                                 window['-TABLE01-'].update(vales)
                                 os.chdir(f'{val}/')
                            case 'Asztal2::-INT2-':
                                val:str = disk_window['-TX1-'].get()
                                vales:list = create_twoD_list(f'{val}/')
                                window['-TABLE02-'].update(vales)
                                os.chdir(f'{val}/')
                    case '-BM2-':
                        match disk_values['-BM2-']:
                            case 'Asztal1::-INT1-':
                                val:str = disk_window['-TX2-'].get()
                                vales:list = create_twoD_list(f'{val}/')
                                window['-TABLE01-'].update(vales)
                                os.chdir(f'{val}/')
                            case 'Asztal2::-INT2-':
                                val:str = disk_window['-TX2-'].get()
                                vales:list = create_twoD_list(f'{val}/')
                                window['-TABLE02-'].update(vales)
                                os.chdir(f'{val}/')
                    case '-BM3-':
                        match disk_values['-BM3-']:
                            case 'Asztal1::-INT1-':
                                val:str = disk_window['-TX3-'].get()
                                vales:list = create_twoD_list(f'{val}/')
                                window['-TABLE01-'].update(vales)
                                os.chdir(f'{val}/')
                            case 'Asztal2::-INT2-':
                                val:str = disk_window['-TX3-'].get()
                                vales:list = create_twoD_list(f'{val}/')
                                window['-TABLE02-'].update(vales)
                                os.chdir(f'{val}/')
                    case '-BM4-':
                        match disk_values['-BM4-']:
                            case 'Asztal1::-INT1-':
                                val:str = disk_window['-TX4-'].get()
                                vales:list = create_twoD_list(f'{val}/')
                                window['-TABLE01-'].update(vales)
                                os.chdir(f'{val}/')
                            case 'Asztal2::-INT2-':
                                val:str = disk_window['-TX4-'].get()
                                vales:list = create_twoD_list(f'{val}/')
                                window['-TABLE02-'].update(vales)
                                os.chdir(f'{val}/')
                    case other:
                        continue        
        disk_window.close()
        disk_selectorup = False
            
    if event in ('-TABLE01-', '-TABLE02-'):
        if is_pressed('enter') == True:
            print('pressed')
        print(event)
        
    if (event == 'r') and (eventlist[0] == 17):
        ...
    
        
    com = values['-COMBO-']
    #print(f'{event} and Combo val: {com}')
window.close()
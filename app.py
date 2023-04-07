import os
from data.file_folder_managing import create_twoD_list, kereses
from gui import create_ablak, make_second_window, create_disk_window, file_or_folder_szita
from data.disk_manager import kinyeres
import PySimpleGUI as psg
from keyboard import is_pressed
from collections import deque
import pyperclip
from data.binaris_search import binaris_atvitel
from data.path_manager import Jelen_EleresiUt
from event_handler import EventHandler
import logging
file_right_click:list
file_right_click = ['Fajl', ['Megnyitas Writerben', 'Eleresi ut masolasa', 'Masolas', '---','Athelyezes::-FILE-','Athelyezes megadott mappaba...::-FILE-','---', 'Atnevezes::-FILE-','---' ,'Tulajdonsagok']]
folder_right_click:list
folder_right_click = ['Folder', ['Utvonal masolasa...', 'Athelyezes::-FOLDER-', 'Athelyezes megadott mappaba...::-FOLDER-', 'Atnevezes::-FOLDER-', 'Eltavolitas', 'Directory fa eltavolitasa...', '---' ,'Megnyitas a masik asztalon','---' , 'Tulajdonsagok']]
writerup:bool = False
search_up:bool = False
disk_selectorup:bool = False
van_kijelolt_tabla1:bool = False
van_kijelolt_tabla2:bool = False
window_minimized:bool = False

kijelolt01:str
kijelolt02:str

os.chdir(os.path.expanduser('~'))


window = create_ablak()
window.set_icon(icon="icon/icov1.ico")
eventlist:deque = deque([])
 #--------------------------A program-----------------------------------------------------
while True:
    event, values = window.read()
    
    if event == psg.WIN_CLOSED:
        break
    
    if event == 'Control_L:17':
        eventlist.clear()
        eventlist.append(17)
    
    
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
            if writer_event == 'Control_L:17':
                    key_event, _ = writer_window.read(100)
                    if key_event == 'z':
                        want_to_close:str = psg.popup_yes_no('Are you sure want to quit?') 
                        if want_to_close == 'Yes':
                            
                            break
                        else:
                            pass
                    if key_event == 's':
                        print('saving')
                    if key_event == 'v':
                        pyperclip.paste()
                    if key_event == 'c':
                        pyperclip.copy()
            if writer_event == 'Megnyitas':
                ...
            
            match writer_event:
                case 'Beillesztes':
                    w_val = writer_values['-MULTI-']
                    writer_window['-MULTI-'].update(f'{w_val} {pyperclip.paste()}')
                    w_val = ''
                case 'Masolas':
                    pyperclip.copy(writer_values['-MULTI-'])
            
            
        writer_window.close()
        writerup=False
    
    #---------------------------------Kereses ablak----------------------------------------------
        
    # if (event == '-SEARCH01-' and search_up == False) or (event == 's' and eventlist[0] == 17 and search_up == False ):
    #     eventlist.clear()
    #     search_up = True
    #     search_window = create_search_window()
    #     while True:
    #         search_event,search_values = search_window.read()
    #         search_window['-SEARCHING-'].set_focus=True
    #         search_event,search_values = search_window.read()
    #         if (search_event == psg.WIN_CLOSED) or (search_event == 'Escape:27') or (event == None):
    #             break
            
    #         if search_values['-SEARCHING-'] != "":
    #             search_window['-FOUND-'].update(binaris_atvitel(sorted(os.listdir(search_values['-DRIVE-'])), search_values['-SEARCHING-']))
            
    #         else:
    #             search_window['-FOUND-'].update(os.listdir(os.getcwd()))
                
                
    #     search_window.close()
    #     search_up=False
        
     #--------------------------------Meghajto kivalszto ablak-----------------------------------------------    
    
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
               
    #-----------------------------Meghajto kivalasztasanal betolti a kivant asztalra--------------------------------------------------
               
            if disk_event.rfind('-BM') != -1:
               
                match disk_event:
                    case '-BM0-':
                        match disk_values['-BM0-']:
                            case 'Asztal1::-INT1-':
                                val:str = disk_window['-TX0-'].get()
                                vales:list = create_twoD_list(f'{val}/')
                                window['-TABLE01-'].update(vales)
                                os.chdir(f'{val}/')
                                window.find_element('-Organize01-').update(os.getcwd())
                                t1_ut: Jelen_EleresiUt = Jelen_EleresiUt(os.getcwd())
                            case 'Asztal2::-INT2-':
                                val:str = disk_window['-TX0-'].get()
                                vales:list = create_twoD_list(f'{val}/')
                                window['-TABLE02-'].update(vales)
                                os.chdir(f'{val}/')
                                window.find_element('-Organize02-').update(os.getcwd())
                                t2_ut: Jelen_EleresiUt = Jelen_EleresiUt(os.getcwd())
                    case '-BM1-':
                        match disk_values['-BM1-']:
                            case 'Asztal1::-INT1-':
                                 val:str = disk_window['-TX1-'].get()
                                 vales:list = create_twoD_list(f'{val}/')
                                 window['-TABLE01-'].update(vales)
                                 os.chdir(f'{val}/')
                                 window.find_element('-Organize01-').update(os.getcwd())
                                 t1_ut: Jelen_EleresiUt = Jelen_EleresiUt(os.getcwd())
                            case 'Asztal2::-INT2-':
                                val:str = disk_window['-TX1-'].get()
                                vales:list = create_twoD_list(f'{val}/')
                                window['-TABLE02-'].update(vales)
                                os.chdir(f'{val}/')
                                window.find_element('-Organize02-').update(os.getcwd())
                                t2_ut: Jelen_EleresiUt = Jelen_EleresiUt(os.getcwd())
                    case '-BM2-':
                        match disk_values['-BM2-']:
                            case 'Asztal1::-INT1-':
                                val:str = disk_window['-TX2-'].get()
                                vales:list = create_twoD_list(f'{val}/')
                                window['-TABLE01-'].update(vales)
                                os.chdir(f'{val}/')
                                window.find_element('-Organize01-').update(os.getcwd())
                                t1_ut: Jelen_EleresiUt = Jelen_EleresiUt(os.getcwd())
                            case 'Asztal2::-INT2-':
                                val:str = disk_window['-TX2-'].get()
                                vales:list = create_twoD_list(f'{val}/')
                                window['-TABLE02-'].update(vales)
                                os.chdir(f'{val}/')
                                window.find_element('-Organize02-').update(os.getcwd())
                                t2_ut: Jelen_EleresiUt = Jelen_EleresiUt(os.getcwd())
                    case '-BM3-':
                        match disk_values['-BM3-']:
                            case 'Asztal1::-INT1-':
                                val:str = disk_window['-TX3-'].get()
                                vales:list = create_twoD_list(f'{val}/')
                                window['-TABLE01-'].update(vales)
                                os.chdir(f'{val}/')
                                window.find_element('-Organize01-').update(os.getcwd())
                                t1_ut: Jelen_EleresiUt = Jelen_EleresiUt(os.getcwd())
                            case 'Asztal2::-INT2-':
                                val:str = disk_window['-TX3-'].get()
                                vales:list = create_twoD_list(f'{val}/')
                                window['-TABLE02-'].update(vales)
                                os.chdir(f'{val}/')
                                window.find_element('-Organize02-').update(os.getcwd())
                                t2_ut: Jelen_EleresiUt = Jelen_EleresiUt(os.getcwd())
                    case '-BM4-':
                        match disk_values['-BM4-']:
                            case 'Asztal1::-INT1-':
                                val:str = disk_window['-TX4-'].get()
                                vales:list = create_twoD_list(f'{val}/')
                                window['-TABLE01-'].update(vales)
                                os.chdir(f'{val}/')
                                window.find_element('-Organize01-').update(os.getcwd())
                                t1_ut: Jelen_EleresiUt = Jelen_EleresiUt(os.getcwd())
                            case 'Asztal2::-INT2-':
                                val:str = disk_window['-TX4-'].get()
                                vales:list = create_twoD_list(f'{val}/')
                                window['-TABLE02-'].update(vales)
                                os.chdir(f'{val}/')
                                window.find_element('-Organize02-').update(os.getcwd())
                                t2_ut: Jelen_EleresiUt = Jelen_EleresiUt(os.getcwd())
                    case other:
                        continue        
        disk_window.close()
        disk_selectorup = False
        
    #-------------------------------Az asztalon kijelolt elemekkel kezelese-------------------------------------------------
                
    if event in ('-TABLE01-', '-TABLE02-'):
        match event:
            case '-TABLE01-':
            
                tmp:list = window['-TABLE01-'].get().copy()
                try:
                    kijelolt_sor = [tmp [row] for row in values[event]].pop()
                except IndexError:
                    ...
                if (kijelolt_sor[1] == 'Mappa'):
                    window['-TABLE01-'].set_right_click_menu(folder_right_click)
                    window['-TABLE01-'].set_tooltip('Az enter lenyomasaval megnyithato')
                    if is_pressed('enter'):
                            
                        if os.path.exists(t1_ut.szulo) == True:
                            t1_ut.Frissites(os.path.join(t1_ut.szulo, kijelolt_sor[0]))
                            try:
                                window['-TABLE01-'].Update(values=create_twoD_list(t1_ut.szulo))
                                window.find_element('-Organize01-').update(t1_ut.szulo)
                                tmp.clear()
                                
                            except (PermissionError, FileNotFoundError, WindowsError):
                                t1_ut.SzuloUtvonal()
                                window['-TABLE01-'].Update(values=create_twoD_list(t1_ut.szulo))
                                window.find_element('-Organize01-').update(t1_ut.szulo)
                                tmp.clear()
                            
                        else:
                            t1_ut.SzuloUtvonal()
                            tmp.clear()
                else:
                    window['-TABLE01-'].set_right_click_menu(file_right_click)
                    window['-TABLE01-'].set_tooltip('Jobb klikkel a lehetosegpanel')
                    eventT1, valuesT1 = window.read()
                    handler: EventHandler 
                    handler = EventHandler(eventT1, {'fo': t1_ut.szulo, 'jelolt': kijelolt_sor[0], 'bovitmenye': kijelolt_sor[1]}).compare()
                    print(type(handler))
                    
                    tmp.clear()
            case '-TABLE02-':
                tmp:list = window['-TABLE02-'].get().copy()
                try:
                    kijelolt_sor = [tmp [row] for row in values[event]].pop()
                except IndexError:
                    ...
                if (kijelolt_sor[1] == 'Mappa'):
                    window['-TABLE02-'].set_right_click_menu(folder_right_click)
                    window['-TABLE02-'].set_tooltip('Az enter lenyomasaval megnyithato')
                    if is_pressed('enter'):
                        if os.path.exists(t2_ut.szulo) == True:
                            t2_ut.Frissites(os.path.join(t2_ut.szulo, kijelolt_sor[0]))
                            window['-TABLE02-'].Update(values=create_twoD_list(t2_ut.szulo))
                            window['-TABLE02-'].SetFocus()
                            window.find_element('-Organize02-').update(t2_ut.szulo)
                            tmp.clear()
                        else:
                            t2_ut.SzuloUtvonal()
                            tmp.clear()
                else:
                    window['-TABLE02-'].set_right_click_menu(file_right_click)
                    window['-TABLE02-'].set_tooltip('Jobb klikkel a lehetosegpanel')
                    eventT2, valuesT2 = window.read(timeout = 100)
                    
                         
                        
                    tmp.clear()
                    
    #---------------------------Az asztalon valo visszalepes kezelese---------------------------------------------------------- 
        
    if event in ('Back01', 'Back02'):
        match event:
            case 'Back01':
                t1_ut.SzuloUtvonal()
                window['-TABLE01-'].Update(values=create_twoD_list(t1_ut.szulo))
                window.find_element('-Organize01-').update(t1_ut.szulo)
            case 'Back02':
                t2_ut.SzuloUtvonal()
                window['-TABLE02-'].Update(values=create_twoD_list(t2_ut.szulo))
                window.find_element('-Organize02-').update(t2_ut.szulo)
                
                
                
    # if event in ('Megnyitas', 'Eleresi ut masolasa', 'Masolas', 'Athelyezes::-FILE-', 'Atnevezes::-FILE-'):
    #     match event:
    #         case 'Megnyitas':
    #             ...
        
    # if event in ('Masolas', '&Utvonal masolasa...', 'Athelyezes::-FOLDER-', 'Athelyezes megadott mappaba...', 'Atnevezes::-FOLDER-', 'Eltavolitas', 'Directory fa eltavolitasa...' ,'Megnyitas a masik asztalon'):
    #     ...
        
    # if event == 'Tulajdonsagok':
    #     ...
    if (event == 'r') and (eventlist[0] == 17):
        ...
        
    
    #print(f'{event} and Combo val: {com}')
window.close()
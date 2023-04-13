import os
from data.file_folder_managing import *
from gui import create_ablak, make_second_window, create_disk_window, file_or_folder_szita, folder_properties_window, file_properties_win
from data.disk_manager import kinyeres
import PySimpleGUI as psg
from keyboard import is_pressed
from collections import deque
import pyperclip
from data.path_manager import Jelen_EleresiUt
import logging
original_right_click:list = []*2
original_right_click = ['Mappa', ['Uj', ['Fajl', 'Mappa']]]
file_right_click:list = []*2
file_right_click = ['Fajl', ['Uj fajl letrehozasa','Megnyitas Writerben','Megnyitas alapertelmezett alkalmazasban', 'Eleresi ut masolasa', 'Masolas', '---','Athelyezes::-FILE-','Athelyezes megadott mappaba...::-FILE-','---', 'Atnevezes::-FILE-','---' ,'Tulajdonsagok']]
other_right_click:list = []*2
other_right_click = ['Fajl', ['Uj fajl letrehozasa','Megnyitas alapertelmezett alkalmazasban', 'Eleresi ut masolasa', 'Masolas', '---','Athelyezes::-FILE-','Athelyezes megadott mappaba...::-FILE-','---', 'Atnevezes::-FILE-','---' ,'Tulajdonsagok']]
folder_right_click:list = []*2
folder_right_click = ['Folder', ['Utvonal masolasa...','Uj', ['Uj fajl', 'Uj mappa'], 'Athelyezes::-FOLDER-', 'Athelyezes megadott mappaba...::-FOLDER-', 'Atnevezes::-FOLDER-', 'Eltavolitas', 'Konyvtar fa eltavolitasa...', '---' ,'Megnyitas a masik asztalon','---' , 'Tulajdonsagok']]
new_menu:list
new_menu = [['Uj fajl', ['Txt fajl', 'Egyeb fajl']], ['Mappa']]
writerup:bool = False
search_up:bool = False
disk_selectorup:bool = False
van_kijelolt_tabla1:bool = False
van_kijelolt_tabla2:bool = False
window_minimized:bool = False
refresh_bool:bool = False
is_saved:bool = False
refresh_num = 0

#Ablak es asztal valtozok
prop_win:psg.Window
prop_event:str;prop_val:str

#Writer_valtozok
t1_ut='';t2_ut=''

#Diszk_valtozok



os.chdir(os.path.expanduser('~'))


window = create_ablak()
window.set_icon(icon="icon/icov1.ico")
eventlist:deque = deque([])
 #--------------------------A program-----------------------------------------------------
 #  
# ██████╗░██████╗░░█████╗░░██████╗░██████╗░░█████╗░███╗░░░███╗  ░██╗░░░░░░░██╗██╗░░██╗██╗██╗░░░░░███████╗
# ██╔══██╗██╔══██╗██╔══██╗██╔════╝░██╔══██╗██╔══██╗████╗░████║  ░██║░░██╗░░██║██║░░██║██║██║░░░░░██╔════╝
# ██████╔╝██████╔╝██║░░██║██║░░██╗░██████╔╝███████║██╔████╔██║  ░╚██╗████╗██╔╝███████║██║██║░░░░░█████╗░░
# ██╔═══╝░██╔══██╗██║░░██║██║░░╚██╗██╔══██╗██╔══██║██║╚██╔╝██║  ░░████╔═████║░██╔══██║██║██║░░░░░██╔══╝░░
# ██║░░░░░██║░░██║╚█████╔╝╚██████╔╝██║░░██║██║░░██║██║░╚═╝░██║  ░░╚██╔╝░╚██╔╝░██║░░██║██║███████╗███████╗
# ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝  ░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝╚══════╝╚══════╝

# ██╗░░░░░░█████╗░░█████╗░██████╗░
# ██║░░░░░██╔══██╗██╔══██╗██╔══██╗
# ██║░░░░░██║░░██║██║░░██║██████╔╝
# ██║░░░░░██║░░██║██║░░██║██╔═══╝░
# ███████╗╚█████╔╝╚█████╔╝██║░░░░░
# ╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░
while True:
    event, values = window.read(timeout=2300)
    
    if event == psg.WIN_CLOSED:
        break
    
    if event == 'Control_L:17':
        eventlist.clear()
        eventlist.append(17)
    
    
# ░██╗░░░░░░░██╗██████╗░██╗████████╗███████╗██████╗░  ███████╗██╗░░░██╗███████╗███╗░░██╗████████╗
# ░██║░░██╗░░██║██╔══██╗██║╚══██╔══╝██╔════╝██╔══██╗  ██╔════╝██║░░░██║██╔════╝████╗░██║╚══██╔══╝
# ░╚██╗████╗██╔╝██████╔╝██║░░░██║░░░█████╗░░██████╔╝  █████╗░░╚██╗░██╔╝█████╗░░██╔██╗██║░░░██║░░░
# ░░████╔═████║░██╔══██╗██║░░░██║░░░██╔══╝░░██╔══██╗  ██╔══╝░░░╚████╔╝░██╔══╝░░██║╚████║░░░██║░░░
# ░░╚██╔╝░╚██╔╝░██║░░██║██║░░░██║░░░███████╗██║░░██║  ███████╗░░╚██╔╝░░███████╗██║░╚███║░░░██║░░░
# ░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ╚══════╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░░░╚═╝░░░
    
    if (event == 'Writer' and writerup == False) or (event == 'w' and eventlist[0] == 17 and writerup == False ):
        eventlist.clear()
        writerup = True
        writer_window = make_second_window()
        while True:
            writer_event, writer_values = writer_window.read(timeout=100)
            used_path = ''
            used_file = writer_window.find_element('-WRITER-NAME-').get()
           
            if writer_event in ('X', psg.WIN_CLOSED) and (is_saved == False) or (event == None):
                match writer_values['-MULTI-']:
                    case '':
                        break
                    case other:
                        made = psg.popup_yes_no('Biztos benne hogy mentes nelkul szeretne bezarni?')
                        match made:
                            case 'Yes':
                                break
                            case 'No':
                                continue
            elif writer_event in ('X', psg.WIN_CLOSED) and (is_saved == True) or (event == None):
                break
            is_saved = True
            writer_window['-MULTI-'].update(disabled = False)
            writer_window['-ENABLE-MODIFY-'].update(visible = False)
            if writer_event == 'Control_L:17':
                    key_event, key_values = writer_window.read(100)
                    if key_event == 'z' and is_saved == False:
                        want_to_close:str = psg.popup_yes_no('Biztos benne hogy mentes nelkul szeretne bezarni?') 
                        match want_to_close:
                            case 'Yes':
                                break
                            case 'No':
                                continue
                    elif key_event == 'z' and is_saved == True:
                        break
                    if key_event == 's':
                        if (used_file == 'untitled.txt') and (is_saved == False):
                            save_place = psg.popup_get_folder('Valassza ki a menteni kivant fajl helyet!')
                            save_name = psg.popup_get_text('Irja be a fajl nevet es bovitmenyet! (fajl.txt)')
                            f, b = os.path.splitext(save_name)
                            if save_place != '' and save_name != '' and f != '' and b != '':
                                match os.path.exists(os.path.join(save_place, save_name)):
                                    case True:
                                        psg.popup_cancel('Ilyen fajl mar letezik!')
                                    case False:
                                        out_message = create_file(save_place, save_name, writer_window['-ENCODED-VAL-'].get(), writer_window['-MULTI-'].get().expandtabs(4))
                                        psg.popup_ok(out_message)
                                        is_saved = True
                                        writer_window['-WRITER-NAME-'].update(save_name)
                                    case other:
                                        ...
                            else:
                                psg.popup_ok('Nem megfelelo adatok lettek megadva!')
                                match save_place:
                                    case '':
                                        psg.popup_ok('Hianyzo utvonal!')
                                        continue
                                    case other:
                                        match f:
                                            case '':
                                                psg.popup_ok('Hianyzo fajlnev!')
                                                used_path = save_place
                                                continue
                                            case other:
                                                match b:
                                                    case '':
                                                        psg.popup_ok('Hianyzo bovitmeny!')
                                                        continue
                                                    case other:
                                                        is_saved = True
                                                        continue
                        elif (used_file != 'untitled.txt') and (is_saved == False):
                            out_message = overwriting_existing_file(used_path, writer_window['-WRITER-NAME-'].get(), writer_window['-ENCODED-VAL-'].get(), writer_window['-MULTI-'].get().expandtabs(4))
                            is_saved = True
                        else:
                            continue
                    if key_event == 'v':
                        pyperclip.paste()
                    if key_event == 'c':
                        pyperclip.copy()
            if writer_event == 'Megnyitas':
                opening_file = psg.popup_get_file('Kerem adja meg a fajl eleresi utjat!')
                match os.path.exists(opening_file):
                    case True:
                        match os.path.isfile(opening_file):
                            case True:
                                fajl_text, encoding = open_file(opening_file)
                                used_path, used_file = os.path.split(opening_file)
                                writer_window['-MULTI-'].Update(fajl_text)
                                writer_window['-ENCODED-VAL-'].Update(encoding)
                                writer_window['-WRITER-NAME-'].Update(used_file)
                                is_saved = True
                            case False:
                                psg.popup_ok('Nem fajlt adott meg!')
                    case False:
                        psg.popup_ok('Nem letezo eleresi ut!')
            
            match writer_event:
                case 'Beillesztes':
                    w_val = writer_window['-MULTI-'].get()
                    writer_window['-MULTI-'].update(f'{w_val} {pyperclip.paste()}')
                    w_val = ''
                case 'Masolas':
                    pyperclip.copy(writer_window['-MULTI-'].get().expandtabs(4))
                case '-MULTI-':
                    is_saved = False
                    
            if writer_event in ('Mentes', '.txt', '.py', '.html', '.js' ,'-MULTI-'):
                match writer_event:
                    case 'Mentes':
                        if (used_path != '') or (writer_window['-WRITER-NAME-'].get() != 'untitled.txt'):
                            if os.path.exists(os.path.join(used_path,f'{fajl}{bov}')):
                                out_message = overwriting_existing_file(used_path, writer_window['-WRITER-NAME-'].get(), writer_window['-ENCODED-VAL-'].get(), writer_window['-MULTI-'].get().expandtabs(4))
                                psg.popup_ok(out_message)
                                is_saved = True
                        else:
                            used_path:str = psg.popup_get_folder('Kerem adja meg a mappat ahova menteni szeretne!', title='Nem lett megadva mappa!')
                            used_file:str = psg.popup_get_text('Kerem adja meg a menteni kivant fajl nevet es bovitmenyet! (fajl.txt)')
                            match used_path:
                                case '':
                                    psg.popup_ok('Nem lett mappa megadva!', title='Hiba')
                                case other:
                                    fajl, bov = os.path.splitext(used_file)
                                    if fajl != '':
                                        match bov:
                                            case '':
                                                if os.path.exists(os.path.join(used_path,f'{fajl}.txt')):
                                                    out_message = overwriting_existing_file(used_path, writer_window['-WRITER-NAME-'].get(), writer_window['-ENCODED-VAL-'].get(), writer_window['-MULTI-'].get().expandtabs(4))
                                                    psg.popup_ok(out_message)
                                                    is_saved = True
                                            case other:
                                                if os.path.exists(os.path.join(used_path,f'{fajl}{bov}')):
                                                    out_message = overwriting_existing_file(used_path, writer_window['-WRITER-NAME-'].get(), writer_window['-ENCODED-VAL-'].get(), writer_window['-MULTI-'].get().expandtabs(4))
                                                    psg.popup_ok(out_message)
                                                    is_saved = True
                                    else:
                                        psg.popup_ok('Nem lett megadva fajlnev')
                                    
                    case '.txt':
                        save_place = psg.popup_get_folder('Valassza ki a menteni kivant fajl helyet!')
                        save_name = psg.popup_get_text('Irja be a fajl nevet! (fajl.txt)')
                        if save_place != '' and save_name != '':
                            match os.path.exists(os.path.join(save_place, f'{save_name}.txt')):
                                case True:
                                    psg.popup_cancel('Ilyen fajl mar letezik!')
                                    continue
                                case False:
                                    out_message = create_file(save_place, f'{save_name}.txt', writer_window['-ENCODED-VAL-'].get(), writer_window['-MULTI-'].get().expandtabs(4))
                                    psg.popup_ok(out_message)
                                    is_saved = True
                                    writer_window['-WRITER-NAME-'].update(save_name)
                        else:
                            match save_place:
                                case '':
                                    psg.popup_ok('Hianyzo utvonal!')
                                case other:
                                    match save_name:
                                        case '':
                                            psg.popup_ok('Hianyzo fajlnev')
                                        case other:
                                            continue
                    case '.py':
                        save_place = psg.popup_get_folder('Valassza ki a menteni kivant fajl helyet!')
                        save_name = psg.popup_get_text('Irja be a fajl nevet! (fajl.py)')
                        if save_place != '' and save_name != '':
                            match os.path.exists(os.path.join(save_place, f'{save_name}.py')):
                                case True:
                                    psg.popup_cancel('Ilyen fajl mar letezik!')
                                    continue
                                case False:
                                    out_message = create_file(save_place, f'{save_name}.py', writer_window['-ENCODED-VAL-'].get(), writer_window['-MULTI-'].get().expandtabs(4))
                                    psg.popup_ok(out_message)
                                    is_saved = True
                                    writer_window['-WRITER-NAME-'].update(save_name)
                        else:
                            match save_place:
                                case '':
                                    psg.popup_ok('Hianyzo utvonal!')
                                case other:
                                    match save_name:
                                        case '':
                                            psg.popup_ok('Hianyzo fajlnev')
                                        case other:
                                            continue
                    case '.html':
                        save_place = psg.popup_get_folder('Valassza ki a menteni kivant fajl helyet!')
                        save_name = psg.popup_get_text('Irja be a fajl nevet! (fajl.html)')
                        if save_place != '' and save_name != '':
                            match os.path.exists(os.path.join(save_place, f'{save_name}.html')):
                                case True:
                                    psg.popup_cancel('Ilyen fajl mar letezik!')
                                    continue
                                case False:
                                    out_message = create_file(save_place, f'{save_name}.html', writer_window['-ENCODED-VAL-'].get(), writer_window['-MULTI-'].get().expandtabs(4))
                                    psg.popup_ok(out_message)
                                    is_saved = True
                                    writer_window['-WRITER-NAME-'].update(save_name)
                        else:
                            match save_place:
                                case '':
                                    psg.popup_ok('Hianyzo utvonal!')
                                case other:
                                    match save_name:
                                        case '':
                                            psg.popup_ok('Hianyzo fajlnev')
                                        case other:
                                            continue
                    case '.js':
                        save_place = psg.popup_get_folder('Valassza ki a menteni kivant fajl helyet!')
                        save_name = psg.popup_get_text('Irja be a fajl nevet! (fajl.js)')
                        if save_place != '' and save_name != '':
                            match os.path.exists(os.path.join(save_place, f'{save_name}.js')):
                                case True:
                                    psg.popup_cancel('Ilyen fajl mar letezik!')
                                    continue
                                case False:
                                    out_message = create_file(save_place, f'{save_name}.js', writer_window['-ENCODED-VAL-'].get(), writer_window['-MULTI-'].get().expandtabs(4))
                                    psg.popup_ok(out_message)
                                    is_saved = True
                                    writer_window['-WRITER-NAME-'].update(save_name)
                        else:
                            match save_place:
                                case '':
                                    psg.popup_ok('Hianyzo utvonal!')
                                case other:
                                    match save_name:
                                        case '':
                                            psg.popup_ok('Hianyzo fajlnev')
                                        case other:
                                            continue
            
            
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
    
    
# ██████╗░██╗░██████╗██╗░░██╗  ░██████╗███████╗██╗░░░░░███████╗░█████╗░████████╗░█████╗░██████╗░
# ██╔══██╗██║██╔════╝██║░██╔╝  ██╔════╝██╔════╝██║░░░░░██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
# ██║░░██║██║╚█████╗░█████═╝░  ╚█████╗░█████╗░░██║░░░░░█████╗░░██║░░╚═╝░░░██║░░░██║░░██║██████╔╝
# ██║░░██║██║░╚═══██╗██╔═██╗░  ░╚═══██╗██╔══╝░░██║░░░░░██╔══╝░░██║░░██╗░░░██║░░░██║░░██║██╔══██╗
# ██████╔╝██║██████╔╝██║░╚██╗  ██████╔╝███████╗███████╗███████╗╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║
# ╚═════╝░╚═╝╚═════╝░╚═╝░░╚═╝  ╚═════╝░╚══════╝╚══════╝╚══════╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
    eventlist.append(0)
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
            
            

# ████████╗░█████╗░██████╗░██╗░░░░░███████╗  ░█████╗░░░███╗░░  ███╗░░░███╗███████╗████████╗██╗░░██╗░█████╗░██████╗░
# ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝  ██╔══██╗░████║░░  ████╗░████║██╔════╝╚══██╔══╝██║░░██║██╔══██╗██╔══██╗
# ░░░██║░░░███████║██████╦╝██║░░░░░█████╗░░  ██║░░██║██╔██║░░  ██╔████╔██║█████╗░░░░░██║░░░███████║██║░░██║██║░░██║
# ░░░██║░░░██╔══██║██╔══██╗██║░░░░░██╔══╝░░  ██║░░██║╚═╝██║░░  ██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══██║██║░░██║██║░░██║
# ░░░██║░░░██║░░██║██████╦╝███████╗███████╗  ╚█████╔╝███████╗  ██║░╚═╝░██║███████╗░░░██║░░░██║░░██║╚█████╔╝██████╔╝
# ░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚══════╝╚══════╝  ░╚════╝░╚══════╝  ╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═════╝░
# ░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚══════╝╚══════╝  ░╚════╝░╚══════╝
            
            #------------------------------Asztal 1 metodusok---------------------------
            
            case '-TABLE01-':
                # kijelolt_sor01:list = []
                window['-TABLE01-'].set_right_click_menu(original_right_click)
                tmp:list = window['-TABLE01-'].get().copy()
                kijelolt_sor = []
                
                    # meghatarozzuk melyik sorba lett kattintva Asztal1 en
                
                try:
                    kijelolt_sor = [tmp [row] for row in values[event]].pop()
                except IndexError:
                    kijelolt_sor = [0,0,0,0]
                    
                    # meghatarozzuk hogy a sorban levo elem mappa vagy sem ha igen, figyeljuk az esemenyeket
                    
                if (kijelolt_sor[1] == 'Mappa'):
                    window['-TABLE01-'].set_right_click_menu(folder_right_click)
                    window['-TABLE01-'].set_tooltip('Az enter lenyomasaval megnyithato')
                    
                        #ha a sorban levo elem ki van jelolve es enter billentyu lenyomva toltse ujra az asztalt az uj ertekekkel
                    
                    if is_pressed('enter'):
                            
                        if os.path.exists(t1_ut.szulo) == True:
                            t1_ut.Frissites(os.path.join(t1_ut.szulo, kijelolt_sor[0]))
                            try:
                                window['-TABLE01-'].Update(values=create_twoD_list(t1_ut.szulo))
                                window.find_element('-Organize01-').update(t1_ut.szulo)
                                tmp.clear()
                                
                                # ha tortent egy rendszrebeli hiba, mint elutasitott kerelem, terjen vissza a szulo utvonalhoz es toltse vissza
                                
                            except (PermissionError, FileNotFoundError, WindowsError):
                                t1_ut.SzuloUtvonal()
                                window['-TABLE01-'].Update(values=create_twoD_list(t1_ut.szulo))
                                window.find_element('-Organize01-').update(t1_ut.szulo)
                                tmp.clear()
                            
                        else:
                            t1_ut.SzuloUtvonal()
                            tmp.clear()
                    event_folder1, _ = window.read() 
                    
                    if event_folder1 == 'Utvonal masolasa...':
                        mappa = kijelolt_sor[0]
                        if os.path.exists(os.path.join(t1_ut.szulo, f'{mappa}')):
                            pyperclip.copy(f'{os.path.normcase(os.path.join(t1_ut.szulo, mappa))}')
                            psg.popup_notify('Copied to clipboard', title='Copied')
                            mappa = ''
                            
                    match event_folder1:
                        case 'Uj fajl':
                            used_path:str = t1_ut.szulo
                            used_file:str = psg.popup_get_text('Kerem adja meg a menteni kivant fajl nevet es bovitmenyet! (fajl.txt)')
                            match used_path:
                                case '':
                                    psg.popup_ok('Nem lett mappa megadva!', title='Hiba')
                                case other:
                                    fajl, bov = os.path.splitext(used_file)
                                    if fajl != '':
                                        match bov:
                                            case '':
                                                if os.path.exists(os.path.join(used_path,f'{fajl}.txt')):
                                                    out_message = creating_file_without_value(used_path, f'{used_file}.txt', 'utf-8')
                                                    psg.popup_ok(out_message)
                                                    refresh_bool = True
                                                    refresh_num = 1
                                            case other:
                                                if os.path.exists(os.path.join(used_path,f'{fajl}{bov}')):
                                                    out_message = creating_file_without_value(used_path, f'{used_file}{bov}', 'utf-8', '')
                                                    psg.popup_ok(out_message, title='Letrehozas')
                                                    refresh_bool = True
                                                    refresh_num = 1
                                    else:
                                        psg.popup_ok('Nem lett megadva fajlnev')
                        case 'Uj mappa':
                            used_path = t1_ut.szulo
                            used_dir = psg.popup_get_text('Kerem adja meg a menteni kivant mappa megnevezeset!')
                            message_out = creating_folder(used_path, used_dir)
                            psg.popup_notify(message_out, title='Letrehozas')
                            refresh_bool = True
                            refresh_num = 1
                        case 'Athelyezes::-FOLDER-':
                            match t2_ut.szulo:
                                case '':
                                    psg.popup_ok('A masik asztalon nincs megnyitva mappa!', title='Asztal 1')
                                case other:
                                    used_path = t1_ut.szulo
                                    used_dir = kijelolt_sor[0]
                                    reg_path = os.path.join(used_path,used_dir)
                                    
                        case 'Athelyezes megadott mappaba...::-FOLDER-':
                            ...
                        case 'Atnevezes::-FOLDER-':
                            real_path, real_dir, = t1_ut.szulo, kijelolt_sor[0]
                            val = psg.popup_get_text('A fajl atnevezese:', default_text=f'{real_dir}', keep_on_top=True)
                            if val != f'{real_dir}' and val != '' and val != None:
                                message_out = renaming(os.path.join(real_path, f'{real_dir}'), os.path.join(real_path, val))
                                psg.popup_notify(message_out, title='Atnevezes')
                                refresh_bool = True
                                refresh_num = 1
                                tmp:list = window['-TABLE01-'].get().copy()
                                kijelolt_sor = [tmp [row] for row in values[event]].pop()
                                tmp.clear()
                            else:
                                psg.popup_notify('Atnevezes nem tortent!', title='Atnevezes')
                        case 'Eltavolitas':
                            try:
                                os.rmdir(os.path.join(t1_ut.szulo, kijelolt_sor[0]))
                                psg.popup_notify('Eltavolitas megtortent!')
                                refresh_bool = True
                                refresh_num = 1
                            except OSError as e:
                                psg.popup_notify('Kerem hasznalja a Konyvtar fa eltavolitasa lehetoseget', title='A konyvtar nem ures!')
                        case 'Konyvtar fa eltavolitasa...':
                            mappa = kijelolt_sor[0]
                            choice = psg.popup_get_text(f'El szeretne tavolitani a {mappa} elemet? Valaszlehetoseg: (yes/no)', title='Delete')
                            match choice:
                                case None:
                                    psg.popup_notify('Cancelled!')
                                case '':
                                    psg.popup_notify('No choice!')
                                case 'yes':
                                    message_out = remove_tree(os.path.join(t2_ut.szulo, mappa))
                                    psg.popup_notify(message_out)
                                    refresh_bool = True
                                    refresh_num = 1
                                case 'no':
                                    psg.popup_notify('Cancelled!')
                                case other:
                                    psg.popup_notify('Cancelled!')
                            fajl, bov = '', ''
                        case 'Megnyitas a masik asztalon':
                            window['-TABLE02-'].Update(create_twoD_list(os.path.join(t1_ut.szulo, kijelolt_sor[0])))
                            window['-Organize02-'].Update(os.path.join(t1_ut.szulo, kijelolt_sor[0]))
                            t2_ut:Jelen_EleresiUt = Jelen_EleresiUt(os.path.join(t1_ut.szulo, kijelolt_sor[0]))
                    
                    if event_folder1 == 'Tulajdonsagok':
                        prop_win = folder_properties_window(os.path.join(t1_ut.szulo, kijelolt_sor[0]))
                        while True:
                            prop_event, _ = prop_win.read()
                            if prop_event == psg.WIN_CLOSED:
                                break
                        prop_win.close()
                else:
                    
                    # ha a kijelolt sorban levo elem fajl -> figyelje az eventeket 
                    # /// tovabba ha a kijelolt fajl '.txt', '.py', '.md', '.js', '.log' 
                    # kiterjesztesu, valtoztasson jobb klikk menut
                    # a jobb klikk menubol meg lehet nyitni majd a Writerben a fajlt 
                    
                    if kijelolt_sor[1] in ('.txt', '.py', '.md', '.js', '.log'):
                        window['-TABLE01-'].set_right_click_menu(file_right_click)
                    else:
                         window['-TABLE01-'].set_right_click_menu(other_right_click)
                    window['-TABLE01-'].set_tooltip('Jobb klikkel a lehetosegpanel')
                    eventT1, _ = window.read()
                    
                        # kiegesziteskent hozzaadtunk billentyukombinaciokat 
                        # az egyszerubb elereshez
                    
                    if eventT1 == 'Control_L:17':
                        print(eventT1)
                        control_event, _ = window.read()
                        print(control_event)
                        match control_event:
                            case 'o':
                                try:
                                    fajl, bov = kijelolt_sor[0], kijelolt_sor[1]
                                    fajlnev = f'{fajl}{bov}'
                                    os.startfile(os.path.join(t1_ut.szulo, fajlnev), 'open')
                                    fajl, bov = '', ''
                                except OSError as e:
                                    psg.popup_notify( f'{bov} cannot be opened and exception {e}' ,title='No program to open')
                                    fajl, bov = '', ''
                            case 'x':
                                fajl, bov = kijelolt_sor[0], kijelolt_sor[1]
                                choice = psg.popup_get_text(f'El szeretne tavolitani a {fajl}{bov} elemet? Valaszlehetoseg: (yes/no)', title='Delete')
                                match choice:
                                    case None:
                                        psg.popup_notify('Cancelled!')
                                    case '':
                                        psg.popup_notify('No choice!')
                                    case 'yes':
                                        remove_folder_or_file(2, os.path.join(t1_ut.szulo, f'{fajl}{bov}'))
                                        psg.popup_notify('Deleted!')
                                    case 'no':
                                        psg.popup_notify('Cancelled!')
                                    case other:
                                        psg.popup_notify('Cancelled!')
                                fajl, bov = '', ''
                                        
                                        #billentyukombinaciok tesztelese utan a jobb klikk esemenyek tesztelese
                                        
                    if eventT1 in ('Athelyezes megadott mappaba...::-FILE-', 'Athelyezes::-FILE-', 'Atnevezes::-FILE-'):
                        match eventT1:
                            case 'Athelyezes::-FILE-':
                                ...
                            case 'Athelyezes megadott mappaba...::-FILE-':
                                ...
                            case 'Atnevezes::-FILE-':
                                real_path, head, tail = t1_ut.szulo, kijelolt_sor[0], kijelolt_sor[1]
                                val = psg.popup_get_text('A fajl atnevezese:', default_text=f'{head}{tail}', keep_on_top=True,)
                                if val != f'{head}{tail}' and val != '' and val != None:
                                    message_out = renaming(os.path.join(real_path, f'{head}{tail}'), os.path.join(real_path, val))
                                    psg.popup_notify(message_out)
                                    refresh_bool = True
                                    refresh_num = 1
                                    tmp:list = window['-TABLE01-'].get().copy()
                                    kijelolt_sor = [tmp [row] for row in values[event]].pop()
                                    tmp.clear()
                                else:
                                    psg.popup_notify('Atnevezes nem tortent!', title='Atnevezes')
                    if eventT1 in ('Megnyitas Writerben', 'Eleresi ut masolasa', 'Masolas', 'Megnyitas alapertelmezett alkalmazasban'):
                        match eventT1:
                            case 'Megnyitas Writerben':
                                fajl, bov = kijelolt_sor[0], kijelolt_sor[1]
                                if os.path.exists(os.path.join(t1_ut.szulo, f'{fajl}{bov}')):
                                    fajl_text, encoded_var = open_file(os.path.join(t1_ut.szulo, f'{fajl}{bov}'))
                                    is_saved = True
                                    writer_window = make_second_window(fajl_text)
                                    while True:
                                        writerup = True
                                        eventw, valuew = writer_window.read(timeout=100)
                                        if eventw in  (psg.WIN_CLOSED, 'X') and is_saved == False:
                                            match valuew['-MULTI-']:
                                                case '':
                                                    break
                                                case other:
                                                    made = psg.popup_ok_cancel('Biztos benne hogy mentes nelkul szeretne bezarni?')
                                                    match made:
                                                        case 'OK':
                                                            break
                                                        case 'Cancel':
                                                            continue
                                        elif eventw in  (psg.WIN_CLOSED, 'X') and is_saved == True:
                                            break
                                        used_path = t1_ut.szulo
                                        used_file = writer_window['-WRITER-NAME-'].get()
                                        if eventw == 'Control_L:17':
                                            key_event, key_values = writer_window.read(100)
                                            if key_event == 'z' and is_saved == False:
                                                want_to_close:str = psg.popup_yes_no('Biztos benne hogy mentes nelkul szeretne bezarni?') 
                                                match want_to_close:
                                                    case 'Yes':
                                                        break
                                                    case 'No':
                                                        continue
                                            elif key_event == 'z' and is_saved == True:
                                                break
                                            if key_event == 's':
                                                if (used_file == 'untitled.txt') and (is_saved == False):
                                                    save_place = psg.popup_get_folder('Valassza ki a menteni kivant fajl helyet!')
                                                    save_name = psg.popup_get_text('Irja be a fajl nevet es bovitmenyet! (fajl.txt)')
                                                    f, b = os.path.splitext(save_name)
                                                    if save_place != '' and save_name != '' and f != '' and b != '':
                                                        match os.path.exists(os.path.join(save_place, save_name)):
                                                            case True:
                                                                psg.popup_cancel('Ilyen fajl mar letezik!')
                                                            case False:
                                                                out_message = create_file(save_place, save_name, writer_window['-ENCODED-VAL-'].get(), writer_window['-MULTI-'].get().expandtabs(4))
                                                                psg.popup_ok(out_message)
                                                                is_saved = True
                                                                writer_window['-WRITER-NAME-'].update(save_name)
                                                            case other:
                                                                ...
                                                    else:
                                                        psg.popup_ok('Nem megfelelo adatok lettek megadva!')
                                                        match save_place:
                                                            case '':
                                                                psg.popup_ok('Hianyzo utvonal!')
                                                                continue
                                                            case other:
                                                                match f:
                                                                    case '':
                                                                        psg.popup_ok('Hianyzo fajlnev!')
                                                                        used_path = save_place
                                                                        continue
                                                                    case other:
                                                                        match b:
                                                                            case '':
                                                                                psg.popup_ok('Hianyzo bovitmeny!')
                                                                                continue
                                                                            case other:
                                                                                is_saved = True
                                                                                continue
                                                elif (used_file != 'untitled.txt') and (is_saved == False):
                                                    out_message = overwriting_existing_file(used_path, writer_window['-WRITER-NAME-'].get(), writer_window['-ENCODED-VAL-'].get(), writer_window['-MULTI-'].get().expandtabs(4))
                                                    is_saved = True
                                                else:
                                                    continue
                                            if key_event == 'v':
                                                pyperclip.paste()
                                            if key_event == 'c':
                                                pyperclip.copy()
                                        
                                        writer_window['-WRITER-NAME-'].update(f'{fajl}{bov}')
                                        writer_window['-ENCODED-VAL-'].update(encoded_var)
                                        writer_window['-SELECT-SAVE-'].Update(['Mentes', ['!Mentes', 'Mentes mint', ['!.txt', '!.py', '!&.html', '!&.js', ]]])
                                        if eventw == '-ENABLE-MODIFY-':
                                            writer_window['-MULTI-'].update(disabled = False)
                                            writer_window['-ENABLE-MODIFY-'].update(visible = False)
                                            writer_window['-SELECT-SAVE-'].Update(['Mentes', ['Mentes', 'Mentes mint', ['!.txt', '!.py', '!&.html', '!&.js', ]]])
                                            
                                        if eventw in ('Mentes', '.txt', '.py', '.html', '.js' ,'-MULTI-'):
                                            match eventw:
                                                case 'Mentes':
                                                    if os.path.exists(os.path.join(t1_ut.szulo,f'{fajl}{bov}')):
                                                        out_message = overwriting_existing_file(used_path, writer_window['-WRITER-NAME-'].get(), writer_window['-ENCODED-VAL-'].get(), writer_window['-MULTI-'].get().expandtabs(4))
                                                        psg.popup_ok(out_message)
                                                        is_saved = True
                                                case '.txt':
                                                    save_place = psg.popup_get_folder('Valassza ki a menteni kivant fajl helyet!')
                                                    save_name = psg.popup_get_text('Irja be a fajl nevet! (fajl.txt)')
                                                    if save_place != '' and save_name != '':
                                                        match os.path.exists(os.path.join(save_place, f'{save_name}.txt')):
                                                            case True:
                                                                psg.popup_cancel('Ilyen fajl mar letezik!')
                                                                continue
                                                            case False:
                                                                out_message = create_file(save_place, f'{save_name}.txt', writer_window['-ENCODED-VAL-'].get(), writer_window['-MULTI-'].get().expandtabs(4))
                                                                psg.popup_ok(out_message)
                                                                is_saved = True
                                                                writer_window['-WRITER-NAME-'].update(save_name)
                                                    else:
                                                        match save_place:
                                                            case '':
                                                                psg.popup_ok('Hianyzo utvonal!')
                                                            case other:
                                                                match save_name:
                                                                    case '':
                                                                        psg.popup_ok('Hianyzo fajlnev')
                                                                    case other:
                                                                        continue
                                                case '.py':
                                                    save_place = psg.popup_get_folder('Valassza ki a menteni kivant fajl helyet!')
                                                    save_name = psg.popup_get_text('Irja be a fajl nevet! (fajl.py)')
                                                    if save_place != '' and save_name != '':
                                                        match os.path.exists(os.path.join(save_place, f'{save_name}.py')):
                                                            case True:
                                                                psg.popup_cancel('Ilyen fajl mar letezik!')
                                                                continue
                                                            case False:
                                                                out_message = create_file(save_place, f'{save_name}.py', writer_window['-ENCODED-VAL-'].get(), writer_window['-MULTI-'].get().expandtabs(4))
                                                                psg.popup_ok(out_message)
                                                                is_saved = True
                                                                writer_window['-WRITER-NAME-'].update(save_name)
                                                    else:
                                                        match save_place:
                                                            case '':
                                                                psg.popup_ok('Hianyzo utvonal!')
                                                            case other:
                                                                match save_name:
                                                                    case '':
                                                                        psg.popup_ok('Hianyzo fajlnev')
                                                                    case other:
                                                                        continue
                                                case '.html':
                                                    save_place = psg.popup_get_folder('Valassza ki a menteni kivant fajl helyet!')
                                                    save_name = psg.popup_get_text('Irja be a fajl nevet! (fajl.html)')
                                                    if save_place != '' and save_name != '':
                                                        match os.path.exists(os.path.join(save_place, f'{save_name}.html')):
                                                            case True:
                                                                psg.popup_cancel('Ilyen fajl mar letezik!')
                                                                continue
                                                            case False:
                                                                out_message = create_file(save_place, f'{save_name}.html', writer_window['-ENCODED-VAL-'].get(), writer_window['-MULTI-'].get().expandtabs(4))
                                                                psg.popup_ok(out_message)
                                                                is_saved = True
                                                                writer_window['-WRITER-NAME-'].update(save_name)
                                                    else:
                                                        match save_place:
                                                            case '':
                                                                psg.popup_ok('Hianyzo utvonal!')
                                                            case other:
                                                                match save_name:
                                                                    case '':
                                                                        psg.popup_ok('Hianyzo fajlnev')
                                                                    case other:
                                                                        continue
                                                case '.js':
                                                    save_place = psg.popup_get_folder('Valassza ki a menteni kivant fajl helyet!')
                                                    save_name = psg.popup_get_text('Irja be a fajl nevet! (fajl.js)')
                                                    if save_place != '' and save_name != '':
                                                        match os.path.exists(os.path.join(save_place, f'{save_name}.js')):
                                                            case True:
                                                                psg.popup_cancel('Ilyen fajl mar letezik!')
                                                                continue
                                                            case False:
                                                                out_message = create_file(save_place, f'{save_name}.js', writer_window['-ENCODED-VAL-'].get(), writer_window['-MULTI-'].get().expandtabs(4))
                                                                psg.popup_ok(out_message)
                                                                is_saved = True
                                                                writer_window['-WRITER-NAME-'].update(save_name)
                                                    else:
                                                        match save_place:
                                                            case '':
                                                                psg.popup_ok('Hianyzo utvonal!')
                                                            case other:
                                                                match save_name:
                                                                    case '':
                                                                        psg.popup_ok('Hianyzo fajlnev')
                                                                    case other:
                                                                        continue
                                                case '-MULTI-':
                                                    is_saved = False
                                    
                                    writerup = False
                                    writer_window.close()
                                    fajl, bov = '', ''
                            
                            case 'Eleresi ut masolasa':
                                fajl, bov = kijelolt_sor[0], kijelolt_sor[1]
                                if os.path.exists(os.path.join(t1_ut.szulo, f'{fajl}{bov}')):
                                    pyperclip.copy(f'{os.path.normcase(os.path.join(t1_ut.szulo, fajl))}{bov}')
                                    psg.popup_notify('Copied to clipboard', title='Copied')
                                    fajl, bov = '', ''
                            case 'Masolas':
                                ...
                            case 'Megnyitas alapertelmezett alkalmazasban':
                                try:
                                    fajl, bov = kijelolt_sor[0], kijelolt_sor[1]
                                    fajlnev = f'{fajl}{bov}'
                                    os.startfile(os.path.join(t1_ut.szulo, fajlnev), 'open')
                                    fajl, bov = '', ''
                                except OSError as e:
                                    psg.popup_notify( f'{bov} cannot be opened and exception {e}' ,title='No program to open') 
                                    fajl, bov = '', ''    
                                    
                    if eventT1 == 'Tulajdonsagok':
                        prop_win = file_properties_win(os.path.join(t1_ut.szulo, f'{kijelolt_sor[0]}{kijelolt_sor[1]}'), kijelolt_sor[3], kijelolt_sor[2])
                        to_rename = ''
                        while True:
                            prop_event, prop_val = prop_win.read()
                            if prop_event == psg.WIN_CLOSED:
                                break
                            prop_win['-RENAMER-FILE-'].set_cursor()
                            if prop_event == '-RENAMER-FILE-':
                                to_rename = prop_win['-RENAMER-FILE-'].get()
                        prop_win.close()
                        if (to_rename != f'{kijelolt_sor[0]}') and (to_rename != ''):
                            ev = psg.popup_yes_no('Szeretne atnevezni a mappat?')
                            match ev:
                                case 'Yes': 
                                    renaming(os.path.join(t1_ut.szulo,f'{kijelolt_sor[0]}{kijelolt_sor[1]}'), os.path.join(t1_ut.szulo, f'{to_rename}{kijelolt_sor[1]}'))
                                    psg.popup_notify('Atnevezes megtortent!')
                                    refresh_bool = True
                                    refresh_num = 1
                                    tmp:list = window['-TABLE01-'].get().copy()
                                    kijelolt_sor = [tmp [row] for row in values[event]].pop()
                                    tmp.clear()
                                    
                                case 'No':
                                    psg.popup_notify('Nem lett atnevezve!')
                    to_rename = '' 
                    tmp.clear()
                    
                    

# ████████╗░█████╗░██████╗░██╗░░░░░███████╗  ░█████╗░██████╗░  ███╗░░░███╗███████╗████████╗██╗░░██╗░█████╗░██████╗░
# ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝  ██╔══██╗╚════██╗  ████╗░████║██╔════╝╚══██╔══╝██║░░██║██╔══██╗██╔══██╗
# ░░░██║░░░███████║██████╦╝██║░░░░░█████╗░░  ██║░░██║░░███╔═╝  ██╔████╔██║█████╗░░░░░██║░░░███████║██║░░██║██║░░██║
# ░░░██║░░░██╔══██║██╔══██╗██║░░░░░██╔══╝░░  ██║░░██║██╔══╝░░  ██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══██║██║░░██║██║░░██║
# ░░░██║░░░██║░░██║██████╦╝███████╗███████╗  ╚█████╔╝███████╗  ██║░╚═╝░██║███████╗░░░██║░░░██║░░██║╚█████╔╝██████╔╝
# ░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚══════╝╚══════╝  ░╚════╝░╚══════╝  ╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═════╝░
                    
                    #------------------------------Asztal 2 metodusok---------------------------
                    
            case '-TABLE02-':
                tmp:list = window['-TABLE02-'].get().copy()
                kijelolt_sor = []
                try:
                    kijelolt_sor = [tmp [row] for row in values[event]].pop()
                except IndexError:
                    kijelolt_sor = [0,0,0,0]
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
                            
                    event_folder2, _ = window.read()
                    if event_folder2 == 'Utvonal masolasa...':
                        mappa = kijelolt_sor[0]
                        if os.path.exists(os.path.join(t2_ut.szulo, f'{mappa}')):
                            pyperclip.copy(f'{os.path.normcase(os.path.join(t2_ut.szulo, mappa))}')
                            psg.popup_notify('Copied to clipboard', title='Copied')
                            mappa = ''
                            
                    match event_folder2:
                        case 'Athelyezes::-FOLDER-':
                            ...
                        case 'Athelyezes megadott mappaba...::-FOLDER-':
                            ...
                        case 'Atnevezes::-FOLDER-':
                            real_path, real_dir, = t2_ut.szulo, kijelolt_sor[0]
                            val = psg.popup_get_text('A fajl atnevezese:', default_text=f'{real_dir}', keep_on_top=True)
                            if val != f'{real_dir}' and val != '' and val != None:
                                message_out = renaming(os.path.join(real_path, f'{real_dir}'), os.path.join(real_path, val))
                                psg.popup_notify(message_out, title='Atnevezes')
                                refresh_bool = True
                                refresh_num = 2
                                tmp:list = window['-TABLE02-'].get().copy()
                                kijelolt_sor = [tmp [row] for row in values[event]].pop()
                                tmp.clear()
                            else:
                                psg.popup_notify('Atnevezes nem tortent!', title='Atnevezes')
                        case 'Eltavolitas':
                            ...
                        case 'Konyvtar fa eltavolitasa...':
                            ...
                        case 'Megnyitas a masik asztalon':
                            window['-TABLE01-'].Update(create_twoD_list(os.path.join(t2_ut.szulo, kijelolt_sor[0])))
                            window['-Organize01-'].Update(os.path.join(t2_ut.szulo, kijelolt_sor[0]))
                            t1_ut:Jelen_EleresiUt = Jelen_EleresiUt(os.path.join(t2_ut.szulo, kijelolt_sor[0]))
                    if event_folder2 == 'Tulajdonsagok':
                        prop_win = folder_properties_window(os.path.join(t2_ut.szulo, kijelolt_sor[0]))
                        to_rename = ''
                        while True:
                            prop_event, prop_val = prop_win.read()
                            if prop_event == psg.WIN_CLOSED:
                                break
                            
                            if prop_event == '-RENAMER-':
                                to_rename = prop_win['-RENAMER-'].get()
                        prop_win.close()
                        
                        if (to_rename != f'{kijelolt_sor[0]}') and (to_rename != ''):
                            ev = psg.popup_yes_no('Szeretne atnevezni a mappat?')
                            match ev:
                                case 'Yes': 
                                    renaming(os.path.join(t2_ut.szulo, kijelolt_sor[0]), os.path.join(t2_ut.szulo, to_rename))
                                    psg.popup_notify('Atnevezes megtortent!')
                                    refresh_bool = True
                                    refresh_num = 2
                                    tmp:list = window['-TABLE02-'].get().copy()
                                    kijelolt_sor = [tmp [row] for row in values[event]].pop()
                                    tmp.clear()
                                    
                                case 'No':
                                    psg.popup_notify('Nem lett atnevezve!')
                else:
                    
                    # ha a kijelolt sorban levo elem fajl -> figyelje az eventeket 
                    # /// tovabba ha a kijelolt fajl '.txt', '.py', '.md', '.js', '.log' 
                    # kiterjesztesu, valtoztasson jobb klikk menut
                    # a jobb klikk menubol meg lehet nyitni majd a Writerben a fajlt 
                    
                    if kijelolt_sor[1] in ('.txt', '.py', '.md', '.js', '.log'):
                        window['-TABLE02-'].set_right_click_menu(file_right_click)
                    else:
                        window['-TABLE02-'].set_right_click_menu(other_right_click)
                        
                    window['-TABLE02-'].set_tooltip('Jobb klikkel a lehetosegpanel')
                    eventT2, valuesT2 = window.read()
                    if eventT2 == 'Control_L:17':
                        print(eventT2)
                        control_event, _ = window.read()
                        print(control_event)
                        match control_event:
                            case 'o':
                                try:
                                    fajl, bov = kijelolt_sor[0], kijelolt_sor[1]
                                    fajlnev = f'{fajl}{bov}'
                                    os.startfile(os.path.join(t2_ut.szulo, fajlnev), 'open')
                                    fajl, bov = '', ''
                                except OSError as e:
                                    psg.popup_notify( f'{bov} cannot be opened and exception {e}' ,title='No program to open')
                                    fajl, bov = '', ''
                            case 'x':
                                fajl, bov = kijelolt_sor[0], kijelolt_sor[1]
                                choice = psg.popup_get_text(f'El szeretne tavolitani a {fajl}{bov} elemet? Valaszlehetoseg: (yes/no)', title='Delete')
                                match choice:
                                    case None:
                                        psg.popup_notify('Cancelled!')
                                    case '':
                                        psg.popup_notify('No choice!')
                                    case 'yes':
                                        remove_folder_or_file(2, os.path.join(t2_ut.szulo, f'{fajl}{bov}'))
                                        psg.popup_notify('Deleted!')
                                    case 'no':
                                        psg.popup_notify('Cancelled!')
                                    case other:
                                        psg.popup_notify('Cancelled!')
                                fajl, bov = '', ''
                    if eventT2 in ('Athelyezes megadott mappaba...::-FILE-', 'Athelyezes::-FILE-', 'Atnevezes::-FILE-'):
                        match eventT2:
                            case 'Athelyezes::-FILE-':
                                ...
                            case 'Athelyezes megadott mappaba...::-FILE-':
                                ...
                            case 'Atnevezes::-FILE-':
                                real_path, head, tail = t2_ut.szulo, kijelolt_sor[0], kijelolt_sor[1]
                                val = psg.popup_get_text('A fajl atnevezese:', default_text=f'{head}{tail}', keep_on_top=True,)
                                print(f'{val}')
                                if val != f'{head}{tail}' and val != '' and val != None:
                                    ...
                                    message_out = renaming(os.path.join(real_path, f'{head}{tail}'), os.path.join(real_path, val))
                                    print(message_out)
                                    psg.popup_notify(message_out)
                                    refresh_bool = True
                                    refresh_num = 2
                                    tmp:list = window['-TABLE02-'].get().copy()
                                    kijelolt_sor = [tmp [row] for row in values[event]].pop()
                                    tmp.clear()
                                else:
                                    ...
                    if eventT2 in ('Megnyitas Writerben', 'Eleresi ut masolasa', 'Masolas', 'Megnyitas alapertelmezett alkalmazasban'):
                        match eventT2:
                            ############################################
                            case 'Megnyitas Writerben':
                                fajl, bov = kijelolt_sor[0], kijelolt_sor[1]
                                if os.path.exists(os.path.join(t2_ut.szulo, f'{fajl}{bov}')):
                                    fajl_text, encoded_var = open_file(os.path.join(t2_ut.szulo, f'{fajl}{bov}'))
                                    is_saved = True
                                    writer_window = make_second_window(fajl_text)
                                    while True:
                                        writerup = True
                                        eventw, valuew = writer_window.read(timeout=100)
                                        if eventw in  (psg.WIN_CLOSED, 'X') and is_saved == False:
                                            match valuew['-MULTI-']:
                                                case '':
                                                    break
                                                case other:
                                                    made = psg.popup_ok_cancel('Biztos benne hogy mentes nelkul szeretne bezarni?')
                                                    match made:
                                                        case 'OK':
                                                            break
                                                        case 'Cancel':
                                                            continue
                                        elif eventw in  (psg.WIN_CLOSED, 'X') and is_saved == True:
                                            break
                                        used_path = t2_ut.szulo
                                        used_file = writer_window['-WRITER-NAME-'].get()
                                        if eventw == 'Control_L:17':
                                            key_event, key_values = writer_window.read(100)
                                            if key_event == 'z' and is_saved == False:
                                                want_to_close:str = psg.popup_yes_no('Biztos benne hogy mentes nelkul szeretne bezarni?') 
                                                match want_to_close:
                                                    case 'Yes':
                                                        break
                                                    case 'No':
                                                        continue
                                            elif key_event == 'z' and is_saved == True:
                                                break
                                            if key_event == 's':
                                                if (used_file == 'untitled.txt') and (is_saved == False):
                                                    save_place = psg.popup_get_folder('Valassza ki a menteni kivant fajl helyet!')
                                                    save_name = psg.popup_get_text('Irja be a fajl nevet es bovitmenyet! (fajl.txt)')
                                                    f, b = os.path.splitext(save_name)
                                                    if save_place != '' and save_name != '' and f != '' and b != '':
                                                        match os.path.exists(os.path.join(save_place, save_name)):
                                                            case True:
                                                                psg.popup_cancel('Ilyen fajl mar letezik!')
                                                            case False:
                                                                out_message = create_file(save_place, save_name, writer_window['-ENCODED-VAL-'].get(), writer_window['-MULTI-'].get().expandtabs(4))
                                                                psg.popup_ok(out_message)
                                                                is_saved = True
                                                                writer_window['-WRITER-NAME-'].update(save_name)
                                                            case other:
                                                                ...
                                                    else:
                                                        psg.popup_ok('Nem megfelelo adatok lettek megadva!')
                                                        match save_place:
                                                            case '':
                                                                psg.popup_ok('Hianyzo utvonal!')
                                                                continue
                                                            case other:
                                                                match f:
                                                                    case '':
                                                                        psg.popup_ok('Hianyzo fajlnev!')
                                                                        used_path = save_place
                                                                        continue
                                                                    case other:
                                                                        match b:
                                                                            case '':
                                                                                psg.popup_ok('Hianyzo bovitmeny!')
                                                                                continue
                                                                            case other:
                                                                                is_saved = True
                                                                                continue
                                                elif (used_file != 'untitled.txt') and (is_saved == False):
                                                    out_message = overwriting_existing_file(used_path, writer_window['-WRITER-NAME-'].get(), writer_window['-ENCODED-VAL-'].get(), writer_window['-MULTI-'].get().expandtabs(4))
                                                    is_saved = True
                                                else:
                                                    continue
                                            if key_event == 'v':
                                                pyperclip.paste()
                                            if key_event == 'c':
                                                pyperclip.copy()
                                        
                                        writer_window['-WRITER-NAME-'].update(f'{fajl}{bov}')
                                        writer_window['-ENCODED-VAL-'].update(encoded_var)
                                        writer_window['-SELECT-SAVE-'].Update(['Mentes', ['!Mentes', 'Mentes mint', ['!.txt', '!.py', '!&.html', '!&.js', ]]])
                                        if eventw == '-ENABLE-MODIFY-':
                                            writer_window['-MULTI-'].update(disabled = False)
                                            writer_window['-ENABLE-MODIFY-'].update(visible = False)
                                            writer_window['-SELECT-SAVE-'].Update(['Mentes', ['Mentes', 'Mentes mint', ['!.txt', '!.py', '!&.html', '!&.js', ]]])
                                            
                                        if eventw in ('Mentes', '.txt', '.py', '.html', '.js','-MULTI-'):
                                            match eventw:
                                                case 'Mentes':
                                                    if os.path.exists(os.path.join(t2_ut.szulo,f'{fajl}{bov}')):
                                                        out_message = overwriting_existing_file(used_path, writer_window['-WRITER-NAME-'].get(), writer_window['-ENCODED-VAL-'].get(), writer_window['-MULTI-'].get().expandtabs(4))
                                                        psg.popup_ok(out_message)
                                                        is_saved = True
                                                case '.txt':
                                                    save_place = psg.popup_get_folder('Valassza ki a menteni kivant fajl helyet!')
                                                    save_name = psg.popup_get_text('Irja be a fajl nevet! (fajl.txt)')
                                                    if save_place != '' and save_name != '':
                                                        match os.path.exists(os.path.join(save_place, f'{save_name}.txt')):
                                                            case True:
                                                                psg.popup_cancel('Ilyen fajl mar letezik!')
                                                                continue
                                                            case False:
                                                                out_message = create_file(save_place, f'{save_name}.txt', writer_window['-ENCODED-VAL-'].get(), writer_window['-MULTI-'].get().expandtabs(4))
                                                                psg.popup_ok(out_message)
                                                                is_saved = True
                                                                writer_window['-WRITER-NAME-'].update(save_name)
                                                    else:
                                                        match save_place:
                                                            case '':
                                                                psg.popup_ok('Hianyzo utvonal!')
                                                            case other:
                                                                match save_name:
                                                                    case '':
                                                                        psg.popup_ok('Hianyzo fajlnev')
                                                                    case other:
                                                                        continue
                                                case '.py':
                                                    save_place = psg.popup_get_folder('Valassza ki a menteni kivant fajl helyet!')
                                                    save_name = psg.popup_get_text('Irja be a fajl nevet! (fajl.py)')
                                                    if save_place != '' and save_name != '':
                                                        match os.path.exists(os.path.join(save_place, f'{save_name}.py')):
                                                            case True:
                                                                psg.popup_cancel('Ilyen fajl mar letezik!')
                                                                continue
                                                            case False:
                                                                out_message = create_file(save_place, f'{save_name}.py', writer_window['-ENCODED-VAL-'].get(), writer_window['-MULTI-'].get().expandtabs(4))
                                                                psg.popup_ok(out_message)
                                                                is_saved = True
                                                                writer_window['-WRITER-NAME-'].update(save_name)
                                                    else:
                                                        match save_place:
                                                            case '':
                                                                psg.popup_ok('Hianyzo utvonal!')
                                                            case other:
                                                                match save_name:
                                                                    case '':
                                                                        psg.popup_ok('Hianyzo fajlnev')
                                                                    case other:
                                                                        continue
                                                case '.html':
                                                    save_place = psg.popup_get_folder('Valassza ki a menteni kivant fajl helyet!')
                                                    save_name = psg.popup_get_text('Irja be a fajl nevet! (fajl.html)')
                                                    if save_place != '' and save_name != '':
                                                        match os.path.exists(os.path.join(save_place, f'{save_name}.html')):
                                                            case True:
                                                                psg.popup_cancel('Ilyen fajl mar letezik!')
                                                                continue
                                                            case False:
                                                                out_message = create_file(save_place, f'{save_name}.html', writer_window['-ENCODED-VAL-'].get(), writer_window['-MULTI-'].get().expandtabs(4))
                                                                psg.popup_ok(out_message)
                                                                is_saved = True
                                                                writer_window['-WRITER-NAME-'].update(save_name)
                                                    else:
                                                        match save_place:
                                                            case '':
                                                                psg.popup_ok('Hianyzo utvonal!')
                                                            case other:
                                                                match save_name:
                                                                    case '':
                                                                        psg.popup_ok('Hianyzo fajlnev')
                                                                    case other:
                                                                        continue
                                                case '.js':
                                                    save_place = psg.popup_get_folder('Valassza ki a menteni kivant fajl helyet!')
                                                    save_name = psg.popup_get_text('Irja be a fajl nevet! (fajl.js)')
                                                    if save_place != '' and save_name != '':
                                                        match os.path.exists(os.path.join(save_place, f'{save_name}.js')):
                                                            case True:
                                                                psg.popup_cancel('Ilyen fajl mar letezik!')
                                                                continue
                                                            case False:
                                                                out_message = create_file(save_place, f'{save_name}.js', writer_window['-ENCODED-VAL-'].get(), writer_window['-MULTI-'].get().expandtabs(4))
                                                                psg.popup_ok(out_message)
                                                                is_saved = True
                                                                writer_window['-WRITER-NAME-'].update(save_name)
                                                    else:
                                                        match save_place:
                                                            case '':
                                                                psg.popup_ok('Hianyzo utvonal!')
                                                            case other:
                                                                match save_name:
                                                                    case '':
                                                                        psg.popup_ok('Hianyzo fajlnev')
                                                                    case other:
                                                                        continue
                                                case '-MULTI-':
                                                    is_saved = False
                                    
                                    writerup = False
                                    writer_window.close()
                                    fajl, bov = '', ''
                                    ###################################################3
                            case 'Eleresi ut masolasa':
                                fajl, bov = kijelolt_sor[0], kijelolt_sor[1]
                                if os.path.exists(os.path.join(t2_ut.szulo, f'{fajl}{bov}')):
                                    pyperclip.copy(f'{os.path.normcase(os.path.join(t2_ut.szulo, fajl))}{bov}')
                                    psg.popup_notify('Copied to clipboard', title='Copied')
                                    fajl, bov = '', ''
                            case 'Masolas':
                                ...
                            case 'Megnyitas alapertelmezett alkalmazasban':
                                try:
                                    fajl, bov = kijelolt_sor[0], kijelolt_sor[1]
                                    fajlnev = f'{fajl}{bov}'
                                    os.startfile(os.path.join(t2_ut.szulo, fajlnev), 'open')
                                    fajl, bov = '', ''
                                except OSError as e:
                                    psg.popup_notify( f'{bov} cannot be opened and exception {e}' ,title='No program to open')
                                    fajl, bov = '', ''   
                                    
                    if eventT2 == 'Tulajdonsagok':
                        to_rename = ''
                        prop_win = file_properties_win(os.path.join(t2_ut.szulo, f'{kijelolt_sor[0]}{kijelolt_sor[1]}'), kijelolt_sor[3], kijelolt_sor[2])
                        while True:
                            prop_event, prop_val = prop_win.read()
                            if prop_event == psg.WIN_CLOSED:
                                break
                            prop_win['-RENAMER-FILE-'].set_cursor()
                            if prop_event == '-RENAMER-FILE-':
                                to_rename = prop_win['-RENAMER-FILE-'].get()
                        prop_win.close()
                        if (to_rename != f'{kijelolt_sor[0]}') and (to_rename != ''):
                            ev = psg.popup_yes_no('Szeretne atnevezni a mappat?')
                            match ev:
                                case 'Yes': 
                                    message_out = renaming(os.path.join(t2_ut.szulo, f'{kijelolt_sor[0]}{kijelolt_sor[1]}'), os.path.join(t2_ut.szulo, f'{to_rename}{kijelolt_sor[1]}'))
                                    psg.popup_notify(message_out)
                                    refresh_bool = True
                                    refresh_num = 2
                                    tmp:list = window['-TABLE02-'].get().copy()
                                    kijelolt_sor = [tmp [row] for row in values[event]].pop()
                                    tmp.clear()
                                    
                                case 'No':
                                    psg.popup_notify('Nem lett atnevezve!')
                    to_rename = ''    
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
                
    if refresh_bool == True:
        match refresh_num:
            case 1: 
                vals = create_twoD_list(t1_ut.szulo)
                window['-TABLE01-'].Update(vals)
                refresh_bool = False
                refresh_num = 0
            case 2:
                vals = create_twoD_list(t2_ut.szulo)
                window['-TABLE02-'].Update(vals)
                refresh_bool = False
                refresh_num = 0
                
    match event:
        case '-Organize01-':
            if os.path.exists(window["-Organize01-"].get()) and (window["-Organize01-"].get()[-1] == '/') or (window["-Organize01-"].get()[-1] == '\''):
                choice = psg.popup_yes_no(f'Megnyissa a {window["-Organize01-"].get()} mappat?')
                if choice == 'Yes':
                    window['-TABLE01-'].Update(create_twoD_list(window['-Organize01-'].get()))
                    t1_ut:Jelen_EleresiUt = Jelen_EleresiUt(window['-Organize01-'].get())
                else:
                    continue
        case "-Organize02-":
            if os.path.exists(window["-Organize02-"].get()):
                choice = psg.popup_yes_no(f'Megnyissa a {window["-Organize02-"].get()} mappat?')
                if choice == 'Yes':
                    window['-TABLE02-'].Update(create_twoD_list(window['-Organize02-'].get()))
                    t2_ut:Jelen_EleresiUt = Jelen_EleresiUt(window['-Organize02-'].get())
                else:
                    continue
        case other:
            continue
                
    match event:
        case ('-TABLE01-', '+CLICKED+', (-1, 0)):
            window['-TABLE01-'].get().sort(key=lambda x: x[0])
            window['-TABLE01-'].update(values=window['-TABLE01-'].get())
        case ('-TABLE02-', '+CLICKED+', (-1, 0)):
            window['-TABLE02-'].get().sort(key=lambda x: x[0])
            window['-TABLE02-'].update(values=window['-TABLE01-'].get())
        case ('-TABLE01-', '+CLICKED+', (-1, 1)):
            window['-TABLE01-'].get().sort(key=lambda x: x[1])
            window['-TABLE01-'].update(values=window['-TABLE01-'].get())
        case ('-TABLE02-', '+CLICKED+', (-1, 1)):
            window['-TABLE02-'].get().sort(key=lambda x: x[1])
            window['-TABLE02-'].update(values=window['-TABLE01-'].get())
        case ('-TABLE01-', '+CLICKED+', (-1, 3)):
            window['-TABLE01-'].get().sort(key=lambda x: x[3])
            window['-TABLE01-'].update(values=window['-TABLE01-'].get())
        case ('-TABLE02-', '+CLICKED+', (-1, 3)):
            window['-TABLE02-'].get().sort(key=lambda x: x[3])
            window['-TABLE02-'].update(values=window['-TABLE01-'].get())
        
                
    # if event in ('Megnyitas', 'Eleresi ut masolasa', 'Masolas', 'Athelyezes::-FILE-', 'Atnevezes::-FILE-'):
    #     match event:
    #         case 'Megnyitas':
    #             ...
        
    # if event in ('Masolas', '&Utvonal masolasa...', 'Athelyezes::-FOLDER-', 'Athelyezes megadott mappaba...', 'Atnevezes::-FOLDER-', 'Eltavolitas', 'Konyvtar fa eltavolitasa...' ,'Megnyitas a masik asztalon'):
    #     ...
    
    # if event == 'Tulajdonsagok':
    #     ...
    if ((event == 'r') and (eventlist[0] == 17)) or event == 'Refresh':
        psg.popup_notify('Refreshed', title='Software')
        
    # if event == 'Refresh':
    #     psg.popup_notify('Refreshed', title='Software')   
    
window.close()
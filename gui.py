import os
import PySimpleGUI as psg
#from data.file_folder_managing import create_twoD_list
from data.disk_manager import kinyeres

fejlec:list = []*4
fejlec = ['Név', 'Bővítmény','Utolsó módosítás','Méret']




writer_menu:list
writer_menu = ['Fajl', ['Mentes', 'Mentes maskent', 'Megnyitas']], ['Szerkeszt', ['Masolas', 'Beillesztes']]
disk_right_click = []
disk_click = ['Disk', ['Megnyitas asztalon', ['Asztal1::-INT1-', 'Asztal2::-INT2-']]]
folder_right_click:list
folder_right_click = ['Folder', ['&Copy', '&Copy path...', 'Move', 'Move to...', 'Rename', 'Remove', 'Remove tree...', 'Open in new tab', 'Properties']]
#a meretek igy [0]appwinx, [1]appwiny, [2]tablex, [3]tabley, [4]secondWindowx, [5]secondWindowy, [6]multilinex, [7]multilineY, [8]searchWinX, [9]searchWinY, [10]searchListX, [11]searchListY , [12]Disk selectorX, [13] Disk selectorY
meretek:list = [1280,720,300,36,700,800,65,45, 400, 700, 50, 50, 400, 400]

vals:list = []
# vals = create_twoD_list(os.getcwd())



def create_layout():
    back_arrow = "C:/Users/csehg/pywork/bcpywork/back-arrow.png"
    psg.theme('SystemDefault')
    layout = [[psg.Button('Diszkek', key='-DISK_WIN-', enable_events=True) ,
               psg.Input(os.getcwd(), enable_events=True, key="-Organize01-", ), 
            #    psg.Button('Kereses ablak', enable_events=True, key='-SEARCH01-'),
               psg.Push(),
               psg.Input(os.getcwd(), enable_events=True, key="-Organize02-"), 
            #    psg.Button('Kereses ablak', enable_events=True, key='-SEARCH02-'),
               psg.Push()],
              [psg.Button('', button_color=(psg.theme_background_color(), psg.theme_background_color()), 
                          image_filename=back_arrow, size=(10,10), key='Back01',
                          image_subsample=2, border_width=0,
                          mouseover_colors=("#507197", "#697dae"), highlight_colors=("#507197", "#697dae")),
               psg.Push(),
               psg.Button('', button_color=(psg.theme_background_color(), psg.theme_background_color()), 
                          image_filename=back_arrow, size=(10,10), key='Back02',
                          image_subsample=2, border_width=0,
                          mouseover_colors=("#507197", "#697dae"), highlight_colors=("#507197", "#697dae")),
               psg.Push()
               ],
              [psg.Table(vals,
                         headings=fejlec, 
                         size=(meretek[2],meretek[3]), 
                         expand_x=True,
                         expand_y=True,
                         key='-TABLE01-', 
                         enable_events=True,
                         bind_return_key=True
                         ),
               psg.Button('Writer'),
               psg.Table(vals,headings=fejlec, size=(meretek[2],meretek[3]), 
                         key='-TABLE02-',
                         expand_x=True,
                         expand_y=True,
                         enable_events=True,
                         bind_return_key=True), 
               ]
              ]
    
    return layout

def create_ablak():
    window = psg.Window('Py File Manager', create_layout(), 
                        size=(meretek[0],meretek[1]), 
                        right_click_menu=[],
                        resizable=True, 
                        return_keyboard_events=True, 
                        location=(0,0),
                        disable_minimize=False
                        )
    return window

def create_disk_layout(diszk_nev:str, diszk_key:str,diszk_max:int):
    
    disk_elolayout = [
        [psg.Text(diszk_nev)],
        [psg.ProgressBar(max_value=diszk_max,right_click_menu=any, key=diszk_key)]
        ]
    
    return disk_elolayout

def create_disk_window(number:int, diszk_lista, diszk_info):
    psg.theme('SystemDefault')
    window4 = psg.Window('Diszkek valasztasa',
                         [
                             [psg.Frame('', [[psg.T('Csatlakozott diszkek', key='-TAROLOK-')]])]
                             ],
                         size=(meretek[12],meretek[13]),  
                         use_custom_titlebar=True,
                         return_keyboard_events=True,
                         keep_on_top=True
                         )
    
    for i in range(number):
        K:str = f'-DISK_WIN{i}-'
        V:str = f'-BM{i}-'
        tval:str = f'-TX{i}-'
        window4.extend_layout(window4['-TAROLOK-'], [[psg.T(f'{diszk_lista[i]}', key=tval), psg.Push(), psg.ButtonMenu('Műveletek', menu_def=disk_click, key=V)],
                                                     [psg.ProgressBar(max_value=diszk_info[i], key=K, size=(50,15))]])
        K:str = ''
        V:str = ''
        tval:str = ''
    
    return window4
        
        

# def create_search_layout():
#     psg.theme('SystemDefault')
#     disk_nev, _, _ = kinyeres()
#     a_keresendo = map(os.path.abspath, disk_nev)
#     search_layout = [[psg.Input('', key='-SEARCHING-', expand_x=True), psg.Combo(values=[x for x in a_keresendo], default_value=os.path.expanduser('~'), key='-DRIVE-', expand_x=True)],
#                      [psg.Listbox([], default_values=any, size=(meretek[10], meretek[11]), right_click_menu=[], key='-FOUND-', highlight_background_color="#7AA874", change_submits=False)]
#                      ]
#     return search_layout

# def create_search_window():
#     window3 = psg.Window('SearchBar', create_search_layout(), 
#                         size=(meretek[8],meretek[9]),  
#                         use_custom_titlebar=True,
#                         resizable=True, 
#                         alpha_channel=1, 
#                         return_keyboard_events=True,
#                         keep_on_top=True
#                         )
#     return window3



def create_writer():
    layout2 = [[psg.Text('Writer'),psg.Push(), psg.Text('X', enable_events=True)],
               [psg.Menu(menu_definition=writer_menu, visible=True)],
               [psg.Multiline('', key='-MULTI-', size=(meretek[6],meretek[7])), psg.Text('Kodolas:'), 
               psg.Combo(values=['utf-8', 'utf-16', 'ansi'], default_value='utf-8')]
               ]
    return layout2

def make_second_window():
    window02 = psg.Window('Writer', 
                          create_writer(), 
                          size=(meretek[4],meretek[5]),
                          no_titlebar=True,
                          return_keyboard_events=True
                          )
    return window02

def file_properties_lay(utv:str, meret: int) -> list:
    szulo, fajl = os.path.split(utv)
    nev, bov = os.path.splitext(fajl)
    layout = [[psg.Input(nev, enable_events=True)],
              [psg.Text('Bovitmeny:'), psg.Text(bov)],
              [psg.Text('Hely:'), psg.Text(szulo)],
              [psg.HorizontalSeparator()],
              [psg.Text('Meret:'), psg.Text(round(meret/1024, 2))],
              ]
    
    return layout

def file_properties_win(utv:str, meret:int):
    prop_window = psg.Window('Tulajdonsagok', 
                             file_properties_lay(utv, meret), 
                             disable_minimize=True, 
                             use_custom_titlebar=True)
    return prop_window

def folder_properties_layout(utv:str):
    szulo, mappa = os.path.split(utv)
    layout = [[psg.Input(mappa, enable_events=True)],
              [psg.Text('Hely:'), psg.Text(szulo)]
              ]
    
    return layout

def folder_properties_window(utv:str):
    prop_window = psg.Window('Tulajdonsagok', 
                             file_properties_lay(utv), 
                             disable_minimize=True, 
                             use_custom_titlebar=True)
    return prop_window
    
if __name__ == '__main__':
    window = file_properties_win('C:/Users/csehg/pytry/2d_one_file.py', 23510)
    
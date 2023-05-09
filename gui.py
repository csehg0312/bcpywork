import os
import PySimpleGUI as psg
#from data.file_folder_managing import create_twoD_list
from data.disk_manager import kinyeres
from time import strftime, gmtime
import pathlib

fejlec:list = []*4
fejlec = ['Név', 'Bővítmény','Utolsó módosítás','Méret bájtokban']

writer_menu:list
writer_menu = ['Fajl', ['Mentes', 'Mentes maskent', 'Megnyitas']], ['Szerkeszt', ['Masolas', 'Beillesztes']]
disk_right_click = []
disk_click = ['Disk', ['Asztal1::-INT1-', 'Asztal2::-INT2-']]
folder_right_click:list
folder_right_click = ['Folder', ['&Copy', '&Copy path...', 'Move', 'Move to...', 'Rename', 'Remove', 'Remove tree...', 'Open in new tab', 'Properties']]
#a meretek igy [0]appwinx, [1]appwiny, [2]tablex, [3]tabley, [4]secondWindowx, [5]secondWindowy, [6]multilinex, [7]multilineY, [8]searchWinX, [9]searchWinY, [10]searchListX, [11]searchListY , [12]Disk selectorX, [13] Disk selectorY
meretek:list = [1280,720,300,36,1000,800,85,45, 400, 700, 50, 50, 400, 600]

vals:list = []

def calcdate(linux_time):
    CTV = strftime('%d %b %Y %H:%M', gmtime(linux_time))
    return f'{CTV}'


def create_layout():
    icon_path = pathlib.Path(__file__).parent.resolve()
    back_arrow = f"{icon_path}/icon/back-arrow-mod.png"
    copy_it = f"{icon_path}/icon/copy_it-mod.png"
    delete_it = f"{icon_path}/icon/delete_it.png"
    edit_it = f"{icon_path}/icon/edit_it-mod.png"
    psg.theme('SystemDefault')
    frame_first_table:list = [[psg.Input('', key="-Organize01-", readonly=True, expand_x=True), 
            #    psg.Button('Kereses ablak', enable_events=True, key='-SEARCH01-'),
               psg.Push()],
                           [psg.Button('', button_color=(psg.theme_background_color(), psg.theme_background_color()), 
                          image_filename=back_arrow, size=(10,10), key='Back01',
                          image_subsample=2, border_width=0,
                          mouseover_colors=("#507197", "#697dae"), highlight_colors=("#507197", "#697dae")),
               psg.Push(),
               psg.Text('Asztal1'),
               psg.Push()],
                              [psg.Table(vals,
                         headings=fejlec, 
                         size=(meretek[2],meretek[3]), 
                         expand_x=True,
                         expand_y=True,
                         key='-TABLE01-', 
                         enable_events=True,
                         bind_return_key=True,
                         enable_click_events=True
                         )]
                              ]
    frame_second_table:list = [[psg.Input('', key="-Organize02-", readonly=True,expand_x=True), 
            #    psg.Button('Kereses ablak', enable_events=True, key='-SEARCH02-'),
               psg.Push()],
                               [psg.Button('', button_color=(psg.theme_background_color(), psg.theme_background_color()), 
                          image_filename=back_arrow, size=(10,10), key='Back02',
                          image_subsample=2, border_width=0,
                          mouseover_colors=("#507197", "#697dae"), highlight_colors=("#507197", "#697dae")),
               psg.Push(),
               psg.Text('Asztal2'),
               psg.Push()],
                           [psg.Table(vals,headings=fejlec, size=(meretek[2],meretek[3]), 
                         key='-TABLE02-',
                         expand_x=True,
                         expand_y=True,
                         enable_events=True,
                         bind_return_key=True,
                         enable_click_events=True)
               ]    
                               ]
    frame_layout = [[psg.Button('Diszkek', key='-DISK_WIN-', enable_events=True)],
                    [psg.Button('Writer')],
                    [psg.Button('Refresh')],
                    [psg.Button('', button_color=(psg.theme_background_color(), psg.theme_background_color()), 
                          image_filename=copy_it, size=(10,10), key='Copy_OUT',
                          image_subsample=2, border_width=0,
                          mouseover_colors=("#507197", "#697dae"), highlight_colors=("#507197", "#697dae")),
                     psg.Button('', button_color=(psg.theme_background_color(), psg.theme_background_color()), 
                          image_filename=delete_it, size=(10,10), key='Delete_OUT',
                          image_subsample=2, border_width=0,
                          mouseover_colors=("#507197", "#697dae"), highlight_colors=("#507197", "#697dae")),
                     psg.Button('', button_color=(psg.theme_background_color(), psg.theme_background_color()), 
                          image_filename=edit_it, size=(10,10), key='Edit_OUT',
                          image_subsample=2, border_width=0,
                          mouseover_colors=("#507197", "#697dae"), highlight_colors=("#507197", "#697dae"))]]
    # layout_old = [[psg.Input('', enable_events=True, key="-Organize01-", ), 
    #         #    psg.Button('Kereses ablak', enable_events=True, key='-SEARCH01-'),
    #            psg.Push(),
    #            psg.Input('', enable_events=True, key="-Organize02-"), 
    #         #    psg.Button('Kereses ablak', enable_events=True, key='-SEARCH02-'),
    #            psg.Push()],
    #           [psg.Button('', button_color=(psg.theme_background_color(), psg.theme_background_color()), 
    #                       image_filename=back_arrow, size=(10,10), key='Back01',
    #                       image_subsample=2, border_width=0,
    #                       mouseover_colors=("#507197", "#697dae"), highlight_colors=("#507197", "#697dae")),
    #            psg.Push(),
    #            psg.Text('Asztal1'),
    #            psg.Push(),
    #            psg.Button('', button_color=(psg.theme_background_color(), psg.theme_background_color()), 
    #                       image_filename=back_arrow, size=(10,10), key='Back02',
    #                       image_subsample=2, border_width=0,
    #                       mouseover_colors=("#507197", "#697dae"), highlight_colors=("#507197", "#697dae")),
    #            psg.Push(),
    #            psg.Text('Asztal2'),
    #            psg.Push()],
    #           [psg.Table(vals,
    #                      headings=fejlec, 
    #                      size=(meretek[2],meretek[3]), 
    #                      expand_x=True,
    #                      expand_y=True,
    #                      key='-TABLE01-', 
    #                      enable_events=True,
    #                      bind_return_key=True,
    #                      enable_click_events=True
    #                      ),
    #            psg.Frame('', frame_layout, element_justification='center'),
    #            psg.Table(vals,headings=fejlec, size=(meretek[2],meretek[3]), 
    #                      key='-TABLE02-',
    #                      expand_x=True,
    #                      expand_y=True,
    #                      enable_events=True,
    #                      bind_return_key=True,
    #                      enable_click_events=True), 
    #            ]
    #           ]
    layout = [[psg.Frame('', frame_first_table, expand_x=True, expand_y=True), psg.Frame('', frame_layout, element_justification='center'), psg.Frame('', frame_second_table, expand_x=True, expand_y=True)],
              [psg.Text('Copyright 2023'), psg.Text('Cseh Gábor')]]
    
    return layout

def create_ablak():
    iconUse = "C:/Users/csehg/pywork/bcpywork/icon/icov1.png" 
    window = psg.Window('Py File Manager', create_layout(), 
                        size=(meretek[0],meretek[1]), 
                        right_click_menu=[],
                        resizable=True, 
                        return_keyboard_events=True, 
                        location=(0,0),
                        disable_minimize=False,
                        icon=iconUse)
    return window

# def create_disk_layout(diszk_nev:str, diszk_key:str,diszk_max:int):
    
#     disk_elolayout = [
#         [psg.Text(diszk_nev)],
#         [psg.ProgressBar(max_value=diszk_max,right_click_menu=any, key=diszk_key)],
#         [psg.Text()]
#         ]
    
#     return disk_elolayout

def create_disk_window(number:int, diszk_lista, diszk_info):
    psg.theme('SystemDefault')
    window4 = psg.Window('Diszkek valasztasa',
                         [
                             [psg.Frame('', [[psg.T('Csatlakozott diszkek', key='-TAROLOK-')]])],
                             [psg.Text('Maximálisan 5 csatlakoztatott diszket támogatat!')]
                             ],
                         size=(meretek[12],meretek[13]),  
                         use_custom_titlebar=True,
                         return_keyboard_events=True,
                         keep_on_top=True
                         )
    
    for i in range(number):
        K:str = f'-DISK_WIN{i}-'
        V:str = f'-BM{i}-'
        F:str = f'-SZABAD{i}-'
        tval:str = f'-TX{i}-'
        window4.extend_layout(window4['-TAROLOK-'], [[psg.T(f'{diszk_lista[i]}', key=tval), psg.Push(), psg.ButtonMenu('Megnyitás', menu_def=disk_click, key=V)],
                                                     [psg.ProgressBar(max_value=diszk_info[i], key=K, size=(50,15))],
                                                     [psg.T('', key=F)]])
        K:str = ''
        V:str = ''
        F:str = ''
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
# kommand_data = ['programs','favorites', 'start', 'appdata', 'documents', 'recent']

# def to_show_data():
#     ...

# def kommand_layout():
#     simple_layout = [[psg.Text('A kommand szovege johet ide')],
#                      [psg.Input('', expand_x=True, tooltip=f'{kommand_data}')]
#                      ]
    
#     return simple_layout

# def kommand_window():
#     ...
    
def create_writer(multi_input:str = ''):
    frame_layout = [[psg.Text('untitled.txt', key='-WRITER-NAME-')],
                    [psg.Text('Kodolas:'), 
                     psg.Combo(values=['utf-8', 'utf-16', 'ansi'], default_value='utf-8', key='-ENCODED-VAL-')],
                    [psg.ButtonMenu('Mentes', menu_def=['Mentes', ['Mentes', 'Mentes maskeppen']], key='-SELECT-SAVE-')]
                    ]
    layout2 = [[psg.Text('Writer'),psg.Push(), psg.Text('X', enable_events=True)],
               [psg.Menu(menu_definition=writer_menu, visible=True)],
               [psg.Push(), psg.Button('Modositas engedelyezese', key='-ENABLE-MODIFY-', visible=True), psg.Push()],
               [psg.Multiline(multi_input, key='-MULTI-', size=(meretek[6],meretek[7]), disabled=True, enable_events=True, expand_x=True),
               psg.Frame(title='', border_width=0, layout=frame_layout)]
               ]
    return layout2


def make_second_window(multi_input:str = ''):
    window02 = psg.Window('Writer', 
                          create_writer(multi_input), 
                          size=(meretek[4],meretek[5]),
                          return_keyboard_events=True, 
                          grab_anywhere_using_control=True
                          )
    return window02

def file_properties_lay(utv:str, meret: int, modositas) -> list:
    szulo, fajl = os.path.split(utv)
    nev, bov = os.path.splitext(fajl)
    mod_date = calcdate(os.path.getctime(utv))
    layout = [[psg.Input(nev, enable_events=True, key='-RENAMER-FILE-')],
              [psg.Text('Bovitmeny:'), psg.Text(bov)],
              [psg.Text('Hely:'), psg.Text(szulo)],
              [psg.HorizontalSeparator()],
              [psg.Text('Meret:'), psg.Text(f'{round(meret/1024, 2)} kB')],
              [psg.Text('Modositas datuma:'), psg.Text(modositas)],
              [psg.Text('Letrehozas datuma: '), psg.Text(mod_date)]
              ]
    
    return layout

def file_properties_win(utv:str, meret:int,  modositas):
    prop_window = psg.Window('Tulajdonsagok', 
                             file_properties_lay(utv, meret, modositas), 
                             disable_minimize=True, 
                             use_custom_titlebar=True, 
                             keep_on_top=True)
    return prop_window

def folder_properties_layout(utv:str):
    szulo, mappa = os.path.split(utv)
    layout = [[psg.Input(mappa, enable_events=True, key='-RENAMER-')],
              [psg.Text('Hely:'), psg.Text(szulo)]
              ]
    
    return layout

def folder_properties_window(utv:str):
    prop_window = psg.Window('Tulajdonsagok', 
                             folder_properties_layout(utv), 
                             disable_minimize=True, 
                             use_custom_titlebar=True,
                             keep_on_top=True)
    return prop_window


def file_or_folder_szita(utv:str, meret:int = 0):
    if os.path.exists(utv):
        match os.path.isdir(utv):
            case False:
                PropWindow = file_properties_win(utv, meret)
                return PropWindow
            case True:
                PropWindow = folder_properties_window(utv)
                return PropWindow
            case other:
                psg.popup_ok('No properties found')
    
if __name__ == '__main__':
   ...
    
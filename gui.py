import os
import PySimpleGUI as psg

fejlec:list = []*4
fejlec = ['Név', 'Bővítmény','Utolsó módosítás','Méret']




egyszeru_jobb_kattintas:list
egyszeru_jobb_kattintas = ['Egyszeru',['&Writer', '&Uj', '&A mappa tulajdonsagai::Properties']]
file_rightl_click:list
file_rightl_click = []
folder_right_click:list
folder_right_click = ['Folder', ['&Copy', '&Copy path...', 'Move', 'Move to...', 'Rename', 'Remove', 'Remove tree...', 'Open in new tab', 'Properties']]
#a meretek igy [0]appwinx, [1]appwiny, [2]tablex, [3]tabley, [4]secondWindowx, [5]secondWindowy, [6]multilinex, [7]multilineY, [8]searchWinX, [9]searchWinY, [10]searchListX, [11]searchListY , [12]Disk selectorX, [13] Disk selectorY
meretek:list = [1280,720,35,36,600,500,45,25, 400, 700, 50, 50, 300, 300]

vals:list = []



def create_layout():
    prelayout = [[psg.ProgressBar(250)]]
    psg.theme('SystemDefault')
    layout = [[psg.Button('Diszkek', key='-DISK_WIN-', enable_events=True) ,psg.Input(os.getcwd(), enable_events=True, key="-Organize-"), psg.Button('Kereses ablak', enable_events=True, key='-SEARCH-')],
              [psg.Table(vals,headings=fejlec, size=(meretek[2],meretek[3]), key='-TABLE01-'),
               psg.Combo(default_value='Minden elem', values=('Minden elem','Csak mappak', 'Csak fajlok'), key='-COMBO-'),
               psg.Table(vals,headings=fejlec, size=(meretek[2],meretek[3]), key='-TABLE02-'), 
               psg.Button('Writer')]
              ]
    
    return layout

def create_ablak():
    window = psg.Window('Py File Manager', create_layout(), 
                        size=(meretek[0],meretek[1]), 
                        right_click_menu_tearoff=True,
                        resizable=True
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
                         use_custom_titlebar=True
                         )
    
    for i in range(number):
        K:str = f'-DISK_WIN{i}-'
        print(K)
        window4.extend_layout(window4['-TAROLOK-'], [[psg.T(diszk_lista[i])],
                                                     [psg.ProgressBar(max_value=diszk_info[i], key=K, size=(50,15), right_click_menu=folder_right_click)]])
        K:str = ''
    
    return window4
        
        

def create_search_layout():
    psg.theme('SystemDefault')
    search_layout = [[psg.Input('', key='-SEARCHING-', expand_x=True)],
                     [psg.Listbox([], default_values=any, size=(meretek[10], meretek[11]), enable_events=True, right_click_menu=[], key='-FOUND-')]
                     ]
    return search_layout

def create_search_window():
    window3 = psg.Window('SearchBar', create_search_layout(), 
                        size=(meretek[8],meretek[9]),  
                        use_custom_titlebar=True,
                        resizable=True, 
                        alpha_channel=0.8
                        )
    return window3



def create_writer():
    layout2 = [[psg.Text('Writer'),psg.Push(), psg.Text('X', enable_events=True)],
              [psg.Multiline('', key='-MULTI-', size=(meretek[6],meretek[7]))],
              [psg.Ok(), psg.Button('Exit')]
               ]
    return layout2

def make_second_window():
    window02 = psg.Window('Writer', 
                          create_writer(), 
                          size=(meretek[4],meretek[5]),
                          no_titlebar=True
                          )
    return window02

    
if __name__ == '__main__':
    create_ablak()
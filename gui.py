import os
import PySimpleGUI as psg

fejlec:list = []*4
fejlec = ['Név', 'Bővítmény','Utolsó módosítás','Méret']




egyszeru_jobb_kattintas:list
egyszeru_jobb_kattintas = ['Egyszeru',['&Writer', '&Uj', '&A mappa tulajdonsagai::Properties']]
file_rightl_click:list
file_rightl_click = []
folder_right_click:list
folder_right_click = ['Folder', ['&Cut', '&Copy', '&Copy path...', 'Move', 'Move to...', 'Rename', 'Remove', 'Remove tree...', 'Open in new tab', 'Properties']]
#a meretek igy appwinx, appwiny, tablex, tabley, secondWindowx, secondWindowy, multilinex, multilineY
meretek:list = [1280,720,35,36,600,500,45,25]

vals:list = []



def create_layout():
    prelayout = [[psg.ProgressBar()]]
    psg.theme('SystemDefault')
    layout = [[psg.Input(os.getcwd(), enable_events=True, key="-Organize-")],
              [psg.Table(vals,headings=fejlec, size=(meretek[2],meretek[3]), key='-T01-'),
               psg.Combo(default_value='Minden elem', values=('Minden elem','Csak mappak', 'Csak fajlok'), key='-COMBO-'),
               psg.Table(vals,headings=fejlec, size=(meretek[2],meretek[3]), key='-T02-'), 
               psg.Button('Writer')],
              []
              ]
    
    return layout

def create_ablak():
    window = psg.Window('Window', create_layout(), 
                        size=(meretek[0],meretek[1]), 
                        icon="icons/icov1.ico", 
                        disable_minimize=False, 
                        use_custom_titlebar=True,
                        right_click_menu_tearoff=True,
                        resizable=True
                        )
    return window



def create_writer():
    layout2 = [[psg.Text('Writer'),psg.Push(), psg.Text('X', enable_events=True)],
              [psg.Multiline('', key='-MULTI-', size=(meretek[6],meretek[7]))],
              [psg.Ok(), psg.Button('Exit')]
               ]
    return layout2

def make_second_window():
    num = randrange(1,100)
    window02 = psg.Window('Writer', create_writer(), size=(meretek[4],meretek[5]), icon="icons/refresh.ico")
    return window02

    
if __name__ == '__main__':
    create_ablak()
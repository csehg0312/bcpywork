import PySimpleGUI as psg
from random import randrange

fejlec:list = []*4
fejlec = ['Név', 'Bővítmény','Utolsó módosítás','Méret']




egyszeru_jobb_kattintas:list
egyszeru_jobb_kattintas = ['Egyszeru',['&Writer', '&Uj', '&A mappa tulajdonsagai::Properties']]
file_rightl_click:list
file_rightl_click = []
folder_right_click:list
folder_right_click = ['Folder', ['&Cut', '&Copy', '&Copy path...', 'Move', 'Move to...', 'Rename', 'Remove', 'Remove tree...', 'Open in new tab', 'Properties']]


win_x:int
win_y:int
ts_x:int
ts_y:int
secx:int
secy:int
win_x = 1280
win_y = 720
ts_x = 35
ts_y = 25
secx = 600
secy = 500



def create_layout():
    psg.theme('SystemDefault')
    layout = [[psg.Combo(default_value='Minden elem', values=('Minden elem','Csak mappak', 'Csak fajlok'), key='-COMBO-') ,psg.Text('Hey its me', enable_events=True, key='text', right_click_menu=egyszeru_jobb_kattintas)],
              [psg.Table([['' for row in range(15)] for col in range(4)], size=(ts_x,ts_y)), psg.Table([['' for row in range(15)] for col in range(4)], size=(ts_x,ts_y))],
              [psg.Button('Writer')],
              [psg.Button('OK'), psg.Button('Cancel')]
              ]
    
    return layout

def create_ablak():
    window = psg.Window('Window', create_layout(), size=(win_x,win_y), icon="icons/icov1.ico")
    return window



def create_writer():
    layout2 = [[psg.Text('Writer'),psg.Push(), psg.Text('X', enable_events=True)],
              [psg.Multiline('', key='-MULTI-', size=(45,25))],
              [psg.Ok(), psg.Button('Exit')]
               ]
    return layout2

def make_second_window():
    num = randrange(1,100)
    window02 = psg.Window('Writer', create_writer(), size=(secx,secy), icon="icons/refresh.ico")
    return window02

    
if __name__ == '__main__':
    create_ablak()
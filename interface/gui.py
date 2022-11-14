import PySimpleGUI as psg

win_x = 700
win_y = 500
lst_x = 35
lst_y = 25

r_clicked = ['&Right', ['Right', '!&Click', '---', '&Menu::_EASY_KEY_', 'E&xit', 'Properties']]
menu_def = [['&File', ['&Open', '&Save', '---', 'Properties', 'C&lose']],
            ['&Edit', ['Paste', ['Special', 'Normal', '!Cheesy'], 'Undo'], ], 
            ['&Help', '&About...'], ]
menu_bar = [r_clicked, menu_def]

def create_layout():
    psg.theme('SystemDefault')
    layout = [[psg.Text('Hey its me', enable_events=True, key='text', right_click_menu=menu_def)],
              [psg.Listbox([], size=(lst_x,lst_y) ), psg.Listbox([], size=(lst_x, lst_y))],
              [psg.Button('OK'), psg.Button('Cancel')]
              ]
    
    return layout

def create_ablak():
    window = psg.Window('Window', create_layout(), size=(win_x,win_y))
    return window
    
if __name__ == '__main__':
    create_ablak()
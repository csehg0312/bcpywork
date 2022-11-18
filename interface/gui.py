import PySimpleGUI as psg




win_x = 1280
win_y = 720
ts_x = 35
ts_y = 25

r_clicked = ['&Right', ['Right', '!&Click', '---', '&Menu::_EASY_KEY_', 'E&xit', 'Properties']]
menu_def = [['&File', ['&Open', '&Save', '---', 'Properties', 'C&lose']],
            ['&Edit', ['Paste', ['Special', 'Normal', '!Cheesy'], 'Undo'], ], 
            ['&Help', '&About...'], ]
menu_bar = [r_clicked, menu_def]

def create_layout():
    psg.theme('SystemDefault')
    postlayout = [[psg.StatusBar('Disk', key='-ST01-', size=(15,1), enable_events=True, visible=False), psg.ProgressBar(max_value=250, key='-PRST01-', visible=False)],
                  [psg.StatusBar('Disk', key='-ST02-', size=(15,1), enable_events=True, visible=False), psg.ProgressBar(max_value=250, key='-PRST02-', visible=False)],
                  [psg.StatusBar('Disk', key='-ST03-', size=(15,1), enable_events=True, visible=True), psg.ProgressBar(max_value=250, key='-PRST03-', visible=True)]]
    layout = [[psg.Text('Hey its me', enable_events=True, key='text', right_click_menu=menu_def)],
              [psg.Frame('No', postlayout), psg.Table([['' for row in range(15)] for col in range(4)], size=(ts_x,ts_y)), psg.Table([['' for row in range(15)] for col in range(4)], size=(ts_x,ts_y))],
              [psg.Button('OK'), psg.Button('Cancel')]
              ]
    
    return layout

def create_ablak():
    window = psg.Window('Window', create_layout(), size=(win_x,win_y))
    return window
    
if __name__ == '__main__':
    create_ablak()
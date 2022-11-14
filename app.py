from interface.gui import *
from data.path_manager import *
import PySimpleGUI as psg

window = create_ablak()

while True:
    event, values = window.read()
    print(event)
    if event == psg.WIN_CLOSED:
        break

window.close()
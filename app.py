import interface.gui as gui
import data.disk_manager as ddm
import PySimpleGUI as psg
import PySimpleGUIQt as psqt
import os

window = gui.create_ablak()
plusser = 0

while True:
    event, values = window.read()
    print(event)
    #psg.SystemTray.notify('New drive is introduced', str(ddm.drives))
    
    if event == psg.WIN_CLOSED:
        #psg.SystemTray.notify('The program is closing','See' )
        break

window.close()
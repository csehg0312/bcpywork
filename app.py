import interface.gui as gui
import interface.notifications as noti
import data.disk_manager as ddm
import PySimpleGUI as psg
import PySimpleGUIQt as psqt
import os



window = gui.create_ablak()

while True:
    event, values = window.read(timeout = 100)
    if event == psg.WIN_CLOSED:
        break
    #psg.SystemTray.notify('New drive is introduced', str(ddm.drives))

window.close()
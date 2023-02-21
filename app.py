import interface.gui as gui
import interface.notifications as noti
import data.disk_manager as ddm
import PySimpleGUI as psg
#import PySimpleGUIQt as psqt
import os



window = gui.create_ablak()

while True:
    event, values = window.read(timeout = 100)
    if event == psg.WIN_CLOSED:
        break
    conn = False
    val:list 
    val = [ddm.drive_inserted()]
    
    if val[0] == 2 and conn == False:
        #print('connection made')
        psg.SystemTray.notify('New drive is introduced', str(ddm.drive_inserted()))
        val.pop()
    if val[0] == 1 and conn == True:
        #print('connection lost')
        conn = False
        val.pop()
    else:
        #print('timeout')
        val.pop()
    #psg.SystemTray.notify('New drive is introduced', str(ddm.drives))
prelayout = [[]]
window.extend_layout(window, psg.Frame('', layout))
window.close()
import os
import interface.controller as c
import interface.gui as gui
import data.disk_manager as ddm
import PySimpleGUI as psg
import keyboard
import logging
#import PySimpleGUIQt as psqt
writerup:bool = False



window = gui.create_ablak()

while True:
    event, values = window.read(timeout = 5000)
    if event == psg.WIN_CLOSED:
        break
    com = values['-COMBO-']
    
    if event == 'Writer' and writerup == False:
        writerup = True
        window2 = gui.make_second_window()
        while True:
            event2,values2 = window2.read(timeout=100)
            
            if event2 in ('X', psg.WIN_CLOSED):
                #logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
                #logging.warning(f'The Writer has been closed, Event: {event2}')
                break
        window2.close()
        
        
    com = values['-COMBO-']
    #print(f'{event} and Combo val: {com}')
window.close()
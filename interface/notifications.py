import PySimpleGUI as psg

def new_connection():
    psg.SystemTray.notify("New drive has been introduced", "its here")
    
def lost_connection():
    psg.SystemTray.notify("Drive has been removed", "its here")
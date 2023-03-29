import os
from collections import deque
from data.dataclass_file_manager import File
from data.dataclass_folder_manager import Folder

def simple_data(ut:str):
    try:
        filebase:dict
        filebase = {'Path':str, 'Parent':str, "Folders":deque([]), "Files":deque([])}

        filebase.update({'Path':ut})
        parent:str
        parent, _ = os.path.split(ut)
        filebase.update({'Parent':parent})
        #print(filebase.values())
        filebase.update({"Folders": deque([x for x in os.listdir(ut) if os.path.isdir(os.path.join(ut,x))])})
        filebase.update({"Files": deque([x for x in os.listdir(ut) if os.path.isdir(os.path.join(ut,x)) == False and os.path.ismount(os.path.join(ut,x)) == False])})
        #filebase.update({"FilePath": deque([os.path.join(ut,x) for x in filebase.get('Files')])})
        #print(filebase.values())
        return filebase
    except (OSError, PermissionError):
        return {}
    
def kereses(ut:str):
    bazis:dict = {}
    keresessor:deque = deque([])
    bazis = simple_data(ut)
    keresessor = bazis.get('Folders')
    keresessor.extend(bazis.get('Files'))
    return list(keresessor)
    

def mappa_osztaly(ut:str):
    bazis:dict
    bazis = {}
    mappa:deque
    mappa = deque([])
    bazis=simple_data(ut)
    mappa = bazis.get('Folders')
    sor:deque
    sor = deque([Folder(ut,x) for x in mappa])
    bazis.clear()
    return sor


def fajl_osztaly(ut:str):
    base:dict
    base = {}
    fajls:deque
    fajls = deque([])
    base = simple_data(ut)
    fajls = base.get('Files')
    sor:deque
    sor = deque([File(ut, x) for x in fajls])
    base.clear()
    return sor

def get_data_from_file(obj:File):
    ob: File = obj
    return [ob.nev.default_factory, ob.bovitmeny.default_factory, ob.modositdate.default_factory, ob.meret.default_factory]

def get_data_folder(obj:Folder):
    ob: Folder = obj
    return[ob.mappa, ob.megnevez.default_factory, ob.modisitasdate.default_factory, 0]


def create_twoD_list(ut:str):
    hossz:int = len(os.listdir(ut))
    
    mappaobj:deque = deque([])
    mappaobj = mappa_osztaly(ut)
    mappaMap = map(get_data_folder, mappaobj)
    
    

    fajlobj:deque = deque([])
    fajlobj = fajl_osztaly(ut)
    fajlMap = map(get_data_from_file, fajlobj)
    
    mappaMap = list(mappaMap)
    fajlMap = list(fajlMap)
    # print(type(mappaMap))
    # print(type(fajlMap))
    
    mappasor = deque([x for x in mappaMap])
    fajlsor = deque([x for x in fajlMap])
    tomb:list = []*hossz
    for m in mappasor:
        tomb.append(m)
        
    for f in fajlsor:
        tomb.append(f)
    
    return tomb

    
if __name__ == '__main__':
    keres:list = []
    keres = kereses(os.getcwd())
    print(keres)
#     S = mappa_osztaly(utv)
#     print(S)
#     print(sys.getsizeof(S))




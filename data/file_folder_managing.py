import os
from collections import deque
from data.dataclass_file_manager import File
from data.dataclass_folder_manager import Folder
import magic

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


def open_the_encoding(current_place) -> str:
    with open(current_place, 'rb') as reader:
        not_encoded = reader.read()
        m = magic.Magic(mime_encoding=True)
        encoded = m.from_buffer(not_encoded)
        # print(encoded)
    return encoded

def open_file(current_path):
    encoder = open_the_encoding(current_path)
    if encoder != 'binary':
        with open(current_path, 'r', encoding=encoder ) as reader:
            file_text = reader.read()
            # print(file_text)
            reader.close()
            return file_text, encoder
    else:
        with open(current_path, 'rb') as reader:
            binary_text = reader.read()
            reader.close()
            return binary_text
    
# def is_same_file_extension(val:str) -> bool:
#     head,tail = os.path.splitext(val)
#     if 
    

def remove_file(current_path) -> str:
    try:
        os.remove(current_path)
        return 'File removed!'
    except OSError as e:
        return f'Exception happened {e}'

def remove_folder(current_path):
    try:
        os.rmdir(current_path)
        return 'Folder removed!'
    except OSError as e:
        return 'Exception happened {e}'
    
def remove_tree(current_path):
    ...
    
def remove_folder_or_file(file_or_folder:int, current_path) -> str:
    match file_or_folder:
        case 0:
            message = remove_folder(current_path)
            return message
        case 2:
            message = remove_file(current_path)
            return message
        case other:
            return 'No path added'
        

def creating_file_without_value(current_folder, file_to_create, encoded:str) -> str:
    file_created = os.path.join(current_folder, file_to_create)
    encodes = ['utf-8', 'utf-16', 'ansi']
    if encoded in encodes:
        # print('its all good')
        with open(file_created, 'w', encoding=encoded) as f_write:
            pass
        return 'A fajl elmentve tartalom nelkul!'
    else:
        return 'A fajl kodolasa nem megfelelo!'
    
def creating_file_with_value(current_folder, file_to_create, encoded:str, value_in:str) -> str:
    file_created = os.path.join(current_folder, file_to_create)
    encodes = ['utf-8', 'utf-16', 'ansi']
    if encoded in encodes:
        # print('its all good')
        with open(file_created, 'w', encoding=encoded) as f_write:
            f_write.write(value_in)
        return 'A fajl elmentve!'
    else:
        return 'A fajl kodolasa nem megfelelo!'

def create_file(current_folder, file_to_create, encoded:str, value_in:str) -> str:
    if value_in == '':
        message:str
        message = creating_file_without_value(current_folder, file_to_create, encoded)
        return message
    else:
        message:str
        message = creating_file_with_value(current_folder, file_to_create, encoded, value_in)
        return message
    
def creating_folder(current_folder, folder_to_create) -> str:
    if os.path.exists(current_folder) and os.path.exists(os.path.join(current_folder, folder_to_create) == False):
        
        folder_created = os.path.join(current_folder, folder_to_create)
        os.mkdir(folder_created)
        return 'Path has been created!'
    else:
        return 'Current path does not exist!'
    
def create_path_or_folder(file_or_folder:int, current_folder, folder_to_create, file_to_create, encoded:str, value_in:str):
    match file_or_folder:
        case 0:
            message:str = creating_folder(current_folder, folder_to_create)
            return message
        case 1:
            create_file(current_folder, file_to_create, encoded, value_in)
            return message
      
def renaming(from_file, to_file:str) -> str:
    try:
        os.rename(from_file,to_file)
        return 'Renaming OK!'
    except OSError as e:
        return 'Exception handled as {e}'
    


    
if __name__ == '__main__':
    ...
    # open_file("C:/Users/csehg/pytry/Elmelet/ocdo.csv")
#     S = mappa_osztaly(utv)
#     print(S)
#     print(sys.getsizeof(S))




import os
import shutil
from winshell import copy_file, delete_file, move_file, rename_file
from collections import deque
from data.dataclass_file_manager import File
from data.dataclass_folder_manager import Folder
import magic

def simple_data(ut:str, numID:int):
    try:
        match numID:
            case 1: 
                filebase:dict
                filebase = {'Path':str, 'Parent':str, "Folders":deque([])}
                filebase.update({'Path':ut})
                parent:str
                parent, _ = os.path.split(ut)
                filebase.update({'Parent':parent})
                #print(filebase.values())
                filebase.update({"Folders": deque([x for x in os.listdir(ut) if os.path.isdir(os.path.join(ut,x))])})
                #filebase.update({"FilePath": deque([os.path.join(ut,x) for x in filebase.get('Files')])})
                #print(filebase.values())
                return filebase
                
            case 2:
                filebase:dict
                filebase = {'Path':str, 'Parent':str, "Files":deque([])}
                filebase.update({'Path':ut})
                parent:str
                parent, _ = os.path.split(ut)
                filebase.update({'Parent':parent})
                #print(filebase.values())
                filebase.update({"Files": deque([x for x in os.listdir(ut) if os.path.isdir(os.path.join(ut,x)) == False and os.path.ismount(os.path.join(ut,x)) == False])})
                #filebase.update({"FilePath": deque([os.path.join(ut,x) for x in filebase.get('Files')])})
                #print(filebase.values())
                return filebase
            
            case other:
                filebase:dict
                filebase = {'Path':str, 'Parent':str, "Folders":deque([])}
                filebase.update({'Path':ut})
                parent:str
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

        # filebase.update({'Path':ut})
        # parent:str
        # parent, _ = os.path.split(ut)
        # filebase.update({'Parent':parent})
        # #print(filebase.values())
        # filebase.update({"Folders": deque([x for x in os.listdir(ut) if os.path.isdir(os.path.join(ut,x))])})
        # filebase.update({"Files": deque([x for x in os.listdir(ut) if os.path.isdir(os.path.join(ut,x)) == False and os.path.ismount(os.path.join(ut,x)) == False])})
        # #filebase.update({"FilePath": deque([os.path.join(ut,x) for x in filebase.get('Files')])})
        # #print(filebase.values())
        # return filebase
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
    bazis=simple_data(ut, 1)
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
    base = simple_data(ut, 2)
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
    tomb.extend(list(mappasor))
    tomb.extend(list(fajlsor))
    # for m in mappasor:
    #     tomb.append(m)
        
    # for f in fajlsor:
    #     tomb.append(f)
    
    return tomb


def open_the_encoding(current_place) -> str:
    try:
        with open(current_place, 'rb') as reader:
            not_encoded = reader.read()
            m = magic.Magic(mime_encoding=True)
            encoded = m.from_buffer(not_encoded)
            ## print(encoded)
        return encoded
    except:
        return 'utf-8'

def open_file(current_path):
    encoder = open_the_encoding(current_path)
    if encoder != 'binary':
        try:
            with open(current_path, 'r', encoding=encoder ) as reader:
                file_text = reader.read()
                # print(file_text)
                reader.close()
                return file_text, encoder
        except:
            return '', encoder
    else:
        try:
            with open(current_path, 'rb') as reader:
                binary_text = reader.read()
                reader.close()
                return binary_text, 'utf-8'
        except:
            return '', 'utf-8'
    
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
        
def is_exists(path_folder_or_file) -> bool:
    return os.path.exists(path_folder_or_file)
        

def creating_file_without_value(current_folder, file_to_create, encoded:str) -> str:
    file_created = os.path.join(current_folder, file_to_create)
    encodes = ['utf-8', 'utf-16', 'ansi']
    if encoded in encodes:
        # print('its all good')
        match is_exists(file_created):
            case False:
                with open(file_created, 'w', encoding=encoded) as f_write:
                    pass
                return 'A fajl elmentve tartalom nelkul!'
            case True:
                return 'A fajl mar letezik! Nevezze at a fajlt!'
    else:
        return 'A fajl kodolasa nem megfelelo!'
    
def overwriting_existing_file(current_folder, existing_file:str, encoded:str, value_in:str):
    file_created = os.path.join(current_folder, existing_file)
    try:
        with open(file_created, 'w', encoding=encoded) as f_write:
            f_write.write(value_in)
        return 'A fajl elmentve!'
    except OSError:
        return 'A fajl nem talalhato! Kerem probalja a [Mentes maskeppen] segitsegevel!'
    
def creating_file_with_value(current_folder, file_to_create, encoded:str, value_in:str) -> str:
    file_created = os.path.join(current_folder, file_to_create)
    encodes = ['utf-8', 'utf-16', 'ansi']
    if (encoded in encodes) or (encoded.count("ascii") > 0) :
        match is_exists(file_created):
            case False:
                with open(file_created, 'w', encoding=encoded) as f_write:
                    f_write.write(value_in)
                return 'A fajl elmentve!'
            case True:
                'A fajl mar letezik! Nevezze at a fajlt!'
    else:
        return 'A fajl kodolasa nem megfelelo!'

def create_file(current_folder, file_to_create, encoded:str, value_in:str) -> str:
    if (value_in == '') or (value_in == b''):
        message:str
        message = creating_file_without_value(current_folder, file_to_create, encoded)
        return message
    else:
        message:str
        message = creating_file_with_value(current_folder, file_to_create, encoded, value_in)
        return message
    
def creating_folder(current_folder, folder_to_create) -> str:
    if os.path.exists(current_folder):
        match is_exists(os.path.join(current_folder, folder_to_create)):
            case False:
                folder_created = os.path.join(current_folder, folder_to_create)
                os.mkdir(folder_created)
                return 'Mappa letrehozva!'
            case True:
                return 'A mappa mar letezik'
    else:
        return 'A megadott mappa nem letezik'
      
def renaming(from_file, to_file:str) -> str:
    try:
        rename_file(from_file,to_file)
        return 'Atnevezes megtortent sikeresen'
    except:
        return 'Felhasznaloi megszakitas, mint {e}'

def remove_to_recycle_bin(path_file_folder) -> str:
    try:
        delete_file(path_file_folder)
        return 'A fajl eltavolitasa sikeres!'
    except:
        return 'Felhasznaloi megszakitas vegett nem lett eltavolitva!'

def removing_tree(path_to_folder) -> str:
    try:
        shutil.rmtree(path_to_folder)
        return 'A fajl eltavolitasa sikeres!'
    except OSError:
        return 'Rendszerszintu megszakitas vegett nem lett eltavolitva!'
    
def moving_file_to_dest(reg_path,cel_path) -> str:
    match is_exists(cel_path):
        case True:
            try:
                move_file(reg_path, cel_path)
                return 'Athelyezve cel mappaba'
            except:
                return 'Felhasznaloi megszakitas miatt nem lett athelyezve'
                
        case False:
            return 'A celmappa nem letezik'
        
def copy_file_to_dest(file_folder_path, path_to_copy) -> str:
    match is_exists(path_to_copy):
        case True:
            try:
                copy_file(file_folder_path, path_to_copy, no_confirm=True)
                return 'Atmasolva a cel mappaba'
            except:
                return 'Felhasznaloi megszakitas miatt nem lett athelyezve'
                
        case False:
            return 'A celmappa nem letezik'
        
# def open_visual_studio(path_to_file) -> str:
#     try:
#         outp = os.system("C:/Users/csehg/AppData/Local/Programs/Microsoft VS Code/Code.exe", path_to_file)
#         print(outp)
#         return 'Megnyitas'
#     except:
#         return 'A fajl nem nyithato meg!'

    
if __name__ == '__main__':
    ...
    # open_file("C:/Users/csehg/pytry/Elmelet/ocdo.csv")
#     S = mappa_osztaly(utv)
#     print(S)
#     print(sys.getsizeof(S))




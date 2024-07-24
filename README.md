

# PyFileManager ->  ## A simple and lightweight file manager written in Python

## PyFileManager -> ## A simple and lightweight file manager written in Python

### 1. This project was initially created with the goal of accessing files on the Windows operating system.
### 2. It can also access drives and show how much space is occupied on each drive.
### 3. File and folder operations include creating, deleting, and renaming.
### 4. The program is a two-window file manager.
### 5. It is possible to copy and move files from one window to another.


## Installation Instructions:


> 1. Install Python 3.10: [https://www.python.org/downloads/](https://www.python.org/downloads/) or [https://apps.microsoft.com/detail/9pjpw5ldxlz5?hl=en-US&gl=US](https://apps.microsoft.com/detail/9pjpw5ldxlz5?hl=en-US&gl=US)
> ### After installation:
>> 1. Open the Run window by pressing the Windows + R keys.
>> 2. Type *cmd* in the text box and press Enter.
>> 3. You can test if the installation was successful by typing *python -V*.
>>
>> *pip 23.0.1*
>
> 2. Install Python's pip installer library: [https://pypi.org/project/pip/](https://pypi.org/project/pip/) or run the command *python get-pip.py* in the terminal.
> ### After installation:
>> 1. Open the Run window by pressing the Windows + R keys.
>> 2. Type *cmd* in the text box and press Enter.
>> 3. You can test if the installation was successful by typing *pip -V*.
>>
>> *Python 3.10.11*
>
>

## What to do on the first run:
>- ### Open the *bcpywork* folder and run the *setup.py* file once.
>- ### If the packages are installed successfully, you can run the *app.py* file.
>- ### If the installation is unsuccessful, the *dependencies* section in the *config.yaml* file lists all the modules and packages that the program uses.
> ### However, all the modules and packages and their installation are listed in the lower part:
>>  - dataclasses
>> *python -m pip install dataclasses*
>>  - collections
>> *python -m pip install collections*
>>  - PySimpleGUI
>> *python -m pip install PySimpleGUI*
>> - cffi
>> *python -m pip install cffi*
>> - pyperclip
>> *python -m pip install pyperclip*
>> - keyboard
>> *python -m pip install keyboard*
>> - winshell
>> *python -m pip install winshell*
>> - python-magic
>> *python -m pip install python-magic*
>> - python-libmagic
>>*pip install python_magic_bin-0.4.14-py2.py3-none-win_amd64.whl* or *pip install python-magic-bin*
>> - pathlib
>> *python -m pip install pathlib*
>> - Tk
>> *python -m pip install tk*
>> - pywin32-stubs
>> *python -m pip install pywin32-stubs*
>> - pywin32 
>> *python -m pip install pywin32*
>> - win32api
>> *python -m pip install win32api*

- Upon successful launch, the Drives window can be opened to show the list of drives!

- If a drive is connected, it is necessary to reopen the Drives window!

- After loading the drive, the listed files and folders are visible on the given Table

- Folders can be opened by double-clicking and pressing Enter.

- It is also possible to copy and move files from one Table to another using the right-click menu.


## Installation Instructions:

### 1. Install Python 3.10:

* [https://www.python.org/downloads/](https://www.python.org/downloads/)
* 


### 1. Ez a projekt azzal a céllal indult, hogy egy a Windows operációs rendszeren elérjük a fájlokat. 
### 2. Továbbá eléri a meghajtókat, meg tudja mutatni mennyire van elfoglalva egyes meghajtó. 
### 3. A fájlokkal és mappákkal való tevékenységek közé tartozik a létrehozás, eltávolítás és átnevezés. 
### 4. A program két ablakos fájlkezelő. 
### 5. Egyik ablakból van lehetőség átmásolni és áthelyezni. 


## Telepítési instrukciók:


> 1. Python 3.10 verziójának a telepítése: https://www.python.org/downloads/windows/ vagy https://apps.microsoft.com/store/detail/python-311/9NRWMJP3717K
> ### Telepítés után:
>> 1. Windows + R gomb kombinációval megnyitni a Futtatás Ablakot. 
>> 2. Szövegdobozba *cmd* és Enter gomb. 
>> 3. *python -V* szöveggel tesztelhetjük sikerült-e telepíteni a csomagot.
>>
>> *pip 23.0.1*
>
> 2. Python pip telepítő könyvtárának telepítése: https://pip.pypa.io/en/stable/installation/ vagy a *python get-pip.py* parancssal a terminálban. 
> ### Telepítés utáni teendő:
>> 1. Windows + R gomb kombinációval megnyitni a Futtatás Ablakot. 
>> 2. Szövegdobozba *cmd* és Enter gomb. 
>> 3. *pip -V* szöveggel tesztelhetjük sikerült-e telepíteni a csomagot
>>
>> *Python 3.10.11*
>
>

## Első indításnál szükséges teendők:
>- ### A *bcpywork* mappa megnyitása után a *setup.py* fájlt kell egyszer lefuttatni. 
>- ###  A sikeres package telepítések esetén az *app.py* fájl futtaható. 
>- ### A sikertelen telepítés esetén a *config.yaml* fájlban található *dependencies* részben található minden egyes modul és package, amit a program használ
> ### Azonban az alsó részben minden egyes modul és package fel lesz sorolva minden egyes modul és annak telepítése:
>>    - dataclasses
>> *python -m pip install dataclasses*
>>    - collections
>> *python -m pip install collections*
>>    - PySimpleGUI
>> *python -m pip install PySimpleGUI*
>>  - cffi
>>  *python -m pip install cffi*
>>  - pyperclip
>> *python -m pip install pyperclip*
>>  - keyboard
>> *python -m pip install keyboard*
>>  - winshell
>> *python -m pip install winshell*
>>  - python-magic
>> *python -m pip install python-magic*
>>  - python-libmagic
>>*pip install python_magic_bin-0.4.14-py2.py3-none-win_amd64.whl* vagy *pip install python-magic-bin*
>>  - pathlib
>>  *python -m pip install pathlib*
>>  - Tk
>>  *python -m pip install tk*
>>  - pywin32-stubs
>>  *python -m pip install pywin32-stubs*
>>  - pywin32 
>> *python -m pip install pywin32*
>>  - win32api
>>  *python -m pip install win32api*

- Sikeres elindításnál a Diszkek ablakkal lehet megnyitni a meghajtók listáját!

- Csatlakoztatott meghajtó esetén szükséges mégegyszer megnyitni a Diszkek ablakát!

- A maghajtó betöltése után kilistázott fájlok és mappák láthatóak az adott Asztalon

- A mappák megnyitása két kattintás után és egy Enter billentyű lenyomása után fog megnyitni.

## Továbbá lehetőség van az egyik Asztalról való megnyitására a Másik Asztalra a Jobb klikk menüből kiválasztva.


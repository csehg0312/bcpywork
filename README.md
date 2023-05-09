# PyFileManager ->  ## A simple and lightweight file manager written in Python
// This documentation is written in Hungarian language at first 


### 1. Ez a projekt azzal a céllal indult, hogy egy a Windows operációs rendszeren elérjük a fájlokat. 
### 2. Továbbá eléri a meghajtókat, meg tudja mutatni mennyire van elfoglalva egyes meghajtó. 
### 3. A fájlokkal és mappákkal való tevékenységek közé tartozik a létrehozás, eltávolítás és átnevezés. 
### 4. A program két ablakos fájlkezelő. 
### 5. Egyik ablakból van lehetőség átmásolni és áthelyezni. 


## Telepítési instrukciók:


> 1. Python 3.10 verziójának a telepítése: https://www.python.org/downloads/windows/
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
>>    - pyperclip
>> *python -m pip install pyperclip*
>>    - keyboard
>> *python -m pip install keyboard*
>>    - winshell
>> *python -m pip install winshell*
>>    - python-magic
>> *python -m pip install python-magic*
>>



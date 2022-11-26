import data.disk_util as du
import os

def drive_inserted():
    dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    def csatlakozas():
        print("New drive introduced")
        return 0

    def lecsatlakozas():
        print("Drive disconnect")
        return 0

        
    notyetchecked = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]

    lk = du.diferencia(notyetchecked , du.drives)

    if lk:
        csatlakozas()
        du.drives = notyetchecked
        return 2
    lk = du.diferencia(du.drives, notyetchecked)

    if lk:
        lecsatlakozas()
        du.drives = notyetchecked
        return 1
    else:
        return 0
drive_val = drive_inserted()
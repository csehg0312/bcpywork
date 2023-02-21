import os.path
import shutil


def diferencia(ls1,ls2):
    ls_diferencia = [item for item in ls1 if item not in ls2]
    return ls_diferencia

dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]



if __name__ == '__main__':
    print(drives)
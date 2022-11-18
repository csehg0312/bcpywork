import shutil
import disk_manager as dm

disk = dm.drives
disks_data = {}

def popper(arg):
    disk = arg
    data = getter(disk)
    data.update({"disk": disk})
    return data

def getter(arg):
    disk = arg
   
    dtotal, dused, dfree = shutil.disk_usage(disk)
    dtotal = dtotal // (2**30)
    dused = dused // (2**30)
    dfree = dfree // (2**30)
    data = {'total': dtotal, 'used':dused, 'free':dfree}
    return data

for item in range(len(disk)):
       data = popper(disk[item])
       disks_data.update({disk[item]:data})

if __name__ == '__main__':
   ''' for item in range(len(disk)):
       data = getter(disk[item])
       print(str(data)) '''
   
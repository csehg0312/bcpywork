import dspace_manager as dsp
import disk_util as dm

#dsp.full(dm.drives)

disk_data = dsp.disks_data
#print(str(disk_data))


for item in range(0,len(dm.drives), 1):
    drive = dm.drives
    
    try:
        print(disk_data.pop(drive.pop()))

    except KeyError:
        print(f"{disk_data.keys()} are just these")
    

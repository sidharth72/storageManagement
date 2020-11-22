import os , shutil

try:
    os.chdir('/storage/emulated/0/')
    path = '/storage/emulated/0/DCIM/Camera'

    for file in os.listdir(path):
        shutil.move(os.path.join(path,file),'/storage/emulated/0/Pictures/camera')
        print('successfully moved!')
except:
    print('Error occured')
    
  

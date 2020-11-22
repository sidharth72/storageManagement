import os , shutil

try:
    os.chdir('/storage/emulated/0/')
    #path of file that want to be moved
    path = '/storage/emulated/0/DCIM/Camera'
    
    #looping through path we get all files in the folder
    for file in os.listdir(path):
        #moving it by shutil module
        shutil.move(os.path.join(path,file),'/storage/emulated/0/Pictures/camera')
        print('successfully moved!')
except:
    print('Error occured')
    
  

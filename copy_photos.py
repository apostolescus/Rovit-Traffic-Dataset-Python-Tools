import os
from shutil import copy
import sys

cwd = os.getcwd()
source_name = str(sys.argv[1]).split("/")[0] # annotation folder
img_folder_name = str(sys.argv[2]) #img folder

dest_folder = source_name + "_photos" #destination folder
dest_folder_path = os.path.join(cwd, dest_folder)

try:
    os.mkdir(dest_folder_path)
except:
    print("file already exists")

source_dest = os.path.join(cwd, source_name)
img_folder = os.path.join(cwd, img_folder_name)

def read_annotations():

    f_list = os.listdir(source_dest)    
    
    for f in f_list:
        img_name = f.split(".")[0]+".jpg"
        #print(img_name)
        final_img = os.path.join(img_folder, img_name)
        
        copy(final_img, dest_folder)
        
read_annotations()

        
        
        


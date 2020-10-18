#extrage toate annotarile care contin clasa data ca parametru
import os
from shutil import copy
import sys

selected_class = int(sys.argv[1])
cwd = os.getcwd()
des_file = os.path.join(cwd, str(selected_class))
src_file = os.path.join(cwd, "Formatted_Annotations_updated")

def add_to_dict(dictz, class_id):
    
    if class_id not in dictz.keys():
        dictz[class_id] = 1
    else:
        dictz[class_id] += 1
               
def parse_txt():
    
    try:
        os.mkdir(des_file)
    except:
        print("folder already exists")
        
    elements = os.listdir(src_file)
    
    for elem in elements:
        
        line_dict = {}
        file_path = os.path.join(src_file, elem)
        f_open = open(file_path, "r")
        line = f_open.readline().split("\n")[0].split()

        if line != []:
            class_id = line[0]
            add_to_dict(line_dict, class_id)
        
        while line:
            
                line = f_open.readline().split("\n")[0].split() 
                if line != []:
                    class_id = line[0]
                    add_to_dict(line_dict, class_id)
        
        #print(line_dict, elem)
        if str(selected_class) in line_dict.keys():
            file_source_path = os.path.join(src_file, elem)
            copy(file_source_path, des_file)     
            #print("copied")
        #print(line_dict, elem)
        
        
parse_txt()
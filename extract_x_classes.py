#extrage x elemente din folderul corespunzator unei clase
import os
import sys
from shutil import copy
from collections import Counter

cwd = os.getcwd()

source_folder = sys.argv[1] #folderul cu annotari
number = int(sys.argv[2]) #numarul de anotari
class_id = int(source_folder) #id ul clasei

source_path = os.path.join(cwd, source_folder)
dest_folder = str(source_folder) + "_"+str(number)

dest_path = os.path.join(cwd, dest_folder)
print(dest_path)
try:
    os.mkdir(dest_path)
except:
    print("Folder already existed")


classes_dict = {}

def init_dict():
    global classes_dict
    for i in range(0,5):
        classes_dict[str(i)] = 0
    
def check_dict():
    
    if classes_dict[str(class_id)] <= number:
        return False
    else:
        return True
    
def add_dicts(temp_dict, classes_dict):
    
    a = Counter(temp_dict) + Counter(classes_dict)
    print(a)
    return dict(a)
    
def add_to_dict(cl_id, temp_dict):
    
    try:
        temp_dict[cl_id] += 1
    except:
        temp_dict[cl_id] = 1
        
def check_dict_proportions(temp_dict):
         
        #interest_class_number = cl_id
        try:
            class_nr = int(temp_dict[str(class_id)])
        except:
            class_nr = 0
            
        v=list(temp_dict.values())
        k=list(temp_dict.keys())
        
        
        try:
            max_val = max(v)
            max_item = k[v.index(max(v))]
        except:
            return True
        
        if max_val == 0:
            return False
        
        #("check dict proportions: ", class_nr, max_val)
        
        if str(k) == str(class_id):
            return True
        
        if class_nr  < max_val and class_nr != 0:
            return False
        
        return True
                    
        
def read_classes():
    
    global classes_dict
 
    files = os.listdir(source_folder)
    
    for f in files:
        temp_dict = {}
        
        file_path = os.path.join(source_path, f)
        f_handler = open(file_path,"r")
        
        line = f_handler.readline().split("\n")[0].split()
        
        if line != []:
            class_ident = line[0]
            add_to_dict(class_ident, temp_dict)    
        
        while line:
            line = f_handler.readline().split("\n")[0].split()
            
            if line != []:
                class_ident = line[0]
                add_to_dict(class_ident, temp_dict)
        #(temp_dict, classes_dict)       
        
        if check_dict_proportions(temp_dict) is True:
            copy(file_path, dest_path)
            #print(temp_dict)
            
            b = add_dicts(temp_dict, classes_dict)
            classes_dict = b
            #print(classes_dict)
            if check_dict() is True:
                return 
            
init_dict()       
read_classes()
    
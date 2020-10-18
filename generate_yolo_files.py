import os
import sys

cwd = os.getcwd()

folder_name = sys.argv[1]
procentage = sys.argv[2]

train_outf = "train.txt"
validate_outf = "validate.txt"

train_path = os.path.join(cwd, train_outf)
validate_path = os.path.join(cwd, validate_outf)

folder_path = os.path.join(cwd, folder_name)

def current_pth():
    
    
    
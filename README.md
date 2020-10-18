# Rovit-Traffic-Dataset Python-Tools :trollface:

Dataset: http://www.rovit.ua.es/dataset/traffic/
This scripts help the user understand, convert to YOLO format and extract useful information from this dataset.

Each class is numberd from 0 - 6.
# Scripts:
### 1. ***generate_yolo_files***
 
  Converts xml file selecting specific classes to yolo format.
  Read the files from "Annotations" and save yolo txts in "Formatted_Annotations".
  Generates information file with each class number in "dataset_infos".
  Personalize the classes you want in "class_list".

### 2. ***get_ds_infos***

  Args: target_folder  
  Reads all files from the target folder (must be in YOLO format) and generates informations about the classes.

### 3. ***extract_class_images***

  Args: selected class ( number from 0 to 6).
  Generates new folder with this name if doesn't exist.
  The new folder has all the txts that contains that class.

### 4. ***extract_x_classes.py***

  Args: annotations folder path, number of classes to extract, class id
  Extracts x txt from te annotations folder coresponding to the class_id.

  The output folder has the following format: annotation.folder_name_x

  Ex: extract_x_classes ./1 2000 
  where:   2000 - the number of classes   
  1 - class id  
  out_folder: 1_2000 

### 5. ***copy_photos.py***
  Args: annotation folder, imgages folder
  Copies the images that are annotated in annotation_folder from image_folder to a new annotation_folder+ "_photos" folder.






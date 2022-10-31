import os
import sys
import json


def get_files(folder_path, file_type):
    
    # check if folder exists
    if os.path.isdir(folder_path):
        
        files = []
        files_and_folders = os.listdir(folder_path)
        for element in files_and_folders:
            if file_type in element:
                element_path = os.path.abspath(element)
                files.append(element_path)
        return files
    else:
        print("Folder does not exists!")
        
# print(get_files(folder_path=r"D:\PYTHON_ADVANCED_COURSE\folder_for_testing", file_type=".mp4"))


def get_json_data(json_path):
    try:
        with open(json_path, "r") as f:
            file_data = f.read()
            json_data = json.loads(file_data)
            return json_data
    except:
        print("file does not exists!")
        
        


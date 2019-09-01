"""
Duplicate a folder structure without copying any files. Was used by accounting department to create invoices folders every new fiscal year
"""

import os

def create_folder(new_folder):
    if os.path.exists(new_folder):
        print("Already exists : " + new_folder)
        pass
    else :
        print("Creating : " + new_folder)
        os.mkdir(new_folder)

source_folder = ""
destination_folder = ""

source_directory = os.path.dirname(source_folder)

for folder in os.listdir(source_directory):
    path = source_directory + "/" + folder
    if os.path.isdir(path):
        new_path = destination_folder + "/" + folder
        print("is dir " + path)
        create_folder(new_path)
        for sub_folder in os.listdir(path):
            sub_path = path + "/" + sub_folder
            if os.path.isdir(sub_path):
                new_sub_path =  new_path + "/" + sub_folder
                print("is subdir " + sub_path)
                create_folder(new_sub_path)
            else:
                print("is a file : " + sub_path)

    else:
        print("is a file : "  + path)


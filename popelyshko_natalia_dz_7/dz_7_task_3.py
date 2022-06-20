import os
import shutil


def process_dir(scan_name: str, dest_path: str):
    for entity_dir in os.scandir(scan_name):
        if entity_dir.is_dir():
            if entity_dir.name == 'templates':
                for entity_dir2 in os.scandir(entity_dir.path):
                    if entity_dir2.is_dir():
                        print("src", entity_dir2.path)
                        print ("dec", dest_path)
                        #shutil.copytree(entity_dir2.path, dest_path)
                        shutil.move(entity_dir, dest_path+"/templates")
            else:
                process_dir(entity_dir.path, dest_path)


for entity_dir in os.scandir("./data/task_3/my_project"):
    if entity_dir.is_dir() and entity_dir.name != 'templates':
        process_dir(entity_dir.path, "./data/task_3/my_project/templates/")


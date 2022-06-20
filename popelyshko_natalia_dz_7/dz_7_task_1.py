import os

project_name: str = "my_project"
directories = open("./data/task_1.txt", "r").readlines()

for dir in directories:
    if not os.path.exists(project_name+"/"+dir):
        os.makedirs(project_name+"/"+dir)

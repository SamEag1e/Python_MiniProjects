"This module moves all dirs inside of givesn path, to the path itself."
import os
import shutil

path = input("path: ")
print(os.listdir(path))

for directory in os.listdir(path):
    for file in os.listdir(f"{path}/{directory}"):
        shutil.move(f"{path}/{directory}/{file}", path)
    os.rmdir(f"{path}/{directory}")

import os

def findallfile(path):
    f = os.listdir(path)
    files = []
    for file in f:
        if '.csv' in file:
            files.append(file)
    return files

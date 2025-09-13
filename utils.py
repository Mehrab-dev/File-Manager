import os

def list_dir(path:str) :
    if not os.path.exists(path) :
        return "There is wrong path"
    item = os.listdir(path)
    if not item :
        return "There is noting"
    return item

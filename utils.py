import os
import shutil

def list_dir(path:str) :
    if not os.path.exists(path) :
        return "There is wrong path"
    item = os.listdir(path)
    if not item :
        return "There is noting"
    return item

def create_folder(path:str,name) :
    new_path = os.path.join(path,name)
    if os.path.exists(new_path) :
        return "Folder already exists"
    else :
        os.mkdir(new_path)
        return "Create Folder"

def delete_folder(path:str,name) :
    delete = os.path.join(path,name)
    if not os.path.exists(delete) :
        return "There is noting"
    else :
        if os.path.isfile(delete) :
            os.remove(delete)
            return "Deleted your file"
        elif os.path.isdir(delete) :
            shutil.rmtree(delete)
            return "Deleted your Folder"



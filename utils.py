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

def delete_item(path:str,name) :
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

def move_item(current_path:str,new_path:str,name) :
    ex_path = os.path.join(current_path,name)
    if not os.path.exists(ex_path) :
        return "The current path is incorrect"
    if not os.path.exists(new_path) :
        return "The new path is incorrect"
    if os.path.isfile(ex_path) :
        shutil.move(ex_path,new_path)
        return "File moved to new destination"
    if os.path.isdir(ex_path) :
        shutil.move(ex_path,new_path)
        return "Folder moved to new destination"
    else :
        return "unknown item type"

def create_file(path:str,name) :
    cr_file = os.path.join(path,name)
    if os.path.exists(cr_file) :
        return "Similar File exists"
    with open(cr_file,"w") :
        pass
    return "Create File"

def copy_file(ex_path:str,new_path:str,name) :
    my_file = os.path.join(ex_path,name)
    dest_file = os.path.join(new_path,name)
    if not os.path.exists(my_file) :
        return "File does not exists"
    if os.path.exists(dest_file) :
        return "Similar File exists"
    shutil.copy2(my_file, dest_file)
    return "File is Copy"






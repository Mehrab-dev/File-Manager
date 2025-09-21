import utils

def test_list() :
    assert utils.list_dir(r"C:\Users\XMART\Desktop\text") == ['python.py','pythonnn']
    assert utils.list_dir(r"C:\Users\XMART\Desktop\tex") == "There is wrong path"
    assert utils.list_dir(r"C:\Users\XMART\Desktop\test3") == "There is noting"

def test_create_folder() :
    assert utils.create_folder(r"C:\Users\XMART\Desktop\text","pythonnn") == "Create Folder"
    assert utils.create_folder(r"C:\Users\XMART\Desktop\text","pythonnn") == "Folder already exists"

def test_delete_item() :
    assert utils.delete_item(r"C:\Users\XMART\Desktop\test3","python.py") == "There is noting"
    assert utils.delete_item(r"C:\Users\XMART\Desktop\text","new.txt") == "Deleted your file"
    assert utils.delete_item(r"C:\Users\XMART\Desktop\text","pythonnn") == "Deleted your Folder"

def test_move_item() :
    assert utils.move_item(r"C:\Users\XMART\Desktop\text2",r"C:\Users\XMART\Desktop\text","python.py") == "File moved to new destination"
    assert utils.move_item(r"C:\Users\XMART\Desktop\text",r"C:\Users\XMART\Desktop\text2","python") == "Folder moved to new destination"
    assert utils.move_item(r"C:\Users\XMART\Desktop\text4",r"C:\Users\XMART\Desktop\text","python") == "The current path is incorrect"
    assert utils.move_item(r"C:\Users\XMART\Desktop\text2",r"C:\Users\XMART\Desktop\texxt","Django") == "The new path is incorrect"

def test_create_file() :
    assert utils.create_file(r"C:\Users\XMART\Desktop\text","pyqt.py") == "Create File"
    assert utils.create_file(r"C:\Users\XMART\Desktop\text","python.py") == "Similar File exists"

def test_copy_file() :
    assert utils.copy_file(r"C:\Users\XMART\Desktop\text",r"C:\Users\XMART\Desktop\text2","python.py") == "File is Copy"
    assert utils.copy_file(r"C:\Users\XMART\Desktop\text",r"C:\Users\XMART\Desktop\text2","pyqttt.py") == "File does not exists"
    assert utils.copy_file(r"C:\Users\XMART\Desktop\test3",r"C:\Users\XMART\Desktop\text","python.py") == "Similar File exists in destination"

def test_copy_folder() :
    assert utils.copy_folder(r"C:\Users\XMART\Desktop\text2",r"C:\Users\XMART\Desktop\text","python") == "Folder copied"
    assert utils.copy_folder(r"C:\Users\XMART\Desktop\text2",r"C:\Users\XMART\Desktop\text","javascript") == "Folder does not exists"
    assert utils.copy_folder(r"C:\Users\XMART\Desktop\text2",r"C:\Users\XMART\Desktop\test3","Django") == "Similar Folder exists in destination"

def test_rename_item() :
    assert utils.rename(r"C:\Users\XMART\Desktop\text","my_project.py","python.py") == "File renamed"
    assert utils.rename(r"C:\Users\XMART\Desktop\text","python","RestApi") == "Folder renamed"
    assert utils.rename(r"C:\Users\XMART\Desktop\text","pyqt.py","pyqt.py") == "Similar File exists in destination"
    assert utils.rename(r"C:\Users\XMART\Desktop\text2","football","football") == "Similar Folder exists in destination"
    assert utils.rename(r"C:\Users\XMART\Desktop\text2","sport","data") == "item does not exists"
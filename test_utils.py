import utils

def test_list() :
    assert utils.list_dir(r"C:\Users\XMART\Desktop\text") == ['python.py','pythonnn']
    assert utils.list_dir(r"C:\Users\XMART\Desktop\tex") == "There is wrong path"
    assert utils.list_dir(r"C:\Users\XMART\Desktop\test3") == "There is noting"

def test_create_folder() :
    assert utils.create_folder(r"C:\Users\XMART\Desktop\text","pythonnn") == "Create Folder"
    assert utils.create_folder(r"C:\Users\XMART\Desktop\text","pythonnn") == "Folder already exists"


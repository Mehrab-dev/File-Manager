from utils import list_dir


if __name__ == "__main__" :
    show_list = list_dir(path=r"C:\Users\XMART\Desktop\text")
    if isinstance(show_list,list) :
        for i in show_list :
            print(i)
    else :
        print(show_list)

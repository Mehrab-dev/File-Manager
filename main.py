from utils import list_dir,create_folder,delete_folder
import argparse

parser = argparse.ArgumentParser(description="Smile File Manager")
sub_argument = parser.add_subparsers(dest="command")
list_argument = sub_argument.add_parser("list",help="list item in your Folder")
list_argument.add_argument("path",help="path of the folder to list")

c_folder = sub_argument.add_parser("cf",help="Create Folder in your path")
c_folder.add_argument("path",help="Path of the Folder to Create")
c_folder.add_argument("name",help="Name for new Folder")

d_folder = sub_argument.add_parser("d",help="Delete File or Folder to list")
d_folder.add_argument("path",help="Path of the File or Folder to Delete")
d_folder.add_argument("name",help="Name for Delete File or Folder")
args = parser.parse_args()

if args.command == "list" :
    result = list_dir(args.path)
    if isinstance(result,list) :
        for i in result :
            print(i)
    else :
        print(result)

if args.command == "cf" :
    result = create_folder(args.path,args.name)
    print(result)

if args.command == "d" :
    result = delete_folder(args.path,args.name)
    print(result)



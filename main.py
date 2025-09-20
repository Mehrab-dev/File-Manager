from utils import list_dir,create_folder,delete_item,move_item
from utils import create_file,copy_file,copy_folder,rename
import argparse

parser = argparse.ArgumentParser(description="Smile File Manager")
sub_argument = parser.add_subparsers(dest="command")
list_argument = sub_argument.add_parser("list",help="list item in your Folder")
list_argument.add_argument("path",help="path of the folder to list")

cr_folder = sub_argument.add_parser("cf",help="Create Folder in your path")
cr_folder.add_argument("path",help="Path of the Folder to Create")
cr_folder.add_argument("name",help="Name for new Folder")

d_folder = sub_argument.add_parser("d",help="Delete File or Folder to list")
d_folder.add_argument("path",help="Path of the File or Folder to Delete")
d_folder.add_argument("name",help="Name for Delete File or Folder")

move = sub_argument.add_parser("move",help="for move File or Folder")
move.add_argument("ex_path",help="ex path for moved")
move.add_argument("new_path",help="new path for moved")
move.add_argument("name",help="Name File or Folder for moved")

cr_file = sub_argument.add_parser("cfile",help="for create file")
cr_file.add_argument("path",help="Path of the File to Create")
cr_file.add_argument("name",help="Name for new File")

c_file = sub_argument.add_parser("copy_file",help="For copy file")
c_file.add_argument("ex_path",help="File source address")
c_file.add_argument("new_path",help="File destination address")
c_file.add_argument("name",help="Name of the desired File")

c_folder = sub_argument.add_parser("copy_folder",help="to copy a folder")
c_folder.add_argument("ex_path")
c_folder.add_argument("new_path")
c_folder.add_argument("name")

rn = sub_argument.add_parser("rename",help="to rename a folder or file")
rn.add_argument("path",help="Folder path")
rn.add_argument("old_name")
rn.add_argument("new_name")

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
    result = delete_item(args.path,args.name)
    print(result)

if args.command == "move" :
    result= move_item(args.ex_path,args.new_path,args.name)
    print(result)

if args.command == "cfile" :
    result = create_file(args.path,args.name)
    print(result)

if args.command == "copy_file" :
    result = copy_file(args.ex_path,args.new_path,args.name)
    print(result)

if args.command == "copy_folder" :
    result = copy_folder(args.ex_path,args.new_path,args.name)
    print(result)

if args.command == "rename" :
    result = rename(args.path,args.old_name,args.new_name)
    print(result)
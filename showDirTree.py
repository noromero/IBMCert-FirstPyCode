#!/usr/bin/env python3

import os

## Scan and return list of all folders and subfolders
def f_scandir(dirname):
  subfolders= sorted([f.path for f in os.scandir(dirname) if f.is_dir() and f.name!='.git'])
  for dirname in list(subfolders):
    subfolders.extend(f_scandir(dirname))
    
  return subfolders

## Scan and return list of all files in current folder
def f_scanfil(dirname):
  return sorted([f.name for f in os.scandir(dirname) if f.is_file()])

## Generate and return dictionary with folders and content
def getTree():
  tree = {
    '':f_scanfil('.')
    }
  subdir_list=f_scandir('.')
  for folder in subdir_list:
    tree[folder[2:]]=f_scanfil(folder)
  return tree
  
## print dictionary with filepath and contents
def printTree(display_path=False, group_files=True, hide_empty_folders=False):
  current_tree=getTree()
  print("\nPrint Options:\ndisplay_path= {}\ngroup_files= {}\nhide_empty_folders= {}\n".format(display_path,group_files,hide_empty_folders))
  for foldername,files in current_tree.items():
    
    if(hide_empty_folders and len(files)==0):
      continue
      
    if(display_path):
      print("{}".format(os.path.join(os.getcwd(),foldername)))
    else:
      print("{}".format(foldername))
      
    if len(files)>0:
      if(group_files):
        print("\t{}\n".format(files))
      else:
        for x in range(0,len(files)):
          print("\t{}".format(files[x]))
          

if __name__ == '__main__':
  ask=input("Would you like to change print options? (y/n): ")
  if(ask=='y' or ask=='Y'):
    
    df=input("display filepath? (y/n): ")
    gf=input("group files? (y/n): ")
    hef=input("hide empty folders? (y/n): ")
    printTree(
      display_path=(df=='y'), 
      group_files=(gf=='y'),
      hide_empty_folders=(hef=='y')
      )
  else:
    printTree()  
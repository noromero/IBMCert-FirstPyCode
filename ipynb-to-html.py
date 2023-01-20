#!/usr/bin/env python3

import os
import subprocess
import re

## Scan and return list of all folders and subfolders
def f_scandir(dirname):
  subfolders= sorted([f.path for f in os.scandir(dirname) if f.is_dir()])
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
def printTree(display_path=True, group_files=True, hide_empty_folders=False):
  current_tree=getTree()
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

def convertFiles():
  jf=getTree()
  #print("Preparing file names for comparison")
  correct_names=[]
  for f in jf['']:
    newstr=''
    if (f[-6:]=='.ipynb'):
      newstr=re.search(r"^(bnypi.).+[-\d]",f[::-1]).group()[::-1]
      correct_names.append(newstr)
      #os.rename(f,newstr)
  #print("Formatted Files:\t{}".format(correct_names))
  
  for f in correct_names:
    print("\tChecking if '{}' has been converted".format(f))
    if (f[:-6]+".html") not in jf['html']:
      subprocess.run(["jupyter", "nbconvert", "--to=html","--output-dir=html", f])
      print("\tconversion successful")  
  

correct=['1-1-Write_your_first_python_code.ipynb', '1-2-Strings.ipynb', '2-1-Tuples.ipynb', '2-2-Lists.ipynb', '2-3-Sets.ipynb', '2-4-Dictionaries.ipynb', '3-1-Conditions.ipynb', '3-1.2ExcecptionHandling.ipynb', '3-2-Loops.ipynb', '3-3-Functions .ipynb', '3-4-Classes.ipynb', '4-1-ReadFile.ipynb', '4-2-WriteFile.ipynb', '4-3-LoadData.ipynb', '4_Pandas_Practice.ipynb', '5-1-Numpy1D.ipynb', '5-2-Numpy2D.ipynb', '5-x-WebScraping_Review_Lab.ipynb', '5.1_Intro_API.ipynb', '5.2_API_2.v2.ipynb', '5.3_Requests_HTTP.ipynb', '5.4_WorkingWithDifferentFileTypes.ipynb']
for item in correct:
  for file in os.listdir():
    if(file in item and file!=item):
      os.rename(file,item)
      
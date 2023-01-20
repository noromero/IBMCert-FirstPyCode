#!/usr/bin/env python3

import os
import subprocess
import re
from showDirTree import getTree


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
  print("Formatted Files:\t{}".format(correct_names))
  
  """
  for f in correct_names:
    print("\tChecking if '{}' has been converted".format(f))
    if (f[:-6]+".html") not in jf['html']:
      subprocess.run(["jupyter", "nbconvert", "--to=html","--output-dir=html", f])
      print("\tconversion successful")  
  """

if __name__=='__main__':
  convertFiles()
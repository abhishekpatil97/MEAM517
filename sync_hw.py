"""
Synchronize homework files (either save files to google drive or copy files from github to google drive) 
"""
import os
from os import path
from shutil import copyfile
import urllib.request
from pathlib import Path
import re

def sync_hw(hw_id, files):
  if 'google.colab' in str(get_ipython()):
    # mount google drive to Colab
    from google.colab import drive
    drive.mount('/content/drive')

    dir = "drive/My Drive/MEAM517_colab/hw"+str(hw_id)+"/"
    git_url = "https://raw.githubusercontent.com/mposa/MEAM517/master/hw"+str(hw_id)+"/"

    for file in files:
      # download the file from github to google drive if it doesn't exist 
      if not path.exists(dir + file):
        # create hw folder in google drive if it doesn't exist
        if not path.exists(dir):
          Path(dir).mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(git_url + file, dir + file)

      # create a symbolic link to the file in google drive if it doesn't exist
      if not path.exists(file): 
        os.system("ln -s " + re.escape(dir) + file + " " + file)

'''CSCI 204 Lab 03 Recursion
Lab section: CSCI 204.L62, Thursday 1:00-2:50pm
Student name: Nahom  Ayele, Yuqin Yang
Instructor name: Professor Fuchsberger'''

import os, sys 

class FileStats:
  """This class gives us information about the files in our Directory """
  def __init__(self, max_size = 0, min_size = sys.maxsize, max_file = 0, min_file = 0):
    self.max_size = max_size
    self.min_size = min_size
    self.max_file = max_file
    self.min_file = min_file

  def print_results(self):
    print(f'maximum size among files : {str(self.max_size)} ({self.max_file})\nminimum size among files : {str(self.min_size)} ({self.min_file})')
      
  def update(self, filename):
    size = os.lstat(filename).st_size
    if size > self.max_size:
      #if the size of our file is larger than the max size we set that as the new max size and we also set it as the new name of the max file.
      self.max_size = size
      self.max_file = filename
    if size<self.min_size:
      # if the size of our filename is smaller than the min size, we set the min size to the new one, and the min_file name to the new filename.
      self.min_size = size
      self.min_file = filename

def list_dir (basedir,fstats):
    path = basedir
    directories = []

    answer= path.split("/")

    print ( "--Entering :", answer[-1])

    
    if not os.path.isdir(path):
      print(path)
      return

    else:
      for f in os.listdir(path):
        print(f)
        v = os.path.join( path, f )
        fstats.update(v)
        #for each file we have to update the new sizes

        if not os.path.isfile(v):
          directories.append(v)

      for i in directories:
        list_dir(i,fstats)
        
        
    print("--Leaving " + answer[-1])
  


basedir = input('Enter a starting directory or file: ')
# fstats = FileStats(42,42,"testfile.txt")
# print(fstats.print_results())
fstats = FileStats()

# print ( f'--Entering : {basedir}')
basedir = basedir[:-1]
list_dir( basedir, fstats )
# print ( f'--Leaving : {basedir} ')
fstats.print_results()


  
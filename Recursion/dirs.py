"""
   This exercise asks students to write a recursive program to visit 
   a Unix direcory tree recursively starting from a giving directory. Print
   only the file name when visiting. 

   Students are not allowed to use the os.walk() method, which
   basically does the recursion.
 
   Date  : Fall 2013
   Revised: 2019-11-05
"""

import os, sys

def list_dir ( start_dir ):
    """ 
        list_dir lists the contents of a starting directory
        and the contents of all its subdirectories recursively.
        
        Input:
           start_dir - name of the starting directory
        Output: a complete list of contents of all subdirectories
    """

    # Set the starting directory and retrieve its contents
    path = start_dir
    directories = []

    answer= path.split("/")
    print ( "--Entering :", answer[-1])
    

    # Check if a path is not a directory
    if not os.path.isdir(path):
      print(path)
      return
      # Print the contents in this directory
      # List everything
    else:
      for f in os.listdir(path):
        print(f)
        v = os.path.join( path, f )

        if not os.path.isfile(v):
          directories.append(v)

      for i in directories:
        list_dir(i)
        #we loop through our Directory and recursively vall our function to print the files in that directory
        
    print("--Leaving " + answer[-1])
      

        
          
       

         
      # for f in os.listdir( path ):
      #     # Convert it into a complete path, needed for 'isdir()'
      #     # 'v' will be needed to run 'isdir()' when recursive call is made
      #     v = os.path.join( path, f )
      #     if os.path.isfile(v) == True:
      #       files.append(f)
      #     # list_dir(os.listdir( v ))
      #     if os.path.isdir(v) == True:
      #       directories.append(f)
      #     # print( f )
      #     # print(v)
      #     # print(os.path.isfile(v))
      #     # print(os.path.isdir(v))
      # # print(files)
      # # print(directories)
      # print(os.listdir( path )[1:])

    ## Student need to fill in the rest of the method
    ## to accomplish the task specified in the lab description


## end of list_dir()


basedir = input('Enter a starting directory or file: ')

# Call list_dir which lists directories and files recursively
# The argument is the starting file(dir)
list_dir( basedir )

## end of program


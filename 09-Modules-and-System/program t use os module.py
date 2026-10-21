# program to sue getcwd mkdir and chdir

import os
#print current working directory
print('current directory', os.getcwd())

#create a new directory
os.mkdir("br_dir")

#change current working directory
os.chdir("br_dir")

#print current working directory
print("current directory now: ",os.getcwd())

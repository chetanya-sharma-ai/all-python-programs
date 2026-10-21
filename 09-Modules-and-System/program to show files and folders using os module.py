#program to show files and folders

import os
files=os.listdir()
print('files and folders')
for f in files:
    print(f)

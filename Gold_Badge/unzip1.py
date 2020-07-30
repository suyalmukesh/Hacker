import os
from zipfile import ZipFile
import subprocess, sys

source = 'C:\\Users\\C58365A\\Desktop\\unzipping\\debug.zipx'
target = 'C:\\Users\\C58365A\\Desktop\\unzipping'
print ("Welcome to Unzipping")
##############  Notes  ####################
# 1 : Small file without password
# 2 : Big file without password
# 3 : Small file with password
# 4 : Big file with password
# 5 : File with directory structure

def unzip_without_password(input_file,output_folder):
        print ("Subroutine :: unzip_without_password")
        try:
            with ZipFile(input_file, 'r') as zipObj:
                # Extract all the contents of zip file in different directory
                zipObj.extractall(output_folder)
        except:
            print("An exception occurred extracting with Python ZipFile library.")
            print("Attempting to extract using 7zip")
            subprocess.Popen(["7z", "e", f"{input_file}", f"-o{output_folder}", "-y"])

unzip_without_password(source,target)
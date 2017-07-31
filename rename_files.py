import os

files = os.listdir(r"C:\Users\Guilherme\Downloads\prank")

print (files)

os.chdir(r"C:\Users\Guilherme\Downloads\prank")

for file_name in files:
    os.rename(file_name, file_name.translate(None, "0123456789"))

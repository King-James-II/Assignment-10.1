import os
directory = input("In what directory do you wish to save your file?\n c:/")
file_path = f"/{directory}"
file_name = input("File name: ")
exists = os.path.exists(file_path)
if exists == False:
    os.makedirs(file_path)
else:
    pass

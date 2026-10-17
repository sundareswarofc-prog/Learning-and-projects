import os

#### for removing a file we need to import os #######

# os.remove("new_file.txt")

#### before that we need to check if the file exist or not ##############

if os.path.exists("new_file.text"):
    os.remove("new_file.text")
else:
    print("File didn't exist")


############### to delete a entire folder #################

os.rmdir("myfolder")
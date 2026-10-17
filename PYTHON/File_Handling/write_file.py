############## to append some thing on the existing file use "a" if the file not exist it will create one #########################

with open("UNANSWERED.txt", "a") as f:
    f.write("now the file has more content")

f=open("UNANSWERED.txt")
print(f.read())
f.close()

############## to remove the existing content and add a new one use "w" #####################

with open("delete.txt", "w") as f:
    f.write("now the file has more content")

f=open("delete.txt")
print(f.read())
f.close()


############ to create a new file use "x" ##########################

with open ("new_file.txt","x") as f:
    f.write("new file!")

f=open("new_file.text","a")
f.write("\nanother line added")


# Mode	File doesn’t exist	    File already exists
# "w"	  Creates it	            Erases it and writes from scratch
# "a"	  Creates it	            Adds to the end
# "x"	  Creates it	            Raises FileExistsError



########## the open takes two arguments file name and mode(read,write) ############
############ when you open a file you have to close the file using close() ####################

f=open("UNANSWERED.txt")
p=open("../UNANSWERED.txt")
f.close()
# print(p.read())
# print(f.read())


############ we can use "with" keyword to close the file automatically instead of manually close the file ############ 

with open ("UNANSWERED.txt") as f:
    print(f.read())
# print(f.read())


##### we can also specify the number of words to return
 
with open("UNANSWERED.txt") as f:
    print(f.readline(),"------- read the first line")
    print(f.read(5),"------- read the first 5 chars")

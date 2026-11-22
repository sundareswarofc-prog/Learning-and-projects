# text = "Python is easy to learn and useful for backend development"

# print(len(text))

# chunk_size = 30
# overlap = 10

# chunks = []

# for i in range(0, len(text), chunk_size - overlap):
#     chunk = text[i:i + chunk_size]
#     chunks.append(chunk)

# for part in chunks:
#     print(part)
#     print("----------")


########## practice task 

text=""

with open(".././python_notes.txt","r",encoding="utf-8") as f:
         text+=f.read()

chunk_size=50
overlap=10

chunks=[]

for i in range(0,len(text),chunk_size-overlap):
        chunk=text[i:i+chunk_size]
        print(chunk,i)
        chunks.append(chunk)
    


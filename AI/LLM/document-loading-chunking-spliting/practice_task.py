text=""

with open("./python_notes.txt","r",encoding="utf-8") as f:
    text=f.read()

print(text)

chunk_size=50

chunk=[text[i:i+chunk_size] for i in range(0,len(text),chunk_size)]                             

for text in chunk:                                                  
    print(text)
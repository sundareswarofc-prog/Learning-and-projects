import os
from pypdf import PdfReader


folder_path="./documents"

documents=[]

for file_name in os.listdir(folder_path):
     if file_name.endswith(".pdf"):
          file_path = os.path.join(folder_path,file_name)
          reader=PdfReader(file_path)
          text=""
          for file in reader.pages:
               text+= (file.extract_text() or "") + "\n"

          documents.append(
               {
                    "title":file_name,
                    "content":text
               }
          )
          
          
          
all_chunks=[]

chunk_size=500
overlap=100

for items in documents:
    text=items["content"]
    
    for i in range(0,len(text),chunk_size-overlap):
        chunk=text[i:i+chunk_size]
        
        if chunk.strip():
             all_chunks.append({
                "text": chunk,
                "source": items["title"]
            })
             
    

          


         
import pandas as pd 
import os

def FileLoading(filepath):
    
    docs_list = os.listdir(filepath)
    txt_list = [file for file in docs_list if file.endswith('.txt')]
    docs_dict = {}
    for txt in txt_list:
        docs = open(filepath+os.sep+txt, "r", encoding="utf-8").read()
        docs_dict[txt] = docs
    return(docs_dict)


def chunks(text,chunk_size,overlap):
    position = 0
    dict_text = {}
    while position  <len(text) :
        end = min(position + chunk_size, len(text))
        dict_text[f"{position}-{end}"] = text[position  : end]
        position +=  chunk_size-overlap

    return dict_text, len(text)


text = FileLoading(r"C:\Users\lonel\Desktop\PERSO\TRAIN\RAG\docs")
print(chunks(text['Nouveau Document texte.txt'],512,50))
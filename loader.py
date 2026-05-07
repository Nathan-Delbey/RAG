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





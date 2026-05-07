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
    text_title = text[0]
    text = text[1]
    position = 0
    chunk_list = []
    while position  <len(text) :
        end = min(position + chunk_size, len(text))
        chunk_list.append({
            "source": text_title,
            "position": f"{position}-{end}",
            "text": text[position : end]
        })
        position +=  chunk_size-overlap

    return chunk_list

if __name__ == "__main__" : 
    docs = FileLoading("docs")
    data_base = []
    for text in docs.items():
        result = chunks(text,512,50)
        data_base.extend(result)
    print(result)

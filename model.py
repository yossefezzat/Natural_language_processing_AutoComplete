import os as os
import nltk as nltk
from collections import defaultdict

def read_Folder_data(folder_name):
    folder_files = os.listdir(folder_name)
    all_files = "" 
    for file in folder_files:
        file = open("International news//" + file , "r" , encoding="utf8").read()
        all_files += file +"\n"
    return all_files

    
def read_file_data(file):
    file = open( file , "r" , encoding="utf8")
    data = file.read()
    file.close()
    return data

def tokenize_words(data):
    data_tokenized = nltk.word_tokenize(data)
    return data_tokenized

def make_trigram(data_tokenized):
    trigram_list = []
    for i in range(len(data_tokenized)-2) :
        trigram_list.append((data_tokenized[i] ,data_tokenized[i+1], data_tokenized[i+2]))
    return trigram_list

def build_model(data_tokenized):
    trigram_data = make_trigram(data_tokenized)
    model = defaultdict(lambda: defaultdict(lambda: 0))
    for words in list(trigram_data):
        w1, w2, w3 = words
        model[(w1,w2)][w3]+=1

    total_count = 0 
    for w1_w2 in model:
        total_count = float(sum(model[w1_w2].values()))
        for w3 in model[w1_w2]:
            model[w1_w2][w3] /= total_count 
    return model


data = read_file_data("international_news.txt")
tokens = tokenize_words(data)
model = build_model(tokens)

text = "يحذر في الوقت ذاته من الاستخدام المفرط للقوة"
text = text.split()

print(model[tuple(text[-2:])].keys() , model[tuple(text[-2:])].values())

    
    
    
    
    
    
    
    
    
    
    
    
    
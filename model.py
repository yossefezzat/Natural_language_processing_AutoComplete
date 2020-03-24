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
    for st_nd_word in model:
        total_count = float(sum(model[st_nd_word].values()))
        for rd_word in model[st_nd_word]:
            model[st_nd_word][rd_word] /= total_count 
    return model


def run_model(data_file):
    data = read_file_data(data_file)
    tokens = tokenize_words(data)
    model = build_model(tokens)
    return model


def sorting_result(model, text):
    model = sorted(model[tuple(text[-2:])].items(), key = lambda kv:(kv[1], kv[0]),reverse=True)
    return model


def get_top_10(model_sorted_result):
    print(len(model_sorted_result) )
    output_size = 10 if len(model_sorted_result)>10  else len(model_sorted_result)
    for i in range(output_size):
        print(model_sorted_result[i][0] , "    " , round(model_sorted_result[i][1],6))
    if output_size == 0: 
        print("لا توجد اقتراحات")

model = run_model("international_news.txt")
text =  input("Enter your Input : ")
text = text.split()
model = sorting_result(model , text)
get_top_10(model)

#" يحذر في الوقت ذاته من الاستخدام المفرط للقوة في العراق وقال"
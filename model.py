import nltk as nltk
from collections import Counter, defaultdict
import os as os


# Create a placeholder for model
model = defaultdict(lambda: defaultdict(lambda: 0))
'''
folder_files = os.listdir("International news")
all_files = "" 

for file in folder_files:
    file = open("International news//" + file , "r" , encoding="utf8").read()
    all_files += file +"\n"
   
f = open('data_international.txt' , 'w' ,  encoding="utf8")
f.write(all_files)
f.close()

'''

file = open("international_news.txt" , "r" , encoding="utf8")
data = file.read()
file.close()
data_tokenized = nltk.word_tokenize(data)

trigram_data = nltk.trigrams(data_tokenized)
#print(list(trigram_data)[-1:])


for words in list(trigram_data):
    w1, w2, w3 = words
    model[(w1,w2)][w3]+=1

count = 0 
for w1_w2 in model:
    total_count = float(sum(model[w1_w2].values()))
    for w3 in model[w1_w2]:
        model[w1_w2][w3] /= total_count 
           
           

        
    

#print(model[tuple("غربية" ,"دول")].keys())
    
  
    
text = "يحذر في الوقت ذاته من الاستخدام المفرط للقوة"
text = text.split()

print(model[tuple(text[-2:])].keys())

'''
sentence_finished = False
 
while not sentence_finished:
  # select a random probability threshold  
  r = 0.6
  accumulator = .0
  for word in model[tuple(text[-2:])].keys():
      accumulator += model[tuple(text[-2:])][word]
      # select words that are above the probability threshold
      if accumulator >= r:
          text.append(word)
          break

  if text[-2:] == [None, None]:
      sentence_finished = True
 
print (' '.join([t for t in text if t]))
'''

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

'''
String_trigram = trigrams(file.split())

for grams in String_trigram:
    print (grams)



for gram in String_trigram:
    print(nltk.probability.FreqDist())
'''
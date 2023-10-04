#Assignment no:-02
# Name:-Prajakta Sambhaji KOlse
# Subject:-NLP
# Roll no:-34 , Batch:-B2
# Title:- Bag Of Word
# Import Library
import gensim
from gensim import corpora

text1 = ["""Gensim is a free open-source Python library for representing documents as semantic vectors,
           as efficiently and painlessly as possible. Gensim is designed 
           to process raw, unstructured digital texts using unsupervised machine learning algorithms."""]

tokens1 = [[item for item in line.split()] for line in text1]
g_dict1 = corpora.Dictionary(tokens1)

#print("The dictionary has: " +str(len(g_dict1)) + " tokens\n")
#print(g_dict1.token2id)
g_bow =[g_dict1.doc2bow(token, allow_update = True) for token in tokens1]
print("Bag of Words : ", g_bow)



#Title : TF-IDF
text = ["The food is excellent but the service can be better",
        "The food is always delicious and loved the service",
        "The food was mediocre and the service was terrible"]

g_dict = corpora.Dictionary([simple_preprocess(line) for line in text])
g_bow = [g_dict.doc2bow(simple_preprocess(line)) for line in text]

print("Dictionary : ")
for item in g_bow:
    print([[g_dict[id], freq] for id, freq in item])

g_tfidf = models.TfidfModel(g_bow, smartirs='ntc')

print("TF-IDF Vector:")
for item in g_tfidf[g_bow]:
    print([[g_dict[id], np.around(freq, decimals=2)] for id, freq in item])


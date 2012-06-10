# generate a pickled multi-dimensional list of the distribution of topics for each document

from gensim import corpora, models, similarities

import os
import logging
import time
import cPickle as pickle

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#re-load
dictionary = corpora.Dictionary.load('xx.dict')

#get corpus from disk
corpus = corpora.MmCorpus("corpus.mm")

print "TOPICS"

modelLDA=models.ldamodel.LdaModel.load('LDAxx.lda')
modelLDA.print_topics(topics=20,topn=10)

#generate the topic distribution for documents in  the corpus
matrixOfTopicDistr=modelLDA[corpus]

topicDistMultiList=[]

index=0

for oneDoc in matrixOfTopicDistr:
    topicDistMultiList.append(oneDoc)
    index += 1

print "total len", index

print "len list", len(topicDistMultiList)

outputMultiList=open('topicDistrMultiList.pkl','wb')
pickle.dump(topicDistMultiList,outputMultiList)
outputMultiList.close()


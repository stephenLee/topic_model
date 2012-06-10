## Pan/Schmaltz
## November 25, 2011; for CS 205
## topicStats.py (V.2011-11-25)

##This is for the online LDA model results.
#This generates the topics (which can be saved from the console from the logging output)
# and generates a pickled multi-dimensional list of the distribution of topics for each document.

from gensim import corpora, models, similarities

import os
import logging
import time
import cPickle as pickle


#logging is necessary to view the topics on the console--see the gensim source code
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


#re-load
dictionary = corpora.Dictionary.load('sample50Kdict.dict')


#get corpus from disk (this returns an iterator):
corpus = corpora.MmCorpus("corpus.mm")

print "TOPICS"

modelLDA = models.ldamodel.LdaModel.load('LDA50K.lda')

modelLDA.print_topics(topics=50, topn=20)


#generate the topic distributions for documents in the corpus
matrixOfTopicDistr = modelLDA[corpus]

topicDistrMultiList = []

index = 0
for oneDoc in matrixOfTopicDistr:
    topicDistrMultiList.append(oneDoc)
    #print one
    index += 1
    #if index > 30:
    #    break

print "total len", index

print "len list", len(topicDistrMultiList)

#print "list", topicDistrMultiList

#save topicDistrMultiList
outputMultiList = open('topicDistrMultiList.pkl', 'wb')
pickle.dump(topicDistrMultiList, outputMultiList)
outputMultiList.close()

print "save check 1"

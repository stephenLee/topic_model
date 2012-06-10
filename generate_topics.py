#generate topics using LDA algorithm

from gensim import corpora, models, similarities

import os
import logging
import time

SEGSTOP_FOLDERNAME="seg_stop"

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class PreProcessedCorpus(object):
    def __init__(self, allFileNamesList):
        self.allFileNamesList=allFileNamesList
    def __iter__(self):
        for oneFileName in self.allFileNamesList:
            oneDocumentList=[]
            for line in open(SEGSTOP_FOLDERNAME+"/"+oneFileName, 'r'):
                oneLineSplit = line.split()
                if len(oneLineSplit) > 0:
                    oneDocumentList = oneDocumentList + oneLineSplit
            yield dictionary.doc2bow(oneDocumentList)

startTime=time.time()

fullPathName=os.path.join(os.getcwd(), SEGSTOP_FOLDERNAME)
allFileNamesList=[]
for root, dirs, files in os.walk(fullPathName):
    for oneFileName in files:
        allFileNamesList.append(oneFileName)
        
indexCounter=0
dictionary=None
for oneFileName in allFileNamesList:
    oneDocumentList=[]
    for line in open(SEGSTOP_FOLDERNAME+"/"+oneFileName,'r'):
        oneLineSplit=line.split()
        if len(oneLineSplit) > 0:
            oneDocumentList = oneDocumentList+oneLineSplit
    if indexCounter==0:
        dictionary=corpora.Dictionary([oneDocumentList])
        indexCounter += 1
    else:
        dictionary.add_documents([oneDocumentList])

dictionary.compactify()

#save dictionary
dictionary.save('xx.dict')
dictionary = corpora.Dictionary.load('xx.dict')

lazyCorpus = PreProcessedCorpus(allFileNamesList)

#store to disk, using market matrix format
corpora.MmCorpus.serialize("corpus.mm", lazyCorpus)

# get corpus from disk
corpus = corpora.MmCorpus("corpus.mm")

#use online LDA:
modelLDA=models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=10)

#save model:
modelLDA.save('LDAxx.lda')

print "TOPICS"

modelLDA.print_topics(10)
completeElapsedTime=time.time() - startTime
print "Total Elapsed time: ", completeElapsedTime

output=open("topicTotalTime.txt", 'w')
output.write(str(completeElapsedTime))
output.close()


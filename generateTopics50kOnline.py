## Pan/Schmaltz
## November 24, 2011; for CS 205
## generateTopics50kOnline.py (V.2011-11-24)

##Generates topics using the online/streaming LDA algorithm

from gensim import corpora, models, similarities

import os
import logging
import time

#note: this only test part of allfileslist

#SEGSTOP_FOLDERNAME = "SegStopFiles1"

#SEGSTOP_FOLDERNAME = "testSegStop"

#SEGSTOP_FOLDERNAME = "SegStopFiles1sample1st5000"

SEGSTOP_FOLDERNAME = "SegStopFiles50kSample"

#ENGLISH TEST:

#SEGSTOP_FOLDERNAME = "EnglishTest"



logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)



#to generate the corpus, open each file and save the tokens in one list
class PreProcessedCorpus(object):
    def __init__(self, allFileNamesList):
        self.allFileNamesList = allFileNamesList
    def __iter__(self):                
        for oneFileName in self.allFileNamesList:
            oneDocumentList = []
            for oneLine in open(SEGSTOP_FOLDERNAME+"/"+oneFileName, 'r'):
                oneLineSplit = oneLine.split()
                if len(oneLineSplit) > 0:
                    oneDocumentList = oneDocumentList + oneLineSplit
            yield dictionary.doc2bow(oneDocumentList)


startTime = time.time()


fullPathName = os.path.join(os.getcwd(), SEGSTOP_FOLDERNAME)


#fileListCounterIndex = 0  #for testing

#get list of all pre-processed files:
allFileNamesList = []
for root, dirs, files in os.walk(fullPathName):
    for oneFileName in files:
        allFileNamesList.append(oneFileName)
        #if fileListCounterIndex > 1000:  #for testing
        #    break
        #fileListCounterIndex += 1

#FOR TESTING:
#allFileNamesList = allFileNamesList[0:20000]




#use lazy instantiation for dictionary:
# get token stats:

indexCounter = 0
dictionary = None
for oneFileName in allFileNamesList:
    #print "filename: ", oneFileName
    oneDocumentList = []
    for oneLine in open(SEGSTOP_FOLDERNAME+"/"+oneFileName, 'r'):
        oneLineSplit = oneLine.split()
        if len(oneLineSplit) > 0:
            oneDocumentList = oneDocumentList + oneLineSplit
    #print "oneDocumentList: ", oneDocumentList
    if indexCounter == 0:  #init dictionary
        dictionary = corpora.Dictionary([oneDocumentList])
        indexCounter += 1
    else: #add remainder to dictionary
        dictionary.add_documents([oneDocumentList])


 
#print dictionary.token2id
# OPTIONAL: get rid of words with frequency == 1
#singletonWordList = [oneWordID for oneWordID, thisWordFrequency in dictionary.dfs.iteritems() if thisWordFrequency == 1]
#dictionary.filter_tokens(singletonWordList) 
dictionary.compactify() 
#print dictionary

#print dictionary.token2id


#save dictionary:
dictionary.save('sample50Kdict.dict')

#go ahead and re-load here, re-writing var, to ensure have iterator
dictionary = corpora.Dictionary.load('sample50Kdict.dict')


#use lazy instantiation for corpus:
lazyCorpus = PreProcessedCorpus(allFileNamesList)

#for oneVector in lazyCorpus:
#    print oneVector

#save corpus to disk using Matrix Market format:
corpora.MmCorpus.serialize("corpus.mm", lazyCorpus)

#get corpus from disk (this returns an iterator):
corpus = corpora.MmCorpus("corpus.mm")

#LDA (uses "batch" mode--much slower--see the source code):
#modelLDA = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=50, update_every=0, passes=20)


#use online LDA:
modelLDA = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=50)

#save model:
modelLDA.save('LDA50K.lda') 

#to subsequently load:
#modelLDA = models.ldamodel.LdaModel.load('LDA50K.lda')

print "TOPICS"

modelLDA.print_topics(10)
#print [one for one in modelLDA[corpus]]



completeElapsedTime = time.time() - startTime
print "Total Elapsed Time (including a variety of disk activity): ", completeElapsedTime

output = open("topicTotalTime.txt", 'w')
output.write(str(completeElapsedTime))
output.close()



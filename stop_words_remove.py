# remove stop words, remove English letters and numbers
import os
import string
import codecs
import time

#Folder from which to read the input:
SEGFILES_FOLDERNAME = "seg_corpus"
#Folder in which to save the ouput:
SEGSTOP_FOLDERNAME="seg_stop"

STOPWORD_FILENAME="stopwords.txt"

fullPathName=os.path.join(os.getcwd(), SEGFILES_FOLDERNAME)

StopWordsDictionary={}
for line in open(STOPWORD_FILENAME, 'r'):
    if line.strip() not in string.whitespace:
        StopWordsDictionary[line.strip().split()[0]]=1

for symbol in string.printable:
    if symbol not in string.whitespace:
        StopWordsDictionary[symbol]=1

startTime=time.time()
progressCounter=0
for root, dirs, files in os.walk(fullPathName):
    for oneFileName in files:
        finalStringToSave=""
        for line in open(SEGFILES_FOLDERNAME+"/"+oneFileName, 'r'):
            for oneWordToken in line.split():
                if oneWordToken not in StopWordsDictionary:
                    includeCounter=0
                    for oneChar in oneWordToken:
                        if oneChar in string.printable:
                            includeCounter += 1
                            break
                    if includeCounter==0:
                        finalStringToSave += oneWordToken+" "
            finalStringToSave += "\n"
        output=open(SEGSTOP_FOLDERNAME+"/"+oneFileName, 'w')
        output.write(finalStringToSave)
        output.close()

        progressCounter += 1
        if progressCounter%1000 == 0:
            print "Progress: Processed files=", progressCounter

completeElapsedTime=time.time() - startTime
print "Total Elapsed time: ", completeElapsedTime
        



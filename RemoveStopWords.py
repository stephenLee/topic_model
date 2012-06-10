## Pan/Schmaltz
## November 12, 2011; for CS 205
## RemoveStopWords.py (V.2011-11-12)
## This version also removes English letters and numbers (from string.printable)
## Note that the final output characters are separated by the
## default space character " ".

import os
import string
import codecs
import time

#folder from which to read the input:
#SEGFILES_FOLDERNAME = "SegFiles1"
SEGFILES_FOLDERNAME = "SegFiles50kSample"

#folder in which to save the output:
#SEGSTOP_FOLDERNAME = "SegStopFiles1"
SEGSTOP_FOLDERNAME = "SegStopFiles50kSample"

STOPWORD_FILENAME = "stopwords2.txt"


fullPathName = os.path.join(os.getcwd(), SEGFILES_FOLDERNAME)

#print fullPathName

##read stop words file and save to dictionary
StopWordsDictionary = {}
for fullLine in open(STOPWORD_FILENAME, 'r'):
    if fullLine.strip() not in string.whitespace:
        StopWordsDictionary[fullLine.strip().split()[0]] = 1

##also add English letters/numbers/etc. in string.printable
for symbol in string.printable:
    if symbol not in string.whitespace:
        StopWordsDictionary[symbol] = 1

##also add additional stopwords:
#for fullLine in codecs.open(STOPWORD_FILENAME2, mode='r', encoding='gb2312', errors='strict'):
#    if fullLine.strip() not in string.whitespace:
#        oneCharGroup = fullLine.strip().split()[0]
#        encodeCharGroup = oneCharGroup.encode('utf_8')
#        StopWordsDictionary[encodeCharGroup] = 1

startTime = time.time()
progressCounter = 0
for root, dirs, files in os.walk(fullPathName):
    for oneFileName in files:  #use files[0:2] for testing
        finalStringToSave = ""
        for fullLine in open(SEGFILES_FOLDERNAME+"/"+oneFileName, 'r'):
            #print "fullLine is: ", fullLine
            for oneWordToken in fullLine.split():
                if oneWordToken not in StopWordsDictionary:
                    #also get rid of English letters/numbers:
                    includeCounter = 0
                    for oneChar in oneWordToken:
                        if oneChar in string.printable:
                            includeCounter += 1
                            break
                    if includeCounter == 0:
                        finalStringToSave += oneWordToken + " "
            finalStringToSave += "\n "
        #print "finalStringToSave is: ", finalStringToSave
        output = open(SEGSTOP_FOLDERNAME+"/"+oneFileName+".txt", 'w')
        output.write(finalStringToSave)
        output.close()
        
        progressCounter += 1
        if progressCounter%1000 == 0:
            print "Progress: Processed files = ", progressCounter

completeElapsedTime = time.time() - startTime
print "Total Elapsed Time (including a variety of disk activity): ", completeElapsedTime

print "save check1"

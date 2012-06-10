## Pan/Schmaltz
## November 3, 2011; for CS 205
## SegmenterSerial.py (V.2011-11-03)

### This script goes through sample of 50k files serially
### and finds the whitespaces between words.
### Saves new files beginning with "seg_"
### NOTE: PLEASE UPDATE THE PATH, THEY ARE ABSOLUTE NOT RELATIVE

import time
import os
import string

# Import pymmseg if script in pymmseg-cpp folder (pymmseg DEPENDENCY)
# Otherwise, use:
#from pymmseg import mmseg
import mmseg
mmseg.dict_load_defaults()

# Path to files that need to be segmented (UPDATE PATH)
maindir = "/home/jpan/CS205/segment/Original50kSample/"

# Path to where teh segmented files need to go (UPDATE PATH)
newdir = "/home/jpan/CS205/segment/SegFiles50kSample/"
os.chdir(newdir)

# Segment the text (timed)
start_time = time.time()
for f in os.listdir(maindir):
    print "starting file: " + f
    filename = "seg_" + f[:]
    path = os.path.join(maindir,f)
    file = open(path)
    txt = file.read()
    algor = mmseg.Algorithm(txt)
    words = []
    for tok in algor:
        print '%s [%d..%d]' % (tok.text, tok.start, tok.end)
        words.append(tok.text)
    words_str = string.join(words,' ')
    output = open(filename,'w')
    output.write('%s' % (words_str))
    output.close()
end_time = time.time()

# Save total time (UPDATE PATH)
total_time = end_time - start_time
enddir = "/home/jpan/CS205/segment/"
os.chdir(enddir)

tout = open("segtime_50k.txt", "w")
tout.write("total time: %f sec" %total_time)
tout.close() 

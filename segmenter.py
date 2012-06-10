## segment Chinese Words of tweets using pymmseg-cpp
import time
import os
import string

import mmseg
mmseg.dict_load_defaults()

# Path to files that need to be segmented
maindir = "/home/lxd/Study/SNA/weibo/topic_model/corpus"

# Path to where segmented files need to go
newdir = "/home/lxd/Study/SNA/weibo/topic_model/seg_corpus"
os.chdir(newdir)

start_time=time.time()
for f in os.listdir(maindir):
    print "Startingfile:" + f
    filename="seg_"+f[:]
    path=os.path.join(maindir,f)
    file=open(path)
    text=file.read()
    algor=mmseg.Algorithm(text)
    words=[]
    for tok in algor:
        print '%s [%d..%d]' % (tok.text, tok.start, tok.end)
        words.append(tok.text)
    words_str=string.join(words,' ')
    output=open(filename,'w')
    output.write('%s' % (words_str))
    output.close()
end_time=time.time()

#total_time
total_time=end_time-start_time
enddir="/home/lxd/Study/SNA/weibo/topic_model"
os.chdir(enddir)

tout=open("segtime.txt", "w")
tout.write("total time: %f sec" %total_time)
tout.close()
    

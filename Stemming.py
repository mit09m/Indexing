#Program for scanning through the files in each subfolder and doing the necessary pre-processing
#like tokenization,stemming and removing special characters.

import os
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
def list_files(dir):                                                                                                  
    r = []                                                                                                            
    subdirs = [x[0] for x in os.walk(dir)]                                                                            
    for subdir in subdirs:                                                                                            
        files = os.walk(subdir).next()[2]                                                                             
        if (len(files) > 0):                                                                                          
            for file in files:                                                                                        
                r.append(subdir + "/" + file)                                                                         
    return r     
pth='/home/mit/Downloads/Infomation Retrieval/Assignment 2 indexing/20news-18828/alt.atheism'
fls=list_files(pth)
stop_words = set(stopwords.words('english'))
ps=PorterStemmer() 
cnt=0
dic={}
for fl in fls:
	f=open(fl)
	example_sent=""
	for wrd in f:
		example_sent+=wrd
	try:
		word_tokens = word_tokenize(example_sent)
	except:
		f.close()
		cnt+=1
		continue
	tem=[]
	for w in word_tokens:
		if ((w[0]>='a' and w[0]<='z') or (w[0]>='A' and w[0]<='Z')):
			tem.append(w.lower())
	word_tokens=tem
	filtered_sentence = []
	f.close()
	f=open(fl,"w") 
	for w in word_tokens:
	    if w not in stop_words:
	    	try:
	        	f.write(ps.stem(w)+" ")
	        except:
	        	continue
	f.close()
print 'cnt = '+str(cnt)

#Program for scanning through the pre-processed documents 
#and creating a posting list

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
pth='/home/aman/Stemming/20news-18828'
fls=list_files(pth)
cnt=0
dic={}
for fl in fls:
	f=open(fl,'r')
	cnt+=1
	tmp_dic={}
	words=[]
	for wrd in f:
		words=wrd.split()
	for wrd in words:
		if wrd in tmp_dic:
			tmp_dic[wrd]+=1
		else:
			tmp_dic[wrd]=1
	f.close()
	cur_file_name=(fl.split('/'))[-1k in tmp_dic.keys():

	


		if k in dic:
			dic[k].append((tmp_dic[k],cur_file_name))
		else:
			dic[k]=[]
			dic[k].append((tmp_dic[k],cur_file_name))
	if(cnt%1000==0):
		print cnt
f=open('/home/aman/Stemming/posting_list','w')
for k in dic.keys():
	st=''
	st+=k+'---->'
	st+=str(dic[k])
	f.write(st+'\n')

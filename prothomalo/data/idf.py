import os
import glob
import math
import operator
files=[]
        
input_path= "words/"
os.chdir(input_path)


for file_ in glob.glob("*"):
    files.append(file_)
    
os.chdir('..')

doc_count={}


for file_ in files:
	doc = open(input_path+file_).readlines()
	for line in doc:
		tokens = line.replace("\n","").split(",")
		key = tokens[0]
		value = int(tokens[1])
		if key not in doc_count.keys():
			doc_count[key] = 1
		else:
			doc_count[key] = doc_count[key]+1



out_file = open('idf.txt', 'w', encoding="utf-8")
idf={}
for key in doc_count.keys():
	idf_=math.log(len(files)/doc_count[key])
	idf[key]=idf_

sorted_idf= sorted(idf.items(), key=operator.itemgetter(1))	
for item in sorted_idf:
    		out_file.write(item[0]+","+str(item[1])+"\n")
out_file.close()

import os
import glob
import math
import operator
import numpy as np
files=[]
        
input_path= "words/"
os.chdir(input_path)


for file_ in glob.glob("*"):
    files.append(file_)
    
os.chdir('..')

idf_file = open('idf.txt').readlines()
idf = {}
for line in idf_file:
	tokens = line.replace("\n","").split(",")
	key = tokens[0]
	value = float(tokens[1])
	idf[key]=value	
	
trainset_file= open('trainset_tfidf_w2v.csv', 'w', encoding="utf-8")
w2v_file=open('w2v.csv').readlines()
w2v = {}
wc=0
for line in w2v_file:
	if len(line.split(' ')) == 302:
		word = line.split(' ')[0]
		vector=[]
		for item in line.split(' ')[1:len(line.split(' '))-1]:
			vector.append(float(item))
		w2v[word]=vector
		wc=wc+1

for file_ in files:
	category = 0
	if 'bangladesh' in file_:
		category = 0
	if 'international' in file_:
		category = 1
	if 'economy' in file_:
		category = 2
	if 'entertainment' in file_:
		category = 3
	if 'sports' in file_:
		category = 4
	vector=[0.0 for i in range(300)]
	vector=np.asarray(vector)
	freq_file = open(input_path+file_).readlines()
	freq_count = {}
	total_freq = 0
	for line in freq_file:
		tokens = line.replace("\n","").split(",")
		key = tokens[0]
		value = int(tokens[1])
		if key not in freq_count.keys():
			freq_count[key] = value
		else:
			freq_count[key] = freq_count[key]+value
		total_freq = total_freq + value
	
	for line in freq_file:
		tokens = line.replace("\n","").split(",")
		key = tokens[0]
		value = int(tokens[1])
		if key not in w2v.keys():
			continue
		else:
			vector=vector+np.asarray(w2v[key])*idf[key]*freq_count[key]/total_freq
	trainset_file.write(str(category))
	for item in vector:	
		trainset_file.write(',')
		trainset_file.write(str(item))
	trainset_file.write('\n')
		

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

idf_file = open('idf.txt').readlines()
idf = {}
for line in idf_file:
	tokens = line.replace("\n","").split(",")
	key = tokens[0]
	value = float(tokens[1])
	idf[key]=value	


feature_count = 3000
features_file = open('featureVec.txt').readlines()
features = []

for i in range(feature_count):
	features.append(features_file[i].split(",")[0])

trainset_file= open('trainset.csv', 'w', encoding="utf-8")

for file_ in files:
	print(file_)
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
	featureVec = []
	for feature in features:
		if feature in freq_count.keys():	
			featureVec.append(idf[feature]*freq_count[feature]/total_freq)
		else:
			featureVec.append(0.0)
	trainset_file.write(str(category))
	for item in featureVec:
		trainset_file.write(',')
		trainset_file.write(str(item))
	trainset_file.write('\n')
trainset_file.close()

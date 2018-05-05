import requests as req
import glob
import os

def get_article_id(url):
    tokens = url.split('/')
    return tokens[len(tokens)-1]

files = []

for file_ in glob.glob("unique*.csv"):
    files.append(file_)
    
print(files)

fileMode = "w"
directory= "pages/"
if not os.path.exists(directory):
        os.makedirs(directory)
for file_ in files:
	count = 0
	article_type = file_.replace('unique_','').replace('.csv','')
	csv_file = open(file_).readlines()
	for link in csv_file:
		count = count + 1
		resp = req.get(link)
		page = resp.text
		article_id = get_article_id(link)
		out_file = open(directory + article_type + '_' +article_id + "_.txt", fileMode, encoding="utf-8")
		out_file.write(page)
		out_file.close()
		print('File:: '+file_+': '+str(count)+'/'+str(len(csv_file))+' links processed.')



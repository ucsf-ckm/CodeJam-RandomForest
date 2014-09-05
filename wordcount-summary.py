import sys, string, os
import csv as csv
from math import *
import operator
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
import re

# ignore stop words
stop_words = ["a", "able","about","across","after","all","almost","also","am","among","an","and","any",
"are","as","at","be","because","been","but","by","can","cannot","could","dear","did","do","does","either", 
"else", "ever","every","for","from","get","got","had","has","have","he","her","hers","him","his","how",
"however","i","if","in","into","is","it","its","just","least","let","like","likely","may","me","might",
"most","must","my","neither","no","nor","not","of","off","often","on","only","or","other","our","own",
"rather","said","say","says","she","should","since","so","some","than","that","the","their","them",
"then","there","these","they","this","tis","to","too","twas","us","wants","was","we","were","what","when",
"where","which","while","who","whom","why","will","with","would","yet","you","your"]

# ignore common words
common_words = ['text','page','gt', 'lt', 'code', 'pre', 'id', 'li','http', 'td', 'strong', 'amp', 'want', 
'width', 'ul', 'nofollow', 'tr', 'img', 'br', 'one', 'height', 'image', 'need', 'here', 'link','way','first',
'works','two']

term_iter = 0

# File containing categories (tags) to be assigned to records
tagTerms = "subjects.txt"

# File containing training data (id, title, text, tags)
trainDocs = "data.csv"

numTerms = 10

searchterm = "Middle-Aged"

print searchterm,

idtags = dict()

searchterm = searchterm.strip()

csv_file_object = csv.reader(open(trainDocs, "rb")) #Load in the training csv file

# get the most common terms for documents with this tag

wordcount = dict()
tagcommonwords = dict()

i = 0
j = 0

# build an index for each subject.  
# index contains each term in the records with this subject and the number of instances of that term.
for row in csv_file_object: 
	for t in row[3].strip().split():
		if searchterm in t:
			for w in re.findall(r"[0-9a-zA-Z#-]+", (row[2] + row[1])):
				if w.lower() not in stop_words and w.lower() not in common_words and (len(w) > 2):
					if w.lower() in wordcount: 
						wordcount[w.lower()] += 1
					else:
						wordcount[w.lower()] = 1

	
sortedwordcount = sorted(wordcount.iteritems(), key=operator.itemgetter(1), reverse=True)

for key,value in sortedwordcount:
    print key + ": " + str(value)




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

# File containing training data (id, title, text, tags)
trainDocs = "data.csv"

# File containing testing data (id, title, text)
# You can use the training doc if you want, tags will be ignored
testDocs = "data.csv"

numTerms = 10

for searchterm in ["Middle-Aged"]: 
	
	print searchterm
	
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
	
	ids = []
	rlists = []
	
	for row in csv_file_object: 
		
		ids.append(row[0])
		
		for t in row[3].strip().split():
			if searchterm in t:
				for w in re.findall(r"[0-9a-zA-Z#-]+", (row[2] + row[1])):
					if w.lower() not in stop_words and w.lower() not in common_words and (len(w) > 2):
						if w.lower() in wordcount: 
							wordcount[w.lower()] += 1
						else:
							wordcount[w.lower()] = 1

		
	sortedwordcount = sorted(wordcount.iteritems(), key=operator.itemgetter(1), reverse=True)

	i = 0

	rterms = []

	# limit the number of terms included in the random forest (to numTerms)
	for s in sortedwordcount:
		i = i + 1
		rterms.append(s[0])
		if i > numTerms:
			break
			
	print "rterms"
	print rterms
	print "*****"

	# print out the termnames 
	termnames = ""

	for r in rterms:
		termnames += r + ","

	termnames = termnames.rstrip(",")
	#print termnames

	# now that we have the numTerms most common terms, build a random forest based on the frequency count
	# of those words for each record that does or does not have that tag
	
	csv_file_object = csv.reader(open(trainDocs, "rb")) #Load in the training csv file

	wordcount = dict()
	tagcommonwords = dict()

	i = 0
	j = 0

	# keeping a balance of number of indicators, to make sure we have some of both (since many tags show up
	# for only a very small percentage of records, we don't want to have too sparse a forest)
	posindicators = 0
	negindicators = 0

	train_data = []	
	
	# add rows to random forest for this tag.  Each row consists of an indicator for whether the tag was present
	# followed by a frequency score for the X most common terms associated with that tag
	for row in csv_file_object: #Skip through each row in the csv file

		pos = 0
		neg = 0

		wordcount = dict()
		rlist = []

		if searchterm in row[3].split():
			rlist.append(1)
			pos = 1
		else:
			rlist.append(0)
			neg = 1
				
		for w in re.findall(r"[0-9a-zA-Z#-]+", (row[2] + row[1])):
			if w.lower() not in stop_words and w.lower() not in common_words and (len(w) > 2):
				if w.lower() in wordcount: 
					wordcount[w.lower()] += 1
				else:
					wordcount[w.lower()] = 1
		
		if len(wordcount) > 0:
	
			for r in rterms:
				
				if r in wordcount:
					rlist.append(wordcount[r])
				else:
					rlist.append(0)
			rlists.append(rlist)
		
		
	for i in range(len(rlist)):
		print ids[i] + " "
		print rlists[i]
		print rlists[i][0]
		for j in range(len(rlists[i])-1):
			print rterms[j] + " " + str(rlists[i][j+1])
		print


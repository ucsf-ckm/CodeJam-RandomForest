import os
from xml.dom.minidom import parse, parseString

#takes the data from data/erc/ and formats it in a csv that can be ingested into the RF app

subjectNames = set()

f_data = open("data.csv", "w")

for f in os.listdir("./data/erc"):
	
	f_data.write(f + ",")
	
	dom1 = parse('data/erc/' + f + '/mrt-datacite.xml')

	subjectlist = dom1.getElementsByTagName('subject')

	titlelist = dom1.getElementsByTagName('title')
	titles = []
	for t in titlelist:
		titles.append(t.childNodes[0].nodeValue.encode('ascii', 'ignore').replace("\"", ""))
	f_data.write("\"" + (' ').join(titles) + "\",")

	descriptionlist = dom1.getElementsByTagName('description')
	
	descriptions = []
	for d in descriptionlist:
		descriptions.append(d.childNodes[0].nodeValue.encode('ascii', 'ignore').replace("\"", "").replace('\n', ' '))
		
	f_data.write("\"" + (' ').join(descriptions).strip()  + "\",")
	
	subjects = []
	for s in subjectlist:
		subjectname = s.childNodes[0].nodeValue.encode('ascii', 'ignore').strip().replace(",","").replace(" ","-").replace("/", "-")
		subjectNames.add(subjectname)
		subjects.append(subjectname)
	f_data.write((' ').join(subjects).strip())
	f_data.write("\n")

f_data.close()
	
f_subjects = open("subjects.txt", "w")
for s in subjectNames:
	f_subjects.write(s + "\n")
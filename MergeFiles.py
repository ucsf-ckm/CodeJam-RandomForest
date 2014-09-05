import sys, string, os
import glob

file_list = glob.glob("./categories/*.txt")

i = 0
for inputfile in file_list:

	if i == 0:
		print inputfile
		i = i+1
		csv_file = open(inputfile)
		idtags = dict()

		for row in csv_file: 
			vals = row.strip().split(',')
			idtags[vals[0]] = []

		csv_file = open(inputfile)	

		for row in csv_file: 
			vals = row.strip().split(',')
			if len(vals[1]) > 0:
				idtags[vals[0]].append(vals[1].replace("\"", ""))
			
	else:

		csv_file = open(inputfile)	
		print inputfile


		for row in csv_file: 
			vals = row.strip().split(',')
			vals[1] = vals[1].replace("\"", "")
			if len(vals[1]) > 1:
				idtags[vals[0]].append(vals[1])

f = open("Merged_Out.txt", "w")

for i in sorted(idtags):
	outstr = i + ",\""
	for t in idtags[i]:
		if t != "":
			outstr += t + " "
	outstr = outstr.strip()
	outstr += "\""
	f.write(outstr + "\n")
	
	


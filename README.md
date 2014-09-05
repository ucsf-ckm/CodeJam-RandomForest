CodeJam-RandomForest
===============================

This repository contains the scripts for different exercises in using a random forest to predict subject tags for datasets based on metadata stored in DataShare.  These samples were part of a CodeJam at the CDL conference in Oakland in August, 2014.

For a full write up, check out the blog post at https://blogs.library.ucsf.edu/ckm/2014/09/05/random-forests-and-datashare-at-the-cdl-code-jam/

Overview of contents

This set of python scripts uses data from the UCSF DataShare site (http://datashare.ucsf.edu) to train a Random Forest to assign subjects based on title, description, and technical methods entered for each dataset.

The data directory contains raw files that would normally be indexed and displayed on the main datashare site.  The prepareData.py script takes this directory and creates a comma delimited file, data.csv, and a subjects list, subjects.txt, for easier parsing and ingestion into the random forest scripts.

Wordcount-summary.py demonstrates how to build a bag of words for all data sets containing the keyword tag "Middle-Aged"

Wodcounts-middle-aged.py displays the bag of words vector used to build and train a random forest for the keyword tag "Middle Aged" for each data set.

rForestDS-Middle-Aged.py creates and applies a random forest for a single keyword, "Middle-Aged".  The script prints parameters for the Random Forest to the command line, and creates an assignment of the keyword "Middle-Aged" to different records in the "categories" folder.  

rforestDS.py creates and applies a random forest for all subjects in datashare (as listed in subjects.txt).  This script prints parameters for the Random Forest for every keyword to the command line, and writes a separate file assigning keywords to records for every keyword tag to the "cagegories" folder.

MergeFiles.py will take all the different keyword assignments and merge them into a single file.  
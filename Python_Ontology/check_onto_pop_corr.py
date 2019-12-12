'''
	check_onto_pop_corr.py checks is used to check the correctness of of onto_pop.py for correct population of the ontology
	I've checked the correctness of onto_pop.py but would appreciate if someone validates it on the points below
	Points to check-
		1. No Entity Duplication
		2. Paragraphs corresponding a Question Type/Attribute is appended in the same Question Type of the Entity it corresponds to as given in the Excel sheet
		3. All paragraphs corresponding to an entity are appended to it
		4. If no paragraph corresponds to a Question Type it should be empty
		Remember, a paragraph can correspond to many entities and many Question Types
'''

import codecs, pickle

with codecs.open("ontology", "r", encoding="utf-8", errors="ignore") as f:
    ontology=pickle.load(f)

f=open("check_onto.txt", "w+")
for o in ontology.keys():
	f.write("\n")
	f.write(o)
	f.write("!!!!!!!!!!!!!!!!!!!!!!\n")
	for a in ontology[o].keys():
		f.write(a)
		f.write("------------------\n")
		for i in ontology[o][a]:
			f.write(i)
			f.write("\n")
from owlready2 import *
onto=get_ontology("file:///Users/adarshkumar/Downloads/ontologyedited.owl").load()
with onto:
	l=list(onto.classes())
	for i in l:
		class Definiton(i >> str):
			pass
		class Types(i >> str):
			pass
		class Effects(i >> str):
			pass
		class Examples(i >> str):
			pass
		class Applications(i >> str):
			pass
onto.save("/Users/adarshkumar/Downloads/ontologyedited.owl")
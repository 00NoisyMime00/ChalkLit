import Levenshtein as lev, codecs, pickle

with codecs.open("ontology", "r", encoding="utf-8", errors="ignore") as f:
    ontology=pickle.load(f) # Loads the Ontology

f=open("output_new.txt", "w+")

def extract_entities(question):
	f.write("\n%s\n" %question)
	question.replace("?", "")
	order=set()
	with open("entity_ex_help.txt", "r") as help:
		words=question.split()
		for lines in help:
			for w in words:	
				if lev.distance(lines.strip().lower(), w.lower())<2:
					order.add(lines.strip())		
	print(order)	
	entity=None
	max=(0, 10)				
	with open("all_distinct.txt", "r") as all:
		for lines in all:
			words=lines.strip().split()
			match=0
			for o in order:
				if o in words:
					match+=1
			if match>0:
				if match==max[0] and len(words)<max[1] or match>max[0]:
					max=(match, len(words))
					entity=lines.strip()
	print(entity)
	return entity

def all_retreive_answer(entity):
	f.write("Entity- %s\n" %entity)
	k=0
	for i in ontology[entity]["Definition"]:
		k+=1
		f.write("%2d. %s\n" %(k, i))

def one_retreive_answer(entity):
	f.write("Entity- %s\n" %entity)
	k=0
	for i in ontology[entity]["Definition"]:
		if k>0:
			break
		f.write("%s\n" %i)
		k+=1

while True:
    question=input("Enter your question: ").lower() # Wikifier returns different entity when in Caps and when not,
    entity=extract_entities(question)             #I've tried a few times and found that in lower gives better
    one_retreive_answer(entity)                       #(ie. if entity is present in the question asked then wouldn't 
                                                    # return that sometimes in Entity is in Caps) results
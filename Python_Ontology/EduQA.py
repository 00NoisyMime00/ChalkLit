'''
    Run files in the following order:
        ExcelPrePro.py -> onto_pop.py -> EduQA.py
    EduQA.py retreives the answer of a question asked by the User given the Question Type as we don't have the 
    inPhyNet Question classification model yet.
    The only conditon is that the entity in the question aked should be present in our ontology
    There is some latency of around a couple of seconds which is due to calling and retreiving the entity from 
    Wikifier, we need to find a way to get around this latency
'''

import json, requests, codecs, pickle
from fuzzywuzzy import fuzz

with codecs.open("ontology", "r", encoding="utf-8", errors="ignore") as f:
    ontology=pickle.load(f) # Loads the Ontology

f=open("output.txt", "w+")

def extract_entities(question):
    '''
        Returns the entities extracted in decreasing order of their Page Rank(PR)
    '''
    entities=[]
    url = 'http://www.wikifier.org/annotate-article?text='+question+'&lang=en&userKey=nwlceyfbsbhrpxugigjreraowemqad'
    
    try: # Requests Wikifier for entity extraction from "question" Note: The returned result also consists of entities which aren't showed if checked on Wikifier page directly also the PR is different  
        r = requests.get(url)
        r_json = r.json()
        for annotation in r_json['annotations']:
            title = annotation['title']
            url = annotation['url']
            pagerank = annotation['pageRank']
            entities.append((title, pagerank))
    except:
        print('Request to server for question {} failed!'.format(question))

    entities.sort(reverse=True, key = lambda x: x[1])
    return entities

def retreive_answer(entities):
    '''
        Writes to file the answer retreived given the entity
    '''
    for e in entities:
        f.write("\n%s %s\n" % (e[0],e[1]))
    entity=None
    for e in entities: 
        max=0  
        for o in ontology.keys(): # Should be optimized: lex sort -> check only with matching Alphabet, someone please optimize this
            Token_Sort_Ratio=fuzz.token_sort_ratio(e[0], o)
            if Token_Sort_Ratio>max: # To find the closest matching entity in our Ontology see 'https://www.datacamp.com/community/tutorials/fuzzy-string-python' for more info
                entity=o
                max=Token_Sort_Ratio
        if max>70: # 70- Hyper-parameter, I request everyone to play with this number and report the success rate of each number you tried so that we can pick the best one
            break
    f.write("Entity- %s\n" % entity)
    k=0
    for i in ontology[entity]["Definition"]: # "Definition" is selected arbitrary, feel free to change it to any other Question Type
        k+=1
        f.write("%2d. %s\n" %(k, i))

while True:
    question=input("Enter your question: ").lower() # Wikifier returns different entity when in Caps and when not,
    entities=extract_entities(question)             #I've tried a few times and found that in lower gives better
    retreive_answer(entities)                       #(ie. if entity is present in the question asked then wouldn't 
                                                    # return that sometimes in Entity is in Caps) results  
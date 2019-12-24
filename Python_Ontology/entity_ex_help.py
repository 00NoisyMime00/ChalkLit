entity_ex_help=open("entity_ex_help.txt","w")
lines_seen = set() 
for line in open("all_distinct.txt", "r"):
	words=line.split()
	print(words)
	for w in words:
		if w not in lines_seen:
			lines_seen.add(w)
			entity_ex_help.write(w)
			entity_ex_help.write("\n")
entity_ex_help.close()

import Levenshtein as lev
print(lev.ratio("push", "hush"))
print(lev.ratio("push", "puuh"))
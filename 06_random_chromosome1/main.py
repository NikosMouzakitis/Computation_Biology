import random
import time
import re

bases=['a','g','c','t']
seq_list=[]

for n in range(0,250000000):
	seq_list.append(random.choice(bases))
print("chromosome created")
chromosome="".join(seq_list)
#print(chromosome)
searchPattern='tataat'
start=time.time()
#search using reg.exp.
result=re.finditer(searchPattern, chromosome)

end=time.time()
countMatch=0

for m in result:
	countMatch+=1

print("Matches: ", countMatch)
print("Start: ",start,"seconds.\nEnd:    ",end,"seconds.")
print("Diff: ",end-start,"seconds to complete the search.")

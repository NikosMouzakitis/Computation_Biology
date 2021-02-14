import re	#for using regular expressions

restrictionEnzymes = {}
restrictionEnzymes['bamH1'] = ['ggatcc',0]
restrictionEnzymes['sma1'] = ['cccggg',2]
restrictionEnzymes['nci1'] = ['cc[cg]gg',2]
restrictionEnzymes['scrF1'] = ['cc[atcg]gg',2]
sequence1 = 'atatatccgggatatatcccggatatat'



#using from the package re(regular expressions)

print(re.findall(restrictionEnzymes['bamH1'][0],sequence1))
print(re.findall(restrictionEnzymes['nci1'][0],sequence1))
print(re.findall(restrictionEnzymes['scrF1'][0],sequence1))

sequence2 = 'cccccttgacaccccccccccccccccctataatccccc'
sequence3 = 'cccccttgacaccccccccccccccccccccctataatccccc'

promoter="ttgaca..tataat"	#dot,means it can be any of the characters(in our nucleod case any of(ATGC).
promoter2="ttgaca.{5,30}taat"#allows a variable lenght for the .,between five and twelve bases.
print("Finding '"+promoter2+"' in: "+sequence2)
print(re.findall(promoter2, sequence2))

print("Finding '"+promoter2+"' in: "+sequence3)
print(re.findall(promoter2, sequence3))



#using iterators

print(re.finditer(promoter2, sequence2))
matches = re.finditer(promoter2, sequence2)
print("using the Iterator")
print("Finding '"+promoter2+"' in: "+sequence2)

for m in matches:
	print(m.group())
	print(m.start(), m.end())
	print(sequence2[m.start()])
	print(sequence2[m.end()-1])
	print(sequence2[m.start():m.end()])

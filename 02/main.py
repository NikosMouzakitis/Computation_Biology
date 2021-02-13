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

promoter="agtc..taat"	#dot,means it can be any of the characters(in our nucleod case any of(ATGC).
promoter="agtc.{5,12}taat"#allows a variable lenght for the .,between five and twelve bases.


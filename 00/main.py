#return a list with the parts of the broken DNA sequence.
def chop_sequence(sequence, positions):
	ret=[]
	tmp=0
	for i in positions:
		ret.append(sequence[tmp:i])
		tmp = i
	ret.append(sequence[tmp:])	
	return	ret
#finds positions of the sequence,
#where the substring s exists.
def find_pos(sequence, s):
	ret=[]
	start=0
	while(True):
		p=sequence.find(s,start)

		if(p!=-1):	
			ret.append(p)
			start=p+1
		else:
			break
	
	return	ret
#dictionary holding all the restriction enjymes for this example.
restrictionEnjymes={}
#First element describes
#enjymes recognition site, while
#the second describe the relative position
#at which DNA is cutted.
restrictionEnjymes['bamH1']=['ggatcc',0]
restrictionEnjymes['sma1']=['cccggg',2]

print(restrictionEnjymes)
#it is a dictionary
print(type(restrictionEnjymes))
#print keys.
print(restrictionEnjymes.keys())
if 'sma1' in restrictionEnjymes:
	print("'sma1' is included in our enjymes dictionary")

dnaSequence='gctgtatttcgatcgatttatgct'
#return's the first occurance of the search sequence.
print(dnaSequence.find('ttt'))
#-1 when not finding anything
print(dnaSequence.find('tptt'))

searchFor='ttt'
#now in pos_list exist the positions in the dnaSequence
#where the searchFor string starts.
pos_list=find_pos(dnaSequence,searchFor)
print(pos_list)

print("Original example DNA sequence")
print(dnaSequence)
parts=chop_sequence(dnaSequence,pos_list)
print("After broken into parts:")
print(parts)

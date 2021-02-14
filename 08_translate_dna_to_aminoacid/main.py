dnaToProtein ={
	'ttt':'F','ttc':'F','tta':'L','ttg':'L',
	'tct':'S','tcc':'S','tca':'S','tcg':'S',
	'tat':'Y','tac':'Y','taa':'_','tag':'_',
	'tgt':'C','tgc':'C','tga':'_','tgg':'W',
	'ctt':'L','ctc':'L','cta':'L','ctg':'L',
	'cct':'P','ccc':'P','cca':'P','ccg':'P',
	'cat':'H','cac':'H','caa':'Q','cag':'Q',
	'cgt':'R','cgc':'R','cga':'R','cgg':'R',
	'att':'I','atc':'I','ata':'I','atg':'M',
	'act':'T','acc':'T','aca':'T','acg':'T',
	'aat':'N','aac':'N','aaa':'K','aag':'K',
	'agt':'S','agc':'S','aga':'R','agg':'R',
	'gtt':'V','gtc':'V','gta':'V','gtg':'V',
	'gct':'A','gcc':'A','gca':'A','gcg':'A',
	'gat':'D','gac':'D','gaa':'E','gag':'E',
	'ggt':'G','ggc':'G','gga':'G','ggg':'G'
	}

f=open("dna.txt","r")

lines=f.readlines()

data=""
for i in lines:
	data=data+str(i.strip())

data.replace("\n","")
data.replace("\r","")
f.close()
	

f=open("protein.txt","r")

lines=f.readlines()
data2=""
for i in lines:
	data2=data2+str(i.strip())
data2.replace("\n","")
data2.replace("\r","")

f.close()

data=data.lower()
print("DNA")
print(data)
data2=data2.lower()
print("TRANSLATED into protein")
print(data2)

peptide=[]

data=data[20:938]

for n in range(0,len(data),3):
	#stop if not on triplet.
	if( (n+2==len(data)-1) or (n+1==len(data)-1)):
		break	
	codon=data[n:n+3]
	peptide.append(dnaToProtein[codon])

peptideSequence="".join(peptide)	

print("Translated with our algorithm")
print(peptideSequence.lower())

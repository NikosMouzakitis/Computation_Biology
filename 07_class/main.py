import string

#used for translation of the RNA
rnaToProtein ={'uuu':'F','uuc':'F','uua':'L','uug':'L',
	'ucu':'S','ucc':'S','uca':'S','ucg':'S',
	'uau':'Y','uac':'Y','uaa':'STOP','uag':'STOP',
	'ugu':'C','ugc':'C','uga':'STOP','ugg':'W',
	'cuu':'L','cuc':'L','cua':'L','cug':'L',
	'ccu':'P','ccc':'P','cca':'P','ccg':'P',
	'cau':'H','cac':'H','caa':'Q','cag':'Q',
	'cgu':'R','cgc':'R','cga':'R','cgg':'R',
	'auu':'I','auc':'I','aua':'I','aug':'M',
	'acu':'T','acc':'T','aca':'T','acg':'T',
	'aau':'N','aac':'N','aaa':'K','aag':'K',
	'agu':'S','agc':'S','aga':'R','agg':'R',
	'guu':'V','guc':'V','gua':'V','gug':'V',
	'gcu':'A','gcc':'A','gca':'A','gcg':'A',
	'gau':'D','gac':'D','gaa':'E','gag':'E',
	'ggu':'G','ggc':'G','gga':'G','ggg':'G'}



class NewDNASequence():

	def __init__(self,name,sequence):
		self.name=name
		self.sequence=[]

		for s in sequence:
			d=DNANucleotide(s)
			self.sequence.append(d)

	def molecularWeight(self):
		mwt=0.0
		for s in self.sequence:
			mwt+=s.weight  #uses the weight as class variable from DNANucleotide class.
		return mwt

	def __str__(self):

		nucs=[]

		for s in self.sequence:
			nucs.append(s.name)

		return "".join(nucs)

class DNANucleotide:


	def __init__(self,nuc):
		nucleotides = {'a':313.2,'c':289.2,'t':304.2,'g':329.2}
		self.nuc=nuc
		self.weight=nucleotides[nuc]
class Sequence:

	def __init__(self, name, sequence):
		self.name=name
		self.sequence=sequence
		self.residues={}

	def search(self, pattern):
		return self.sequence.find(pattern)
	
	def molecularWeight(self):
		mwt=0.0

		for residue in self.sequence:
			mwt+=self.residues[residue]

		return mwt

	def validSequence(self):

		for i in self.sequence:
			if not i in self.residues:
				return False

		return True

class DNASequence(Sequence):

	def __init__(self,name,sequence):
		Sequence.__init__(self,name,sequence) #uses parent's init.
		self.residues={'a':313.2,'c':289.2,'t':304.2,'g':329.2}

	#return transcription as a string
	def transcribe(self):
		return self.sequence.replace('t','u')

	#return transcription into an RNA class instance
	def transcribeToRNA(self):
		rnaSeq=self.sequence.replace('t','u')
		rnaName='Transcibed from '+self.name
		return RNASequence(rnaName,rnaSeq)

class RNASequence(Sequence):

	def __init__(self,name,sequence):
		Sequence.__init__(self,name,sequence)

	def translate(self):

		peptide=[]
		for n in range(0,len(self.sequence),3):
			codon=self.sequence[n:n+3]
			peptide.append(rnaToProtein[codon])
		peptideSequence="".join(peptide)	

		return peptideSequence

class ProteinSequence(Sequence):

	def __init__(self,name,sequence):
		Sequence.__init__(self,name,sequence)


#start of program	
myseq=Sequence("lala","agtatata")
print(myseq.name)
print(myseq.sequence)
print(myseq.search("gta"))
print(type(myseq))


#test DNASequence class
dnaseq=DNASequence("testDNAseq","gat")
print(dnaseq.name)
print(dnaseq.sequence)
print(dnaseq.search("gat"))
print(dnaseq.transcribe())
print(dnaseq.transcribeToRNA())
print(dnaseq.transcribeToRNA().sequence)
print(type(dnaseq))

#test RNA Sequence.
rnaseq=RNASequence("testRNAseq","gcugauauc")
print(rnaseq.name)
print(rnaseq.sequence)
print(rnaseq.search("gat"))
print(type(rnaseq))
print(rnaseq.translate())


#test protein sequence.
proteinseq=ProteinSequence("proteinseq","MDVTLFSLOY")
print("protein sequence:")
print(proteinseq.sequence)
print(proteinseq.search("LFS"))


print(dnaseq.sequence+" has molecular weight  :"+str(dnaseq.molecularWeight()))
print(dnaseq.validSequence())



myDNASequence=NewDNASequence("A new dna sequence.","gctgatatc")
print(myDNASequence.sequence[2].nuc)
print(myDNASequence.molecularWeight())

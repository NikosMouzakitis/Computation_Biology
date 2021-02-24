from Bio.SeqIO import parse
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

f = open("data.fasta")
records=parse(f,"fasta") 
for record in records:
	print("ID: %s"%record.id)
	print("Name: %s"%record.name)
	print("Desc: %s"%record.description)
	print("Annot: %s"%record.annotations)
	print("Sequence Data: %s"%record.seq)
	print("Sequence Alphabet: %s"%record.seq.alphabet)


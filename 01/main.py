from Bio import SeqIO

f="example_protein.fasta"

print("demonstration with FASTA files")


handle = open(f,"rU")
print("handle acquired")



#print records
for record in SeqIO.parse(handle,"fasta"):
	print(record.id)
	print(record.seq)
	print(record.description)
handle.close()

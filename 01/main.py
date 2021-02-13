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

#########################################
#	using the Sequences.fasta	#
#########################################

f="Sequences.fasta"
handle=open(f,"rU")
print("handle acquired on %s file."%(f))

lines=handle.readlines()

seq_dict={}
seq_name=None

for line in lines:
	if line[0]=='>':	#special for FASTA start
		seq_name=line[1:].strip()
		seq_dict[seq_name]=""
	else:
		if seq_name:
			seq_dict[seq_name]+=line.strip()


print(seq_dict)

for i in seq_dict.keys():
	print("Gene:>>")
	print(i)
	print("Sequence:>>")
	print(seq_dict[i])

handle.close()

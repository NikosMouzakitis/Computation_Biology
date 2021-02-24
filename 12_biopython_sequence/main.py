from Bio.Seq import Seq
from Bio.Alphabet import single_letter_alphabet

seq=Seq("ACGT")
print("Sequence: %s"%seq)
print("Alphabet: %s"%seq.alphabet)
print(seq)
test_seq=Seq('AGTATCGAATCGA',single_letter_alphabet)
print(test_seq)
print(test_seq.alphabet)


seq=Seq('ACGTTCGCA')
print(seq[0])
print(seq)
for i in range(0,len(seq)):
	print(seq[i])	
seq2=Seq('AAATTT')
seq=seq+seq2
print(seq.lower())
print(seq.upper())
seq3 = Seq(' ACGT ')
print(seq3)
print(seq3.strip())


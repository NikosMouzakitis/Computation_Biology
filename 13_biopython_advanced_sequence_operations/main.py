from Bio.Alphabet import IUPAC
from Bio.Data import IUPACData
from Bio.Seq import Seq
import pprint

nucleotide=Seq('TCCAGCAT',IUPAC.ambiguous_dna)
print("DNA sequence  :"+nucleotide)
print("Complement    :"+nucleotide.complement())#it creates the complement for the sequence.

#Data used to produce the complement.
print(IUPACData.ambiguous_dna_complement)

#GC content
from Bio.SeqUtils import GC
nucleotide=Seq('GACTGACTTCGA',IUPAC.unambiguous_dna)
print("Nucleotide: "+nucleotide)

print("GC content: "+str(GC(nucleotide)))



#transcription
from Bio.Seq import transcribe
dna_seq=Seq('ATGCCGATCGTAT',IUPAC.unambiguous_dna)
print("dna_seq   : "+nucleotide)
print("transcibed: "+transcribe(dna_seq))
rna_seq=transcribe(dna_seq)
print("rna_seq   : "+rna_seq)
rna_seq_back_transcribed = rna_seq.back_transcribe()
print("rna_seq.bt: "+rna_seq_back_transcribed)

dna_template = rna_seq_back_transcribed.reverse_complement()
print("DNA templa:"+dna_template)

seqt=Seq('GAGATC',IUPAC.unambiguous_dna)
print(transcribe(seqt))

	
	
rna_seq = Seq("AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGA",IUPAC.unambiguous_rna)
print(rna_seq)
print(rna_seq.translate())

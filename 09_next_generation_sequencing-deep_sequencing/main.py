import subprocess
#automate alignment
#with open('e_coli_10000snp.sam',"w") as output_sam:
#	subprocess.check_call(['bwa','mem','NC_008253.fna','e_coli_10000snp.fq'], stdout=output_sam)
print("1")
output_sam=open('e_coli_10000snp.sam',"w")
subprocess.check_call(['bwa','mem','NC_008253.fna','e_coli_10000snp.fq'], stdout=output_sam)
output_sam.close()
print("2")
with open("e_coli_10000snp.bam","w") as output_bam:
	subprocess.check_call(['samtools','view','-b','-S',"e_coli_10000snp.sam"],stdout=output_bam)


#we could continue create more wrappers like that to include the whole 
#samtools commands as we see in the readme file.

import os.path
import pysam

print("working with pysam")

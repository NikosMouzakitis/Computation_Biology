import pysam
import os.path
import subprocess

def sort_and_index(bam_filename):
	prefix,suffix=os.path.splitext(bam_filename)
	
	#generated sorted bam file
	sorted_bamfilename=prefix+".sorted.bam"
	#sort it using pysam's output
	print("generated resorted BAM:"+sorted_bamfilename)
	pysam.sort("-o",sorted_bamfilename,bam_filename)

	#index it
	print("Index BAM:"+sorted_bamfilename)
	pysam.index(sorted_bamfilename)

	return sorted_bamfilename


#automate alignment

output_sam=open('e_coli_10000snp.sam',"w")
subprocess.check_call(['bwa','mem','NC_008253.fna','e_coli_10000snp.fq'], stdout=output_sam)
output_sam.close()
with open("e_coli_10000snp.bam","w") as output_bam:
	subprocess.check_call(['samtools','view','-b','-S',"e_coli_10000snp.sam"],stdout=output_bam)


#we could continue create more wrappers like that to include the whole 
#samtools commands as we see in the readme file.

print("working with pysam")
output_sorted_bamfilename=sort_and_index("e_coli_10000snp.bam")
print(output_sorted_bamfilename)




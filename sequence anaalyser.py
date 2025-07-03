from Bio import SeqIO
from Bio.Seq import Seq
import os
# Getting the sequence form the fasta

fasta_file= input("Enter the fasta file name:")
if not os.path.isfile(fasta_file):
          print(f" Error: File '{fasta_file}' not found.")
else:
      record=SeqIO.read(fasta_file, "fasta")
      sequence= record.seq.upper()
      print(f"Sequnce id: {record.id}")
      print(f"Sequence: {sequence}")
      print(F"Lenght: {len(sequence)}")

##calculate GC and AT content
gc_count= sequence.count("G") + sequence.count("C")
at_count= sequence.count("A")+ sequence.count("T")
gc_content= gc_count/len(sequence)*100
at_content = at_count/len(sequence)*100
#Email your CV to: atharvakakde@genextgenomics.com
print(f"GC Content: {gc_content:.2f}%")
print(f"AT Content: {at_content:.2f}%")
# calculate AT/GC ratio
if gc_count !=0:
    at_gc_ratio=at_count/gc_count
    print(f"AT/GC Ratio: {at_gc_ratio:.2f}")
else:
        print("GC count is zero, cannot compute AT/GC ratio")

#reverse compliment

reverse_complement= sequence.reverse_complement()
print(f"Reverse Complement: {reverse_complement}")
##t transcription
rna_sequence=sequence.transcribe()
print(f"RNA Transcript: {rna_sequence}")

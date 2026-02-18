# DNA Analysis Tool: Basic metrics and transcription
sequence = "ATGCGATCGTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC"

# 1. Counting Nucleotides
counts = {"A": sequence.count("A"), "T": sequence.count("T"), 
          "G": sequence.count("G"), "C": sequence.count("C")}

# 2. Calculating GC Content
gc_content = (counts["G"] + counts["C"]) / len(sequence) * 100

# 3. Transcription (DNA -> RNA)
rna_sequence = sequence.replace("T", "U")

print(f"Sequence Length: {len(sequence)} bp")
print(f"GC Content: {gc_content:.2f}%")
print(f"RNA: {rna_sequence}")

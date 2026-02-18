from Bio.Seq import Seq

# The jellyfish DNA sequence
gfp_dna = Seq("ATGAGTAAAGGAGAAGAACTTTTCACTGGAGTTGTCCCAATTCTTGTTGAATTAGATGGTGATGTTAATGGGCACAAATTTTCTGTCAGT")

# The one-line 'Pro' translation
gfp_protein = gfp_dna.translate()

print(f"Professional Translation: {gfp_protein}")
print("Analysis complete for the Daerblue Lab!")

# Bioinformatics Toolkit & Portfolio 
### Created by Ayushi Shukla

Welcome to my computational biology journey. This repository documents Bioinformatics journey, featuring foundational projects.

---

##  Project Tracker
##  Project Tracker (Top 10 Bioinformatics Portfolio)
| S.No | Project Title | Status | Learning Outcome |
| :--- | :--- | :--- | :--- |
| 1 | DNA Sequence Alignment | ✅ Completed | Needleman-Wunsch & Smith-Waterman |
| 2 | Protein Sequence Analysis | ✅ Completed | Secondary Structure Prediction |
| 3 | Genomic Data Visualization | ✅ Completed | Matplotlib & Circos Plots |
| 4 | Phylogenetic Tree Construction | ✅ Completed | Evolutionary Relationship Mapping |
| 5 | GC Content Calculation | ✅ Completed | Genome Stability & Coding Regions |
| 6 | SNP Analysis | ✅ Completed | Genetic Variation & VCF Data |
| 7 | Gene Expression Analysis | ✅ Completed | RNA-seq & Differential Expression |
| 8 | Functional Annotation | 📅 Planned | GO & KEGG Pathway Mapping |
| 9 | Protein Structure Viz | 📅 Planned | 3D Modeling (PyMOL/Chimera) |
| 10 | Microbial Community Analysis | 📅 Planned | 16S rRNA & Microbiome Studies |

---

##  Current Scripts
### 1. DNA Analysis Core (`dna_analysis.py`)
Basic metrics including GC content and transcription logic.

### 2. Custom Translation Engine (`dna_to_protein.py`)
A manual implementation of the genetic code to translate DNA into Amino Acids.

### 3. Professional GFP Translation (`gfp_pro_translation.py`)
Using the Biopython library to handle real-world jellyfish GFP sequences.


##  Project Highlights

## 1. Clinical Sequence Alignment & Variant Analysis
**Task:** Comparative genomic alignment of the SARS-CoV-2 Spike Protein (Wuhan vs. Delta).
**Technical Specs:** - **Algorithm:** Needleman-Wunsch (Global Alignment).
- **Matrix:** **BLOSUM62** for biologically accurate scoring.
**Result:** Successfully identified key missense mutations (like **L452R**) and achieved an alignment score of 782.0.

### 2. Protein Analysis & Lab Prep
* **Task:** Analyzed the Green Fluorescent Protein (GFP) sequence.
* **Objective:** Determine the **Isoelectric Point (pI)** and **Molecular Weight**.
* **Result:** Generated the exact chemical parameters required for protein purification experiments.

## 3. Sliding Window GC Content & Genomic Stability
**Task:** Visualization of DNA stability across the Spike protein genome.
**Method:** Implemented a **Sliding Window algorithm** to find GC-rich regions.
**Value:** Essential for identifying coding regions and primer design.
**Visual:** Created `wuhan_spike_gc_plot.png` showing local fluctuations in genomic stability.

### Project 4: Evolutionary Mapping (Phylogeny)
Task: Construct a Phylogenetic Tree to visualize the relationship between SARS-CoV-2 variants.

*  **Algorithm:** Used the UPGMA (Unweighted Pair Group Method with Arithmetic Mean) clustering method.

* **Data Source:** Applied a distance matrix based on observed mutations between the Wuhan, Delta, and Omicron variants.

####  Methodology & Assumptions
To build this tree, I utilized the Molecular Clock Hypothesis.

* **The Assumption:** This model assumes that DNA sequences evolve at a relatively constant rate over time.

* **The Result:** Because UPGMA uses this "constant rate" logic, it produces a Symmetrical (Ultrametric) Tree where all "leaves" (the variants) are equidistant from the root. This is a simplified but powerful way to visualize how Omicron has diverged significantly further from the Wuhan strain than Delta did.

### Project 6: Clinical SNP AnalysisTask: 
Filter and analyze Single Nucleotide Polymorphisms (SNPs) from a VCF (Variant Call Format) file.
* **Objective:** Identify high-confidence genetic variations by removing sequencing noise and low-quality "calls."
#### Methodology:
* ***VCF Parsing:*** Developed a custom parser to extract genomic coordinates (POS), reference/alternate alleles (REF/ALT), and quality scores (QUAL).
* ***Quality Thresholding:*** Implemented a filter requiring a Quality Score > 50 and a PASS status. This ensures the mutations analyzed are statistically significant and not artifacts of the sequencing machine.
* **Results:** Successfully isolated 3 high-confidence SNPs on Chromosome 1, including rs123 and rs456, which are ready for clinical annotation. 

### High-Confidence SNP Results
| Chromosome | Position | Mutation | Quality |
| :--- | :--- | :--- | :--- |
| **chr1** | 1001 | A -> G | 60.0 |
| **chr1** | 1100 | C -> T | 95.0 |
| **chr1** | 1200 | G -> A | 55.0 |

### Project 7: Differential Gene Expression Visualization
* **Objective:** Identify changes in gene activity between two biological conditions.

* **Tooling:** Utilized Pandas for matrix manipulation and Seaborn for Heatmap generation.

* **Insight:** The heatmap reveals a clear "signature" where growth-related genes were suppressed and repair-related genes were activated in the treatment group, demonstrating the cellular response to the stimulus.
*  **Results:**
Generated a Differential Gene Expression (DGE) heatmap using Seaborn and Pandas.

Visualized mRNA expression levels for critical genes (BRCA1, TP53, MYC, EGFR) across Healthy and Treated samples.

Implemented a RdYlBu_r color map to highlight Up-regulated (Red) and Down-regulated (Blue) genetic signatures.

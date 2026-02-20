# 🧬 Bioinformatics Toolkit & Portfolio 
### Created by Ayushi Shukla

Welcome to my computational biology journey. This repository documents Bioinformatics journey, featuring foundational projects.

---

## 🚀 Project Tracker
## 🚀 Project Tracker (Top 10 Bioinformatics Portfolio)
| S.No | Project Title | Status | Learning Outcome |
| :--- | :--- | :--- | :--- |
| 1 | DNA Sequence Alignment | ✅ Completed | Needleman-Wunsch & Smith-Waterman |
| 2 | Protein Sequence Analysis | ✅ Completed | Secondary Structure Prediction |
| 3 | Genomic Data Visualization | ✅ Completed | Matplotlib & Circos Plots |
| 4 | Phylogenetic Tree Construction | 📅 Planned | Evolutionary Relationship Mapping |
| 5 | GC Content Calculation | ✅ Completed | Genome Stability & Coding Regions |
| 6 | SNP Analysis | 📅 Planned | Genetic Variation & VCF Data |
| 7 | Gene Expression Analysis | 📅 Planned | RNA-seq & Differential Expression |
| 8 | Functional Annotation | 📅 Planned | GO & KEGG Pathway Mapping |
| 9 | Protein Structure Viz | 📅 Planned | 3D Modeling (PyMOL/Chimera) |
| 10 | Microbial Community Analysis | 📅 Planned | 16S rRNA & Microbiome Studies |

---

## 📂 Current Scripts
### 1. DNA Analysis Core (`dna_analysis.py`)
Basic metrics including GC content and transcription logic.

### 2. Custom Translation Engine (`dna_to_protein.py`)
A manual implementation of the genetic code to translate DNA into Amino Acids.

### 3. Professional GFP Translation (`gfp_pro_translation.py`)
Using the Biopython library to handle real-world jellyfish GFP sequences.


## 🔍 Project Highlights

* ### 1. Clinical Variant Alignment (SARS-CoV-2)
* **Task:** Performed comparative genomic alignment of the Spike Protein (Wuhan vs. Delta).
* **Objective:** Use the **BLOSUM62** matrix to identify high-impact missense mutations.
* **Result:** Successfully identified key mutation regions (like L452R) using Biopython’s `PairwiseAligner`.

### 2. Protein Analysis & Lab Prep
* **Task:** Analyzed the Green Fluorescent Protein (GFP) sequence.
* **Objective:** Determine the **Isoelectric Point (pI)** and **Molecular Weight**.
* **Result:** Generated the exact chemical parameters required for protein purification experiments.

### 3. Sliding Window GC Content
* **Task:** Visualized DNA stability across the Spike protein genome.
* **Objective:** Use a "Sliding Window" algorithm to find GC-rich regions.
* **Visual:** Created a Matplotlib line graph showing local fluctuations in genomic stability (wuhan_spike_gc_plot.png)


# Bacterial Illumina Sequencing Analysis Pipeline

This repository demonstrates a **bacterial whole genome sequencing (WGS) analysis workflow** using Illumina sequencing data. The project is designed as a **portfolio mini-project** to showcase practical skills in **bioinformatics, Python scripting, Linux-based workflows, and reproducible genomics analysis**, relevant for R&D environments.

---

## Project Overview

The pipeline follows a standard bacterial genomics workflow:

1. Quality control of raw sequencing reads
2. Read trimming and filtering
3. Genome assembly
4. Assembly quality assessment and visualization

Large raw sequencing files and intermediate outputs are intentionally excluded to keep the repository lightweight and focused on **analysis logic and reproducibility**.

---

## Tools & Technologies

* **Programming:** Python (pandas, Biopython, matplotlib)
* **Bioinformatics Tools:** FastQC, fastp, SPAdes
* **Operating System:** Linux (command-line workflows)
* **Version Control:** Git / GitHub

---

## Pipeline Components

### 1. Quality Control

* Initial quality assessment of Illumina reads using **FastQC**
* Automated extraction of QC metrics using Python

### 2. Read Trimming

* Adapter removal and quality trimming using **fastp**

### 3. Genome Assembly

* De novo genome assembly performed using **SPAdes**

### 4. Assembly Statistics & Visualization

Custom Python scripts were developed to:

* Calculate assembly metrics (total length, number of contigs, N50, largest contig)
* Generate contig length distribution plots

Scripts are located in the `scripts/` directory.

---

## Repository Structure

```
bacterial-wgs-pipeline/
├── scripts/                 # Python scripts for analysis and visualization
├── results/                 # Small result files (CSV summaries, plots)
├── README.md                # Project documentation
```

---

## Reproducibility

* All analysis steps are documented
* Scripts are modular and reusable
* Version-controlled using Git

This structure reflects good practices commonly used in **industrial and academic R&D bioinformatics teams**.

---

## Notes

* Raw FASTQ files and large intermediate assembly files are excluded due to size constraints
* The pipeline logic can be easily extended to other bacterial genomes

---

## Author

**Vimala Valli Vempati**
M.Sc. Agrobiotechnology | M.Sc. Microbiology
GitHub: [https://github.com/vimalavalli14](https://github.com/vimalavalli14)

from Bio import SeqIO
import pandas as pd

# Path to assembled contigs
contigs_file = "../results/assembly/contigs.fasta"

# Function to calculate N50
def calculate_n50(lengths):
    sorted_lengths = sorted(lengths, reverse=True)
    total_len = sum(sorted_lengths)
    cumsum = 0
    for l in sorted_lengths:
        cumsum += l
        if cumsum >= total_len / 2:
            return l
    return 0

# Parse contigs
contig_lengths = [len(rec.seq) for rec in SeqIO.parse(contigs_file, "fasta")]

# Compute statistics
assembly_stats = {
    "Total_contigs": len(contig_lengths),
    "Total_length": sum(contig_lengths),
    "Largest_contig": max(contig_lengths),
    "N50": calculate_n50(contig_lengths)
}

# Save as CSV
df = pd.DataFrame([assembly_stats])
df.to_csv("../results/assembly/assembly_stats.csv", index=False)

print("Assembly statistics saved to ../results/assembly/assembly_stats.csv")
print(assembly_stats)


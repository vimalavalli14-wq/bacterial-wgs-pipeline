import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend for WSL

from Bio import SeqIO
import matplotlib.pyplot as plt
import os

# Path to assembled contigs
contigs_file = "../results/assembly/contigs.fasta"
output_plot = "../results/assembly/contig_length_distribution.png"

# Parse contig lengths
contig_lengths = [len(rec.seq) for rec in SeqIO.parse(contigs_file, "fasta")]

# Plot histogram
plt.figure(figsize=(10,6))
plt.hist(contig_lengths, bins=50, color='skyblue', edgecolor='black')
plt.title('Contig Length Distribution')
plt.xlabel('Contig Length (bp)')
plt.ylabel('Number of Contigs')
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()
plt.savefig(output_plot)
plt.show()

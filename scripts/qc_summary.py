import os
import zipfile
import pandas as pd

FASTQC_DIR = "../results/qc"
OUTPUT_FILE = "../results/qc/fastqc_summary.csv"

rows = []

for file in os.listdir(FASTQC_DIR):
    if file.endswith("_fastqc.zip"):
        with zipfile.ZipFile(os.path.join(FASTQC_DIR, file), 'r') as zip_ref:
            with zip_ref.open(file.replace(".zip", "") + "/summary.txt") as summary:
                for line in summary:
                    status, module, _ = line.decode().strip().split("\t")
                    rows.append({
                        "sample": file,
                        "module": module,
                        "status": status
                    })

df = pd.DataFrame(rows)
df.to_csv(OUTPUT_FILE, index=False)
print(f"QC summary written to {OUTPUT_FILE}")

import gzip
import shutil

# Input and output paths
input_path = "./codelight/candidates.jsonl"
output_path = "./codelight/candidates.jsonl.gz"

# Compress the file
with open(input_path, "rb") as f_in:
    with gzip.open(output_path, "wb") as f_out:
        shutil.copyfileobj(f_in, f_out)

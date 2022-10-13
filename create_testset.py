import pandas as pd
import os
import numpy as np

file_path = "sexy_selfie_labels.csv"
def_label = 'sexy_selfie'
number_files = 100
df = pd.read_csv(file_path,names=['path','label'])
paths = np.array(df['path'])
labels = np.array(df['label'])
cnt = 0
for i, p in enumerate(paths):

    if labels[i] == def_label:
        out_path = 'small_'+ p
        cmd = f"cp {p} {out_path}"
        os.system(cmd)
        cnt += 1
        if cnt>=100:
            break

print(f"{number_files} files transfered to {def_label} folder")
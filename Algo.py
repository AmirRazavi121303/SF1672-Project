import numpy as np
import pandas as pd

df = pd.read_csv("/Users/amir/Downloads/CodeAmir/SF1672/riksdag_2026_overgangsmatris_256x256.csv", index_col=0)
ny_ordning = df.index.drop("Ingen (Ø)").to_list() + ["Ingen (Ø)"]
df = df.reindex(index = ny_ordning, columns = ny_ordning)

P = np.transpose(df.to_numpy())

def i(parti):
    return df.index.to_list().index(parti)

v = np.zeros((256, 1))
v[-1] = 1

Pn = np.linalg.matrix_power(P, 10)
dict = {zip(ny_ordning, v)}

print(P[i("KD"), i("S")])
print(dict)

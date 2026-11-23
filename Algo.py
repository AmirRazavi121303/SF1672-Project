import numpy as np
import pandas as pd

def get_matrix(link):
    df = pd.read_csv(link, index_col=0)
    ny_ordning = df.index.drop("Ingen (Ø)").to_list() + ["Ingen (Ø)"]
    df = df.reindex(index = ny_ordning, columns = ny_ordning)
    return np.transpose(df.to_numpy()), ny_ordning

def get_state_vector():
    v = np.zeros((256, 1))
    v[-1] = 1
    return v

def i(link, parti):
    df = pd.read_csv(link, index_col=0)
    ny_ordning = df.index.drop("Ingen (Ø)").to_list() + ["Ingen (Ø)"]
    df = df.reindex(index = ny_ordning, columns = ny_ordning)
    return df.index.to_list().index(parti)

def main():
    csv_link = "/Users/amir/Downloads/CodeAmir/SF1672/riksdag_2026_overgangsmatris_256x256.csv"
    
    P, ny_ordning = get_matrix(csv_link)
    v = get_state_vector()
    Pn = np.linalg.matrix_power(P, 1)
    status_vektor = []
    
    for row in  Pn @ v:
        for column in row:
            status_vektor.append(column)
    dictionary = dict(zip(ny_ordning, status_vektor))
    for row, val in dictionary.items():
        print(f"{row}:  {val:.6f}")
        
    print(f"Den koalitionen som är mest sannolik är {max(dictionary, key=dictionary.get)}")

if __name__ == "__main__":
    main()
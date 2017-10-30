import pandas as pd
import numpy as np
def read_pokemon():
    df = pd.read_csv(r'E:\python_files\csv\Pokemon.csv')
    for n in range(df.shape[0]):
        print(df.ix[n])
    return df 



if __name__ == '__main__':
    read_pokemon()
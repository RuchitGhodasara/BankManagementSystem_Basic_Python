def balance(i_d):
    import pandas as pd
    data = pd.read_csv('mainFile.csv', index_col=0)
    bala = data.loc[i_d, 'CurrentBalance']
    return bala

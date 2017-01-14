import pandas as pd

df = pd.read_csv('census.csv',index_col='SUMLEV')
df['SUMLEV_ADD'] = df.index
df.set_index('STNAME',inplace=True)
print(df.head())

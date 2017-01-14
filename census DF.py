import pandas as pd

##df = pd.read_csv('census.csv')
##print(df['SUMLEV'].unique())
##print(df['SUMLEV'].count())
##print(len(df['SUMLEV'].unique()))
##df = df[df['SUMLEV']==50]
##df.set_index(['STNAME','CTYNAME'],inplace=True)
##pop_df = df[[
##    'POPESTIMATE2010','POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013','POPESTIMATE2014', 'POPESTIMATE2015',
##    'BIRTHS2010', 'BIRTHS2011', 'BIRTHS2012', 'BIRTHS2013', 'BIRTHS2014','BIRTHS2015']]
##print(pop_df.head())
##
##print(pop_df.loc[[('Alabama','Autauga County'),('Alabama','Blount County')]][['POPESTIMATE2010','BIRTHS2010']])
##print(pop_df.loc['Alabama','Blount County'])

purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
purchase_4 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Food',
                        'Cost': 3.00})
##df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
##print(df)
##df['Location']=df.index
##df.set_index(['Location','Name'],inplace=True)
##new_df = pd.DataFrame([purchase_4],index=['Store 2'])
##new_df['Location']=new_df.index
##new_df.set_index(['Location','Name'],inplace=True)
##df = df.append(new_df)
##print(df)
##s = pd.Series(data={'Cost': 3.00, 'Item Purchased': 'Kitty Food'}, name=('Store 2', 'Kevyn'))
##print(s)
##print(purchase_4)



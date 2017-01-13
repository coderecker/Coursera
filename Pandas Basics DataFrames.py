import pandas as pd
import time
import datetime
import numpy as np

def time_func(fn):
    def dummy_fn(*args,**kwargs):
        before = datetime.datetime.now()
        print(before)
        x = fn(*args,**kwargs)
        after = datetime.datetime.now()
        print(after)
        print('Execution Time for {}: '.format(fn.__name__),after - before)
        return x
    return dummy_fn


##purchase_order1 = pd.Series({'Name':'Kevin',
##                             'Item Purchased':'Dog Food',
##                             'Cost':33.4})
##
##purchase_order2 = pd.Series({'Name':'Jenny',
##                             'Item Purchased':'Dog collar',
##                             'Cost': 50.0})
##
##purchase_order3 = pd.Series({'Name':'David',
##                             'Item Purchased':'Kennel',
##                             'Cost':100})

purchase_order1 = {'Name':'Kevin',
                   'Item Purchased':'Dog Food',
                   'Cost':33.4,
                   'Date':'01/11/2017'}

purchase_order2 = {'Name':'Jenny',
                   'Item Purchased':'Dog collar',
                   'Cost': 50.0}

purchase_order3 = {'Name':'David',
                   'Item Purchased':'Kennel',
                   'Cost':100}


df = pd.DataFrame([purchase_order1, purchase_order2, purchase_order3], index=['Store 1','Store 1','Store 2'])
df.loc['Store 2','Cost']=100.25
print(df)
##print(df['Name'])
print(df.iloc[1:3,0:3])
#df.drop('Date',inplace=True, axis=1)
del df['Date']
print(df)
##print(df.loc['Store 1']['Name'])
##print(df.iloc[0])
##print(type(df.loc['Store 2']))

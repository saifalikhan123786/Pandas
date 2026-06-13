import pandas as pd

# customer dataframe 

df_customers=pd.DataFrame({
    'CustomerID':[1,2,3],
    'Name':['Saif','Ali','Khan']
})

## Order Data Frame

df_orders=pd.DataFrame({
    'CustomerID':[1,2,4],
    'OrderAmount':[250,450,350]
})

# merge

df_merge=pd.merge(df_customers,df_orders, on="CustomerID", how="inner")
print('inner join')
print(df_merge)
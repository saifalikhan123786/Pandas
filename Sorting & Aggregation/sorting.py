## sorting data 
## Ascending order = True
## Descending order = False

import pandas as pd

data={
    "Name": ['Saif','Ali','khan'],
    "Age":[28,34,22],
    "Salary":[10000,20000,30000]
}

df=pd.DataFrame(data)

df.sort_values(by="Age", ascending=True, inplace=True)
print("Sorted Age my Descending")
print(df)
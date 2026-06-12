import pandas as pd 

data={
    "Name": ['saif',None,'usman','adil','haris','asad','ahmad','raju'],
    "Age":[12,None,56,78,90,67,66,34],
    "Salary":[50000,None,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,None,78,92,88,95,80,89]
}

df=pd.DataFrame(data)
print(df)

df.dropna(inplace=True)
print(df)
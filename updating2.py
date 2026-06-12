import pandas as pd 

data={
    "Name": ['saif','ali','usman','adil','haris','asad','ahmad','raju'],
    "Age":[12,23,56,78,90,67,66,34],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,90,78,92,88,95,80,89]
}

df=pd.DataFrame(data)
print(df)

# increasing salary my 5%

df['Salary']=df['Salary'] * 1.05
print(df)
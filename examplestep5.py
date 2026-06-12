import pandas as pd 

data={
    "Name": ['saif','ali','usman','adil','haris','asad','ahmad','raju'],
    "Age":[12,23,56,78,90,67,66,34],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,90,78,92,88,95,80,89]
}

df=pd.DataFrame(data)

print("Sample Datafram")
print(df)

print("Name(single  column return series)")
name=df['Name']
print(name)

## selecting multiple column
subset=df[["Name","Salary"]]
print('\n subset with name and salary')
print(subset)

import pandas as pd 

data={
    "Name": ['saif','ali','usman','adil','haris','asad','ahmad','raju'],
    "Age":[12,23,56,78,90,67,66,34],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,90,78,92,88,95,80,89]
}

df=pd.DataFrame(data)
print(df)

df["Bonus"]=df['Salary'] * 0.1
print (df)

## using insert()

df.insert(0,"Employee_id",[10,20,30,40,50,60,70,80])
print(df)
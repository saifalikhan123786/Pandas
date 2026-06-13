import pandas as pd

data={
    "Name": ['Saif','Ali','khan','Haris','Asad',],
    "Age":[28,34,22,34,28],
    "Salary":[500000,600000,450000,520000,480000]
}

df=pd.DataFrame(data)

grouped=df.groupby("Age")["Salary"].sum()
print(grouped)
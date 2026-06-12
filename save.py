import pandas as pd

data={
    "Name":['saif','Ali','Khan','ahmad'],
    "Age":[10,20,30,40],
    "City":['Lahore','Sialkot','shadra','pindi']
}

df=pd.DataFrame(data)
print(df)

# df.to_csv("output.csv", index=False)
# df.to_excel("output.xlsx", index=False)
df.to_json("output.json", index=False)





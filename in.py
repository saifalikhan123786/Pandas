import pandas as pd

data={
    "Name":['saif','Ali','Khan','ahmad'],
    "Age":[10,20,30,40],
    "City":['Lahore','Sialkot','shadra','pindi']
}

df=pd.DataFrame(data)


print('Displaying the info of data set')
print(df.info())
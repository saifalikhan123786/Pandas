import pandas as pd 

data={
    "Name": ['saif','ali','usman','adil','haris','asad','ahmad','raju'],
    "Age":[12,23,56,78,90,67,66,34],
    "Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance Score":[85,90,78,92,88,95,80,89]
}

df=pd.DataFrame(data)

high_salary=df[df['Salary']>50000]
print('Employees with salry > 50000')
print(high_salary)

## filtering rows salary > 50000 & age > 30

filtered= df[(df['Age']>30) & (df['Salary']>50000)]
print("Employee list age> 30 + salary > 50000")
print(filtered)

## Using or condition 

filtered_or= df[(df['Age']> 35) | (df['Performance Score']>90)]
print('Employees older then 35 OR performance score > 90')
print(filtered_or)


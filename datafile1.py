import pandas as pd
import csv
# opne file
data = pd.read_csv(r"C:\Users\HP REGISTERED\Desktop\python\data1.csv",encoding="cp1256")
# print(data)
# list of name
n=[]
for index, row in data.iterrows():
        n.append(row['name'])
print(n)
df2=pd.DataFrame()
df2['id']=data['age']
df2['name']=data['name']
df2['Address']=data['Address']
df2['age']=data['age']
print(df2)

#age 
d=data.loc[data.age>35]
print(d)
d1=data.loc[data.age<20]
d2=df2.drop_duplicates(subset=['age'])
print(d2)
#sum of age
n=0
for i in df2['age'] :
    n=n+i
# print(n)
# age over 30
df4=pd.DataFrame()
d1=data.loc[data.age>30]
df4['age']=d1['age']
print(df4)
#save data frame in CSV
df4.to_csv('file_name_df4.csv')
# age =20
df5=pd.DataFrame()
d2=data.loc[data.age ==20]
df5['name']=d2['name']
df5['age']=d2['age']
print(df5)
#save data frame in CSV
df5.to_csv('file_name_df5.csv')




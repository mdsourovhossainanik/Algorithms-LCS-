import pandas as pd
data={
    'name':['pavan','kapil','lalit','ishan','om'],
    'age':[25,None,44,23,None],
    'salary':[50000,60000,70000,None,None]

}
df=pd.DataFrame(data)
print("Orginal DataFrame:")
print(df)
# print(df.isnull().sum())
# print(df.isnull().mean()*100)#koto % data null ace seta dekhabe
# df_drop=df.dropna()#null data set drop/avoid kore dibe full data gula dekhabe
# print(df_drop)
df['age'].fillna(df['age'].mean(),inplace=True)
df['salary'].fillna(df['salary'].mean(),inplace=True)
print('clean data frame:')
print(df)
# print(df.isnull().mean()*100)



from sklearn.preprocessing import LabelEncoder
import pandas as pd
df=pd.read_csv("d:\Downloads\data.csv ")
df_label=df.copy()
le=LabelEncoder()
df_label['gender']=le.fit_transform(df_label['gender'])#encoding hocca 1/0 dara


print('\nlabel Encodded Data:')
print(df_label[['name','age','salary','gender']])

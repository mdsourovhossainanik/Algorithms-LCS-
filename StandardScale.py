import pandas as pd
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.model_selection import train_test_split
data={
    'StudyHours':[1,2,3,4,5],
    'TestScore':[40,50,60,70,80]
}
df=pd.DataFrame(data)
print("StandardScaler output:")
Std_df=StandardScaler().fit_transform(df)
print(pd.DataFrame(Std_df,columns=['StudentHours','TestScore']))
print("\nMinMaxScaled output:")
MinMax_df=MinMaxScaler().fit_transform(df)
print(pd.DataFrame(MinMax_df,columns=['StudentHours','TestScore']))


x=df[['StudyHours']]
y=df[['TestScore']]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
print("---X-Training Data----")
print("Train data",x_train)
print("Test data:",x_test)
print("---Y-Training Data----")
print("Train data",y_train)
print("Test data:",y_test)
 

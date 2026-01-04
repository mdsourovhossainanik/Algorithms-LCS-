import pandas as pd
import numpy as np
traind=pd.read_csv('d:\\Downloads\\test.csv') # file ta k read kore niye asbe akhane
# print(traind)
print(traind.head(10))# 1st 10 row print korbe
# print(traind.tail())# 1st 5 colum print korbe

df=traind.copy()

print(np.isinf(df['PassengerId']))##infinit value check kore
#
#df.drop_duplicates(inplace=True)##duplicate data handle it
print(df)
print(df.shape) # row and colum a sape print korbe

print(df.isnull()) ##null gulo true return dibe
print(df.isnull().sum()) #data frame colum wise jotogulo null valu ace sum korlam
print("Null value of age:",df['Age'].isnull().sum())#just age colum  er null value print korlam
age_avg=df['Age'].mean() ##/ .median() midle value calculate kore
print("Avarage null value is present of age:",age_avg)# age colum er gor value print hocca(meam() function)

df['Age'].fillna(age_avg,inplace=True) #?/( dataframe k directly update korce)avarage value dara null value gulo fill up kore dilam

print("Updated null value is present of age:",df['Age'].isnull().sum()) #punrai check korlam age colum er vitor null valu ace ki? nai

print(df.isnull().sum())
print(df.Sex)
# #conver sex data type to number
df['Sex']=df['Sex'].map({'male':'1','female':'0'})
print(df.Sex)

df.to_csv('d:\\Downloads\\test.csv',index=False)
print("Data cleaning compleated!")
# #modify data frame last Name/first name
# print(df['Name'] )
# df['LastName']=df['Name'].apply(lambda x:x.split(', ')[0])
# df['FastName']=df['Name'].apply(lambda x:x.split(', ')[1])
# print(df['FastName'] ) 
# print(df['LastName'] ) 
# print (df.head(11)) 





# #cabin colum  er null value  handle korbo
# print(df['Cabin'].mean())
# df['Cabin'].fillna(df['Cabin'].mean(),inplace=True)
# print(df['Cabin'].isnull().sum())

 

# print(df.columns)
# print(df.describe())# data k describe kore by value

#creating data frame
# df_empty=pd.DataFrame()
# print(df_empty.head())# create empty data frame


import pandas as pd
# Student_dict={
#     'Name':['Md Anik','Md Sazzad Hossain','Md Ashiqur Rahman','Nur Mohammad sweet'],
#     'Age':[22,23,24,25],
#     'Id':[24131144,24131153,24131132,24131122],
#     'Semester':['4th','4th','4th','4th'],
#     'Section':['D','D','D','D'],
#     'Dept':['CSE at VU','CSE at VU','CSE at VU','CSE at VU'],


# }
# df_student=pd.DataFrame(Student_dict) #data frame a convert kore debe
# print(df_student)
# print(df_student.describe())
 

# import pandas as pd

 
# num_students = int(input("How to student details stored?: "))

 
# names = []
# ages = []
# rolls = []

 
# for i in range(num_students):
#     print(f"\nStudent {i+1} information:")
#     name = input("Name: ")
#     age = int(input("Age: "))
#     roll = int(input("Roll: "))

#     names.append(name)
#     ages.append(age)
#     rolls.append(roll)

 
# student_dict = {
#     'Name': names,
#     'Age': ages,
#     'Roll': rolls
# }

 
# df_student = pd.DataFrame(student_dict)

 
# print("\n Student DataFrame:")
# print(df_student)




 


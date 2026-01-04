import numpy as np## use kora hoi large amount number of data quickly handle korar jonno
##using array;Benifits:less memory use
##use of numpy:

tempeature=np.array([32.5,31.8,33.0,35.2,36.6])
average=np.mean(tempeature)
print(average)


# ##1D Array:
# ar_1d=np.array([10,20,30,40,50])
# print(ar_1d)

# ##2D Array:
# arr_2d=np.array([[1,2,3,4],
#                  [5,6,7,8],
#                  [9,0,1,2]])
# print(arr_2d)

# ##Multidimention array/3D:

# ##matrix:
# matrix=np.array([[2,3,4],
#                  [5,6,7]])
# print(matrix)
 
# zeros_array=np.zeros((3,3))
# print(zeros_array)

# ones_array=np.ones((2,3))
# print(ones_array)

# print(np.full((3,3),7))

# print(np.arange(1,10,3)) #using sequential list

# print(np.eye(3))

## numpy array properties:

##shape:
# arr_2d=np.array([[1,2.4,3,4],
#                  [5,6.7,7,8],
#                  [9,0,1,2]])
# print(arr_2d.shape)
# #size:
# print(arr_2d.size)
# ##ndim:
# print(arr_2d.ndim)
# ##dtype:
# print(arr_2d.dtype)
# ##type change:
# int_arr=arr_2d.astype(int)
# print(int_arr)
# str_arr=arr_2d.astype(str)
# print(str_arr)

##array mumtiply/sub/add:
# print(arr_2d*2)
# print(arr_2d**2)
# print(arr_2d+2)
# print(arr_2d-2)

##agregation function:
""""
print(np.sum(arr_2d))
print(np.mean(arr_2d))
print(np.min(arr_2d))
print(np.max(arr_2d))
print(np.std(arr_2d))
print(np.var(arr_2d))
"""
#indexing/slicing:
# arr_2d=np.array([[1,2,3,4],
#                  [5,6,7,8],
#                  [9,0,1,2]])
# print(arr_2d[2,3])
# print(arr_2d[0:2,0:2])


##Array filtering:--------------------
import numpy as np

# arr = np.array([
#     [1, 6, 3],
#     [7, 5, 9]
# ])
# print(arr.shape[0])number of row 
# print(arr.shape[1])number of colum
 
# ধরো আমরা 5 খুঁজবো
# target = int(input("Enter target:"))
# found=False
# for i in range(arr.shape[0]):
#     for j in range(arr.shape[1]):
#         if arr[i][j]==target:
#             found=True
#             break
# if found==True:
#     print('found at index :',i,' ',j)   
# else:
#     print("Not found")      
# খুঁজে পাই কোথায় আছে (True/False matrix)
# result = np.where(arr == target)
# print('index:',result)
 
# if result[1].size > 0:
#     print(f"Element found: {target}")
#     print(f"Index: Row={result[0][0]}, Column={result[1][0]}")
# else:
#     print("Element not found.")

#-----------------------------------
#Reshaping------

# arr=np.array([1,2,3,4,5,6])

# reshape_arr=arr.reshape(2,3) #it does not create  copy
# print(reshape_arr[0,2])
# print(reshape_arr)

#------flatten-------copy return korbe
#------ravel-----copy return korbe na
#multidymention array k 1D te convert kore
# arr2D=np.array([[1,2,3],[4,5,6]])
# print(arr2D)
# arr2D.ravel()
# print(arr2D)

# print(arr2D)
# arr2D=arr2D.flatten()
# print(arr2D)
# arr2D=np.array([[1,2,3,4],
#               [5,6,7,8],
#               [9,0,1,2]])
# print(arr2D)
# print(np.insert(arr2D,3,[1,2,3,4],axis=0))#3 number row
# arr=np.array([1,2,3,4,5])# 1D array
# print(np.insert(arr,5,6))

# print(np.append(arr,[6,7,8])) #element add at the end
# list=[1,2,3,4,5]
# list.append(6)  ###for list
# print(list)
# list.insert(3,0)
# print(list)

###joind array
# arr1=np.array([[1,2,3,4],
#               [5,6,7,8],
#               [9,0,1,2]])
              
# # arr2=np.array([[1,2,3,4],
# #               [5,6,7,8],
# #               [9,0,1,2]])
# # newArr=np.concatenate((arr1,arr2))## (arr1,arr2)parameter a element gulo list/tuple a dite hbe
# # print(newArr)

# ##np.delete()--
# new_arr=np.delete(arr1,0,axis=0) #1st row deelete hbe
# print(new_arr)
"""vstack()->row wise
   hstack()->colum wise"""
# arr1=np.array([1,2,3])
# arr2=np.array([4,5,6])
# print(np.vstack((arr1,arr2)))
# print(np.hstack((arr1,arr2)))
"""split(),hsplit(),vsplit()"""
# arr1=np.array([1,2,3,4])
# print(np.split(arr1,2)) #array k 2 part a vag kore dilo
"""Broadcasting->different different array k shape performance kore without using loop
   mathametically operation kora jai easily   kono empty list create kora lage na  """
# prices=[100,200,300 ]
# discount=10
# final_prices=[]
# print(len(prices)) ##using loop
# for i in prices:
#     final_price=i-(i * discount/100)
#     final_prices.append(final_price)
# print(final_prices)  
#   
##using Broadcast verry important
# prices=np.array([100,200,300 ]) 
# discount=10
# final_prices=prices-(prices * discount/100)
    
# print(final_prices)
# 
#
# price=[100,200,300 ]
# delevery_charges=[10,20,30]
# print(price*2)   ##for list does not element calculate as  curresponding element
# print(price+delevery_charges)
# prices=np.array([100,200,300 ]) 

# print(prices*2) ##for array broad cast easily handle it
# result=[x-y  for x,y in zip(price,delevery_charges)]
# print(result)

# """for 2D array using broadcast"""
# matrix=np.array([[1,2,3],
#                  [4,5,6]])
# vector=np.array([10,20,30])
# result=matrix+vector
# print(result)
"""np.isnan(arr)->detected missing value return true 
   np.nan_to_num(arr,nan=value)->
   np.isinf(arr,posinf=100,neginf=100)
"""
# num=np.array([1,np.inf,2,3,np.nan,4,np.inf,5,6,6,np.nan])
# print(np.isnan(num))
# cleaned_arr=np.nan_to_num(num,nan=10)## handle it.defaule is 0;
# print(cleaned_arr)
# print(np.isinf(num))
# print(np.nan_to_num(num,posinf=1000,neginf=1000))##handle it infinitive value




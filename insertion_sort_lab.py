arr=[64,34,25,12,22,11,90]
n=len(arr)
for i in range(1,n):
    key=arr[i]
    j=i-1
    while j>=0 and arr[j]>key:
        arr[j+1]=arr[j]
        j=j-1
    arr[j+1] =key
print(f"Assending order: {arr}")       

for i in range(1, n):
    key = arr[i]
    j = i - 1
 
    while j >= 0 and arr[j] < key: #changing
        arr[j + 1] = arr[j]  #changing
        j -= 1
    arr[j + 1] = key

print(f"Descending order: {arr}")
# n=int(input("size:"))
# arr=[int(input())for i in range(n)] 
 
# arr=[5,4,6,7,2]
# n=len(arr)
# for i in range(0,n):
#     key=arr[i]
#     j=i-1
     
#     while j>=0 and arr[j]>key:
#         arr[j+1]=arr[j]
       
#         j=j-1
        
#     arr[j+1] =key
#     print(f"After inserting{key}:{arr[:i+1]}")
#     print(f"Assending order{arr}")
    # print(f"After inserting{key}:{arr[:i+1]}")
    # print("After inserting iteration",i)
    # k=0
    # for k in range(i) :
    #     print(arr[k], end=" ")
    # print("\n") 
    
    
# print(f"Assending order: {arr}")
 
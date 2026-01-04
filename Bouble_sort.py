arr=[64,3,25,12,22,11,90]
n=len(arr)
for i in range(n-1):
    for j in range(n-1-i):
        if arr[j]>arr[j+1]:
          arr[j+1],arr[j]=arr[j],arr[j+1] #swaping 
print("Assending order:",arr)   



for i in range(n-1):
    for j in range(n-1-i):
        if arr[j]<arr[j+1]:
          arr[j+1],arr[j]=arr[j],arr[j+1] #swaping 
print("Descending order:",arr)           


arr=[15,18,20,3,6,12]

while True:
    target=int(input('Enter target value:'))
    low,high=0,len(arr)-1
   
    found=False

    while low<=high:
      
      mid=(low+high)//2
     
      if arr[mid]==target:
         found=True
         break
         
      if arr[low] == arr[mid] == arr[high]: ##for duplicate valu handle it
         low += 1
         print("yes")
         high -= 1  
    

      elif arr[low]<=arr[mid]:# left sorted

        if arr[low]<=target<arr[mid]:
            high=mid-1
        else:
            low=mid+1    
      else:           #right sorted
        if arr[mid]<target<=arr[high]:
            low=mid+1
        else:
            high=mid-1
    if found==True:
      print(f"{target} is found at index: {mid}")
      break
    else:  
      print(f"{target} value is not found please try again..")            


        







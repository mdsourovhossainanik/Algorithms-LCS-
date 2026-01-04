
import math
n=int(input())
 
sum=0
if n==0 or n==1:
    print("-1")
    exit(0)
     

for i in range(2,n+1): 
    sum+=math.log10(i)
    print(int(sum))
print("digit=",int(sum+1))   
#time and space complexity koto? 
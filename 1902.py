t=int(input())
result=[]
while t:
    
    n=int(input())
    s=input()[:n]
    
    if '0'in s and '1' in s:
       result.append("YES")
    
    elif '0'in s:
       result.append("YES")
    else:
       result.append("NO")   
    t-=1  
for i in result:
    print(i)         
    
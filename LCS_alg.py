import numpy as np
def lcs_length(x,y):
    m=len(x)
    n=len(y)
    dp = np.zeros((m+1, n+1),dtype=int) 
    lcs=[]
    for i in range(1, m+1):
        
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                 dp[i, j] = 1 + dp[i-1, j-1] #diagonal
            else:
                 dp[i, j] = max(dp[i-1, j], dp[i, j-1])  
    print(dp)
    i, j = m, n
    
   
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            lcs.append(x[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1, j] > dp[i, j - 1]:  
            i -= 1
        else:
            j -= 1  
    lcs.reverse()              
    return dp[m, n],lcs
   
        
x=input("1st string:")
y=input("2nd string:")
 
n,lcs=lcs_length(x,y)
print("LCS length:",n)
print(''.join(lcs))
 
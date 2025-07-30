
    Return dp[m][n]
"""


import numpy as np
def lcs_length(x,y):
    m=len(x)
    n=len(y)
    dp = np.zeros((m+1, n+1),dtype=int) #2D matrix nilam

    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                dp[i, j] = 1 + dp[i-1, j-1]# diagonal element er sate 1 add korbo
            else:
                dp[i, j] = max(dp[i-1, j], dp[i, j-1]) # compare left and upper value then maximum ta nibo

    return dp[m, n]
x=input("1st string:")
y=input("2nd string:")
print("LCS length:",lcs_length(x,y))

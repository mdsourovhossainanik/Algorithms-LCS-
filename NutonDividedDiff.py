import pandas as pd
import numpy as np
 
def v(i,val,x):
    prod=1
    for j in range(i):
        prod*=(val-x[j])
    return prod
def newton_divided_diff(x,y,val):
    n=len(x)
    table=np.full((n,n+1),None,dtype=float) #create a 2D table initialize value null
 
    
    for i in range(n):
        table[i,0]=x[i]
        table[i,1]=y[i]

    for j in range(2,n+1):#colum
        for i in range(n-j+1):#row 
           table[i,j]=(table[i+1,j-1]-table[i,j-1]) / (x[i+j-1] - x[i])
            
    col_names=[ ] 
    for i in range(n+1):
        if i==0 :
            col_names.append("X")
        elif i==1:
            col_names.append("Y")
        else:
            col_names.append(f"D^{i-1}y")    
    #col_names = ["X" if i==0 else "Y" if i==1 else f"D^{i-1}y" for i in range(n+1)] #sortversion
           
    df=pd.DataFrame(table,columns=col_names)

    print("By using newton divided diff interpolation:\n")
    print( df.round(4).fillna(""))
    
    result = table[0, 1]
    for i in range(1, n):
        result += table[0, i+1] * v(i, val, x)
        
    print(f"\nApproximate result at point {val} is:{result:.5f}")
    return None    
x=[2,2.3,2.6,2.9,3.2]
y=[0.85467,0.75682,0.431126,0.22364,0.08567]
val=2.8
newton_divided_diff(x,y,val)
 
 
 
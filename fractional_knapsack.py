import pandas as pd
def fractional_knapsack(value,weight,capacity):
     
   
    items=[(value[i],weight[i],value[i]/weight[i]) for i in range(len(value))]
    col_names=["price","weight","ratio"]
    df=pd.DataFrame(items,columns=col_names,dtype=float)
    print(df)
    item_sorted=sorted(items,key=lambda item:item[2],reverse=True)
   
   
    total_value=0
    for v,w,ratio in item_sorted:
        if capacity>=w:
            capacity-=w
            total_value+=v
        else:
            total_value+=ratio*capacity
            break
    return items,total_value
product_no=int(input("Number of product:"))
value=[]
weight=[]
for i in range(product_no):
    print(f"\nproduct_no->>{i+1}:")
    v,w=map(float,input("price_and_weight=").split())
    value.append(v),weight.append(w)
capacity=float(input("Enter Maximum Capacity="))    
items,result=fractional_knapsack(value,weight,capacity)  
print(f"Maximum profit={result:.2f}")    
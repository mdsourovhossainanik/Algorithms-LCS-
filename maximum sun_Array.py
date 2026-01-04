a = [-2, 3, 0, -1, 5, -3, 2, 2, -5, 4] 
n=len(a)
max_sum=-2**31
# print (max_sum)
curr_sum=0
start=0
end=0
s=0
for i in range(n):
    # print("pass:",i)
    curr_sum=curr_sum+a[i]
    if curr_sum > max_sum:
        max_sum = curr_sum
        start=s
        # print("  start index changing:",start)
        end=i
        # print("  end index chainging:",i)
    if curr_sum<0:
        curr_sum=0
        s=i+1
        
print (f"Maximum profit={max_sum}")  
print(f"Start index(buy day)={start}")      
print(f"End index(sell day)={end}")  
print("Subarray:", a[start:end+1])


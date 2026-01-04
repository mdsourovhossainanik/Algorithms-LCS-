
"""লিস্টে কোনো element-এর index খুঁজতে হলে index() মেথড ব্যবহার করতে হয়।
list.index() → linear search ব্যবহার করে"""
#1. linear search:
# arr = [10, 20, 30, 20, 40]

# print(arr.index(20))   # 1 (first occurrence)

#2.Binary search:(bisect method)
"""Python-এ bisect মডিউল মূলত sorted list-এ fast searching ও insertion 
এর জন্য ব্যবহার হয়। এটি binary search principle ব্যবহার করে,
 তাই O(log n) time complexity হয়।"""

"""Main Functions in bisect

bisect.bisect_left(list, x)

Sorted list-এ x কোথায় insert করতে হবে সেটা দেয়, existing element-এর
 বাম দিকে।

Element থাকলে তার left-most index রিটার্ন করে।

bisect.bisect_right(list, x) / bisect.bisect(list, x)

x কোথায় insert হবে সেটা দেয়, existing element-এর ডান দিকে।

Element থাকলে তার right-most index রিটার্ন করে।

bisect.insort_left(list, x)

Sorted list-এ x insert করে, left-most position এ।

bisect.insort_right(list, x) / insort()

Sorted list-এ x insert করে, right-most position এ।"""

import bisect

arr = [2, 5, 6, 6,10]
target = 6
# left_index= bisect.bisect_left(arr, target) #most right occerence dibe
index = bisect.bisect(arr, target)-1 #most right occerence dibe
print("Found at index:", index)
if index < len(arr) and arr[index] == target:
    print("Found at index:", index)
else:
    print("Not found")

# #Insertion in-sorted list
# import bisect

# arr = [1, 3, 4, 4, 7]

# # Insert 4 at left-most position
# bisect.insort_left(arr, 5)
# print(arr)  # [1, 3, 4, 4, 4, 7]

# # Insert 5 at right-most position
# bisect.insort_right(arr, 8)
# print(arr)  # [1, 3, 4, 4, 4, 5, 7]

#2.bisect.bisect_left(list, x, lo=0, hi=len(list))
# x কোথায় insert করলে left-most position হবে সেটা দেয়।
# যদি element already থাকে → left-most index।
import bisect

arr = [1, 3, 4, 4, 7]
# print(bisect.bisect_left(arr, 2))  # 2


#3. bisect.bisect_right(list, x, lo=0, hi=len(list))
# x কোথায় insert করলে right-most position হবে সেটা দেয়।
# যদি element already থাকে → right-most index।
# Alias: bisect.bisect()
# print(bisect.bisect_right(arr, 4))  # 4
# print(bisect.bisect(arr, 4))        # 4

# #4.3️⃣ bisect.insort_left(list, x, lo=0, hi=len(list))
# # Sorted list-এ left-most position এ x insert করে।
# # List sorted থাকে।
# bisect.insort_left(arr, 4)
# print(arr)  # [1, 3, 4, 4, 4, 7]







#3. Hash Table (Dictionary / Set) 
# Condition: Data sorted না-ও থাকতে পারে

 



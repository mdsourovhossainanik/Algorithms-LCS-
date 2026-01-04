import heapq

arr = [50, 40, 10, 30, 20, 60]
print("Before heapify:", arr)      

heapq.heapify(arr)
print("After heapify:", arr)#min heap

heapq.heappush(arr,5)
print(f"before inser 5 element:{arr}")

heapq.heappush(arr,70)
print(f"before inser 70 element:{arr}")

min_item=heapq.heappop(arr)
print(f"min item:{min_item}")

# print ("remaining heap",arr)

#max heap-->
# nums = [10, 50, 20]
# max_heap = [-x for x in nums] 
# print("Before:",max_heap)

# heapq.heapify(max_heap)
# print("after",nums)

# # Pop max
# print(-heapq.heappop(max_heap))  # Output: 50





"""| Function                 | কাজ                                       |
| ------------------------ | ----------------------------------------- |
| `heapify(list)`          | লিস্টকে হিপে রূপান্তর করে (Min Heap)      |
| `heappush(heap, val)`    | হিপে মান যোগ করে                          |
| `heappop(heap)`          | হিপ থেকে সর্বনিম্ন মান সরিয়ে রিটার্ন করে  |
| `heappushpop(heap, val)` | নতুন মান যোগ করে এবং সঙ্গে সঙ্গে মিন সরায় |
| `heapreplace(heap, val)` | মিন সরায় → নতুন মান যোগ করে (একসাথে)      |
| `nlargest(n, iterable)`  | সবচেয়ে বড় `n`টি মান দেয়                   |
| `nsmallest(n, iterable)` | সবচেয়ে ছোট `n`টি মান দেয়                  |
"""


# Simple Kruskal's Algorithm (No classes, minimal code)
""" find function এই ফাংশনটা বলে দেয় node u কোন set-এর মধ্যে আছে,অর্থাৎ তার “ultimate parent” কে।যদি parent[u] == u, তাহলে সে নিজেই root।নইলে recursion 
করে তার parent-এর parent খুঁজে root বের করে।এটা দিয়ে cycle আছে কিনা বোঝা যায়।"""
def find(u, parent): 
  
    if parent[u] == u:
        # print ("root:",u)
        return u #this is untimate parent /root nood
    return find(parent[u], parent) 
    # parent[u]=find(parent[u], parent) #if ata koti path compression hobeparent update হবে — প্রত্যেক node কে সরাসরি root-এর child বানানো হবে।
    # return parent[u]
# Union two sets"""
"""এটা দুইটা set (যাদের root আলাদা) কে এক করে দেয়।কাজ:দুই node-এর root বের করো → pu, pv
যদি আলাদা হয় → একসাথে merge করো nion by Rank:ছোট tree-টাকে বড় tree-এর নিচে রাখোযেন future-এ find() দ্রুত কাজ করে।"""

def union(u, v, parent, rank): 
    pu = find(u, parent) #find ultimate parent
    pv = find(v, parent)
    # print(pu,pv)
    if pu != pv:
        if rank[pu] < rank[pv]:
            parent[pu] = pv
        elif rank[pu] > rank[pv]:
            parent[pv] = pu
        else:
            parent[pv] = pu #jekono akta dilei hbe
            rank[pu] += 1

def kruskal(V, edges):
    # Sort edges by weight
    edges=sorted(edges,key=lambda x: x[2])
    print(edges)

    parent = [i for i in range(V)]# index k parent node dhore cnsider[0,1,2,3] ecch node rank initially 0
    print ("parent node compare index:",parent)
    rank = [0] * V #initialy 0 set korce for each node
    
    print("rank each node:",rank)
    cost = 0  
    

    for u, v, wt in edges:# # Sort edges by weight er upo loop chalacci u=edge er first node and v=2nd node
        
        if find(u, parent) != find(v, parent): #jdi 2 ta node er root diffrent hoi tahole add koro same set a otherwise noo adding
            print("selected node:",u,v,parent)
            # print ("root for selected node: ",find(u, parent) ,find(v, parent) )
            cost += wt
            union(u, v, parent, rank)

    return cost
 
 
 
V = 9

#(u,v,w) for each node
edges = [
        (0, 1, 3),
        (1, 2, 4),
        (5, 6, 15),
        (3, 4, 5),
        (7, 8, 17),
        (3,6,20),
        (4,6,25)
    ]

mst_cost = kruskal(V, edges)
print("Total cost of MST:", mst_cost)








"""1.সব edges-কে তাদের weight অনুযায়ী sort করা হয় (ছোট থেকে বড়)।

   2.ছোট weight-এর edge গুলো এক এক করে যোগ করা হয়, যদি তা cycle না তৈরি করে।

   3.যতক্ষণ না সব nodes connected হয়, ততক্ষণ কাজ চলে।
     
   usecase-->যখন গ্রাফে node অনেক, কিন্তু edge (সংযোগ) তুলনামূলকভাবে কম থাকে।  """ 
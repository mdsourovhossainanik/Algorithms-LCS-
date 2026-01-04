# # LAN (Local Area Network) design using Kruskal's Algorithm
# # ----------------------------------------------------------

# def find(u, parent):
#     # Path Compression
#     if parent[u] != u:
#         parent[u] = find(parent[u], parent)
#     return parent[u]

# def union(u, v, parent, rank):
#     pu = find(u, parent)
#     pv = find(v, parent)
#     if pu != pv:
#         if rank[pu] < rank[pv]:
#             parent[pu] = pv
#         elif rank[pu] > rank[pv]:
#             parent[pv] = pu
#         else:
#             parent[pv] = pu
#             rank[pu] += 1

# def kruskal(V, edges):
#     # Sort all edges by their weight (cost)
#     edges.sort(key=lambda x: x[2])
    
#     parent = [i for i in range(V)]
#     rank = [0] * V
#     mst_cost = 0
#     mst_edges = []
    
#     for u, v, w in edges:
#         if find(u, parent) != find(v, parent):
#             union(u, v, parent, rank)
#             mst_cost += w
#             mst_edges.append((u, v, w))
    
#     return mst_cost, mst_edges


# # Example LAN setup (Computers and cable costs)
# # 6 computers (0–5)
# # edges = (computer1, computer2, cost)
# edges = [
#     (0, 1, 4),   
#     (0, 2, 3),
#     (1, 2, 1),
#     (1, 3, 2),
#     (2, 3, 4),
#     (3, 4, 2),
#     (4, 5, 6)
# ]

# V = 6  # total computers (nodes)

# total_cost, lan_network = kruskal(V, edges)

# print("Minimum Cost LAN Network (Using Kruskal's Algorithm):")
# for u, v, w in lan_network:
#     print(f"Connect Computer {u} ↔ {v} with cable cost {w}")
# print("Total Minimum Cable Cost:", total_cost)




"""NetworkX হলো একটা graph handling library —
যেটা দিয়ে তুমি graph (node + edge) তৈরি, বিশ্লেষণ,
এবং বিভিন্ন algorithm (যেমন Kruskal, Dijkstra, BFS, DFS ইত্যাদি) চালাতে পারো।"""
import networkx as nx 

# Graph তৈরি
G = nx.Graph()
 
# Node ও Edge যোগ
G.add_weighted_edges_from([
    (0, 1, 4),   
    (0, 2, 3),
    (1, 2, 1),
    (1, 3, 2),
    (2, 3, 4),
    (3, 4, 2),
    (4, 5, 6)
])

# MST বের করা
mst = nx.minimum_spanning_tree(G, algorithm='kruskal')
print(mst)
total_cost=0
print("Minimum Spanning Tree edges:")
for u, v, data in mst.edges(data=True):
    total_cost+=data['weight']
    print(f"{u} ↔ {v}  (weight = {data['weight']})")
print("Total Minimum Cable Cost:", total_cost)

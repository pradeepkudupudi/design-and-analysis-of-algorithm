# Union-Find helper functions
def find(parent, i):
    if parent[i] == i:
        return i
    else:
        return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

# Number of vertices and edges
n = 4
m = 5
# Edge list with weights
edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
# Given MST
given_mst = [(2, 3, 4), (0, 3, 5), (0, 1, 10)]

# Calculate the total weight of the given MST
given_mst_weight = sum(weight for u, v, weight in given_mst)

# Sort edges based on their weight
edges.sort(key=lambda edge: edge[2])

# Initialize union-find structure
parent = [i for i in range(n)]
rank = [0] * n

# Initialize MST and its total weight
mst = []
total_weight = 0

# Iterate through sorted edges and apply Kruskal's Algorithm
for edge in edges:
    u, v, w = edge
    if find(parent, u) != find(parent, v):
        union(parent, rank, u, v)
        mst.append(edge)
        total_weight += w

# Check if the given MST is unique
is_unique = given_mst_weight == total_weight

# Output the result
print("Is the given MST unique?", is_unique)
if not is_unique:
    print("Another possible MST:", mst)

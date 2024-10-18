import itertools

cities = ['A', 'B', 'C']
distances = {
    ('A', 'B'): 10,
    ('A', 'C'): 15,
    ('B', 'C'): 20,
}

min_distance = float('inf')
best_route = None

for perm in itertools.permutations(cities):
    current_distance = sum(distances.get((perm[i], perm[(i + 1) % len(perm)]), 0) for i in range(len(perm)))
    if current_distance < min_distance:
        min_distance = current_distance
        best_route = perm

print("Best route:", best_route)
print("Minimum distance:", min_distance)

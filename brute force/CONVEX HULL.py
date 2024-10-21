points = [(0, 0), (1, 1), (2, 2), (0, 2), (1, 0), (2, 0), (1, 2)]

hull = []
p = min(points)

while True:
    hull.append(p)
    q = points[0]
    for r in points:
        if q == p or (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1]) < 0:
            q = r
    p = q
    if p == hull[0]:
        break

print("Convex Hull:", hull)

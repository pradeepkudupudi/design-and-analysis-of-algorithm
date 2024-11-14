import sys
N = 5

graph = [
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 20],
    [20, 25, 30, 0, 15],
    [25, 30, 20, 15, 0]
]

dp = [[sys.maxsize] * (1 << N) for _ in range(N)]
dp[0][1] = 0 
for visited in range(1 << N):
    for pos in range(N):
        if visited & (1 << pos): 
            for city in range(N):
                if not visited & (1 << city): 
                    new_visited = visited | (1 << city)
                    dp[city][new_visited] = min(dp[city][new_visited], dp[pos][visited] + graph[pos][city])

min_path_distance = sys.maxsize
for pos in range(1, N):
    min_path_distance = min(min_path_distance, dp[pos][(1 << N) - 1] + graph[pos][0])

print("Minimum path distance:", min_path_distance)

n = 3
line1 = [5, 9, 3]
line2 = [6, 8, 4]
line3 = [7, 6, 5]
transfer = [
    [0, 2, 3],
    [2, 0, 4],
    [3, 4, 0]
]
dependencies = [(0, 1), (1, 2)]

dp1 = [0] * n  
dp2 = [0] * n 
dp3 = [0] * n  
dp1[0] = line1[0]
dp2[0] = line2[0]
dp3[0] = line3[0]
for i in range(1, n):
    dp1[i] = min(dp1[i - 1] + line1[i], dp2[i - 1] + transfer[1][0] + line1[i], dp3[i - 1] + transfer[2][0] + line1[i])

    dp2[i] = min(dp2[i - 1] + line2[i], dp1[i - 1] + transfer[0][1] + line2[i], dp3[i - 1] + transfer[2][1] + line2[i])

    dp3[i] = min(dp3[i - 1] + line3[i], dp1[i - 1] + transfer[0][2] + line3[i], dp2[i - 1] + transfer[1][2] + line3[i])

result = min(dp1[n - 1], dp2[n - 1], dp3[n - 1])

print("The minimum total production time is:", result)

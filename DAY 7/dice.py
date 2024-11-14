num_sides = 6
num_dice = 2
target_sum = 7
dp = [[0] * (target_sum + 1) for _ in range(num_dice + 1)]
dp[0][0] = 1
for dice in range(1, num_dice + 1):
    for sum_value in range(1, target_sum + 1):
        dp[dice][sum_value] = sum(dp[dice - 1][sum_value - face] for face in range(1, num_sides + 1) if sum_value - face >= 0)

result = dp[num_dice][target_sum]

print("Number of ways to achieve the target sum:", result)

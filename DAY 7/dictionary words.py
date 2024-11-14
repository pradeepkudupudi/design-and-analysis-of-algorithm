s = "ilikesamsung"  # Example input string
wordDict = {"i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go", "mango"}  # Example dictionary

dp = [False] * (len(s) + 1)
dp[0] = True  
for i in range(1, len(s) + 1):
    for j in range(i):
        if dp[j] and s[j:i] in wordDict:
            dp[i] = True
            break
if dp[len(s)]:
    print("Yes")
else:
    print("No")

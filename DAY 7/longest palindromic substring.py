s = "babad"  
start, max_len = 0, 1

for i in range(len(s)):
    for left, right in [(i, i), (i, i + 1)]:  
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > max_len:
                start, max_len = left, right - left + 1
            left -= 1
            right += 1

print("Longest Palindromic Substring:", s[start:start + max_len])

words = ["apple"]  
prefix_suffix_map = {} 
for i, word in enumerate(words):
    for prefix_len in range(len(word) + 1):  
        for suffix_len in range(len(word) + 1): 
            prefix = word[:prefix_len]  
            suffix = word[len(word) - suffix_len:]  
            key = (prefix, suffix)
            prefix_suffix_map[key] = i  

pref = "a" 
suff = "e"  
if (pref, suff) in prefix_suffix_map:
    print(prefix_suffix_map[(pref, suff)])  
else:
    print(-1)  

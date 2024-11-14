n = 4  

a1 = [4, 5, 3, 2]  
a2 = [2, 10, 1, 4]  

t1 = [0, 7, 4, 5]
t2 = [0, 9, 2, 8]    

e1, e2 = 10, 12     
x1, x2 = 18, 7       

f1 = [0] * n 
f2 = [0] * n  
f1[0] = e1 + a1[0]
f2[0] = e2 + a2[0]
for i in range(1, n):
    f1[i] = min(f1[i - 1] + a1[i], f2[i - 1] + t2[i] + a1[i])
    f2[i] = min(f2[i - 1] + a2[i], f1[i - 1] + t1[i] + a2[i])
result = min(f1[n - 1] + x1, f2[n - 1] + x2)

print("The minimum time required to process the product is:", result)

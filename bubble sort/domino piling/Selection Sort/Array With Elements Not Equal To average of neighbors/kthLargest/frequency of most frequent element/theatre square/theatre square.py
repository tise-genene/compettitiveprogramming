a, b, c = map(int,input().split()) 
 
if b%c == 0: 
    res1 = b//c 
else: 
    res1 = b//c+1 
 
if a%c == 0: 
    res2 = a//c 
else: 
    res2 = a//c+1 
 
print(res1*res2) 

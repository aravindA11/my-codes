from collections import defaultdict 
a=input()
n = len(a)  
dist = len(set([b for b in a])) 
co = defaultdict(lambda: 0) 
count = 0
s = 0
mi = n  
for j in range(n): 
    co[a[j]] += 1
    if co[a[j]] == 1: 
        count += 1
    if count == dist: 
        while co[a[s]] > 1: 
            if co[a[s]] > 1: 
                co[a[s]] -= 1
            s += 1
        le = j - s + 1	
        if mi > le: 
            mi = le 
            si = s 
print(len(str(a[si: si +mi]))) 

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    r, s = sys.stdin.readline().split()
    r = int(r)
    p = ""
    
    for char in s:
        p += char *r
        
    print(p)
    
    
    
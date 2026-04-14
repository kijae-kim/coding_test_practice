import sys

# H 호텔의 층수 W 각 층 방 수 N 손님
t = int(sys.stdin.readline())

for _ in range(t):
    h,w,n = map(int, sys.stdin.readline().split())
    
    floor = n%h
    
    room = (n // h) +1
    
    if floor == 0:
        floor = h
        room = n // h
    print(f"{floor}{room:02d}")

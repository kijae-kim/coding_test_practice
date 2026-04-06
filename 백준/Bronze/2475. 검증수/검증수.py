import sys
nums=list(map(int,sys.stdin.readline().split()))

total=0
for n in nums:
    total += n**2
print(total%10)
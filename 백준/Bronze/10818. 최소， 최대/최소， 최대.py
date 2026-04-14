import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

min_value = min(nums)
max_value = max(nums)

print(min_value, max_value)
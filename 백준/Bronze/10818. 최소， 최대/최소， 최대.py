import sys

n = int(sys.stdin.readline())
numbers = list(map(int,sys.stdin.readline().split()))

min_value = min(numbers)
max_value = max(numbers)

print(min_value, max_value)
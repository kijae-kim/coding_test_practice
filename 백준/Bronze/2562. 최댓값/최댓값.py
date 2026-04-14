import sys

numbers=[]
for _ in range(9):
    numbers.append(int(sys.stdin.readline()))
    
max_value = max(numbers)

max_idx = numbers.index(max_value) +1

print(max_value)
print(max_idx)
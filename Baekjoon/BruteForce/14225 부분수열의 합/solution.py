import sys
from itertools import combinations

n = int(sys.stdin.readline())

s = list(map(int, sys.stdin.readline().split()))

numbers = []

for num in range(1, n + 1):
    case_list = combinations(s, num)
    for case in case_list:
        numbers.append(sum(case))

numbers = set(numbers)

num = 1
while True:
    if num not in numbers:
        break
    num += 1

print(num)
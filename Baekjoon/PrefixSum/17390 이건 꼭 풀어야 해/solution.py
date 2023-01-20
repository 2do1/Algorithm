import sys

n, q = map(int, sys.stdin.readline().split())

a = sorted(map(int, sys.stdin.readline().split()))

prefix_sums = [0]
prefix_sum = 0

for num in a:
    prefix_sum += num
    prefix_sums.append(prefix_sum)

for _ in range(q):
    l, r = map(int, sys.stdin.readline().split())

    print(prefix_sums[r] - prefix_sums[l - 1])
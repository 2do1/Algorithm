import sys

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

prefix_sums = [0]
prefix_sum = 0
for num in nums:
    prefix_sum += num
    prefix_sums.append(prefix_sum)

m = int(sys.stdin.readline())
for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())

    print(prefix_sums[j] - prefix_sums[i - 1])
import sys

n, m = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))

prefix_sums = [0]
prefix_sum = 0
for num in nums:
    prefix_sum += num
    prefix_sums.append(prefix_sum)

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())

    print(prefix_sums[j] - prefix_sums[i - 1])

# 처음 풀이
# import sys

# n, m = map(int, sys.stdin.readline().split())

# nums = list(map(int, sys.stdin.readline().split()))

# prefix_sums = []
# prefix_sum = 0
# for num in nums:
#     prefix_sum += num
#     prefix_sums.append(prefix_sum)

# for _ in range(m):
#     i, j = map(int, sys.stdin.readline().split())

#     if i == 1:
#         print(prefix_sums[j - 1])
#     else:
#         print(prefix_sums[j - 1] - prefix_sums[i - 2])
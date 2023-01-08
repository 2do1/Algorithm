import sys
MIN_NUM = -10001

while True:
    t = int(sys.stdin.readline())

    if not t:
        break

    profit = [int(sys.stdin.readline()) for _ in range(t)]

    for index in range(1, t):
        profit[index] = max(profit[index], profit[index - 1] + profit[index])

    print(max(profit))   
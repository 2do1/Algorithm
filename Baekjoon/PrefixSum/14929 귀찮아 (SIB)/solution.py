n = int(input())

x_list = list(map(int, input().split()))

answer = 0
prefix_sum = 0
for i in range(len(x_list) - 1, 0, -1):
    prefix_sum += x_list[i]
    answer += x_list[i - 1] * prefix_sum

print(answer)
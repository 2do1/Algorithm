n = int(input()) # 양의 실수들의 개수 n

num_list = [float(input()) for _ in range(n)] # 실수들

for i in range(1, n):
    num_list[i] = max(num_list[i], num_list[i] * num_list[i - 1])

print("{:.3f}".format(max(num_list)))
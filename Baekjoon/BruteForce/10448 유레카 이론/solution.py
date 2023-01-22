def find(num):
    for i in range(len(triangle_num)):
        for j in range(i, len(triangle_num)):
            for k in range(j, len(triangle_num)):
                if triangle_num[i] + triangle_num[j] + triangle_num[k] == num:
                    return 1
    return 0

t = int(input())

triangle_num = [num * (num + 1) // 2 for num in range(1, 46)]

for _ in range(t):
    num = int(input())

    print(find(num))
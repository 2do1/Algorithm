n, l = map(int, input().split()) # 상자의 개수 n, 상자의 사이즈 L

x_list = list(map(int, input().split()))

total = 0
is_stable = True

for index in range(n - 1, -1, -1):
    total += x_list[index]
    center = total / (n - index)

    if center >= x_list[index - 1] + l or center <= x_list[index - 1] - l:
        is_stable = False

if is_stable:
    print("stable")
else:
    print("unstable")
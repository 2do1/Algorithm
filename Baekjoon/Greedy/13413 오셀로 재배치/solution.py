t = int(input())

for _ in range(t):
    n = int(input())

    init = input()
    goal = input()

    white_count = 0
    black_count = 0
    for index in range(n):
        if init[index] != goal[index]:
            if init[index] == "B":
                white_count += 1
            else:
                black_count += 1
    
    print(max(white_count, black_count))
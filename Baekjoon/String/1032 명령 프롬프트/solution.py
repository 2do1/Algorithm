n = int(input())
first_file = list(input())

for _ in range(n - 1):
    file = input()
    for index in range(len(first_file)):
        if first_file[index] != file[index]: # 같지 않은 경우
            first_file[index] = "?"

answer = "".join(first_file)
print(answer)
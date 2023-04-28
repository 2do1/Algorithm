t = int(input())


for _ in range(t):
    n = int(input())

    clothes = dict()

    for _ in range(n):
        name, kind = input().split()

        if kind in clothes.keys(): # 종류가 이미 있을 경우
            clothes[kind].append(name)
        else:
            clothes[kind] = [name]

    answer = 1 # 가능한 모든 경우의 수 
    for value in clothes.values():
        answer *= (len(value) + 1) # 안입는 경우의 수 까지
    
    answer -= 1 # 어느것도 선택하지 않는 경우의 수는 제외
    print(answer)
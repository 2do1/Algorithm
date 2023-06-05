t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    while True:
        if a > b:
            a //= 2

        elif b > a:
            b //= 2
        
        else: # a == b 일 경우, # 두 노드의 부모 노드가 같다면
            print(b * 10)
            break
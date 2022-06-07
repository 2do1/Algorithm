# 명령어 4개 존재
# 1: 전구 켜져 있음, 0: 전구 꺼져 있음

# n: 전구의 개수, m: 입력되는 명령어 개수
n, m = map(int, input().split())

bulb_list = list(map(int, input().split())) # 전구들의 상태를 담아놓은 리스트

for _ in range(m): # 명령어 입력 받기
    # a: a번째 명령어, (b, c): (i,x) or (l, r)
    a, b, c = map(int, input().split()) 

    if a == 1: # 1번째 명령어일 경우
        bulb_list[b-1] = c
    elif a == 2: # 2번째 명령어일 경우
        for i in range(b-1, c):
            if bulb_list[i] == 1: # 전구가 켜져 있을 경우
                bulb_list[i] = 0 # 전구를 끈다
            else: # 전구가 꺼져 있을 경우
                bulb_list[i] = 1 # 전구를 켠다.
    elif a == 3: # 3번째 명령어일 경우
        # for i in range(b-1, c):
        #     bulb_list[i] = 0
        bulb_list[b-1:c] = [0] * (c - b + 1)
    elif a == 4: # 4번째 명령어일 경우
        # for i in range(b-1, c):
        #     bulb_list[i] = 1
        bulb_list[b-1:c] = [1] * (c - b + 1)

for bulb in bulb_list:
    print(bulb, end=" ")
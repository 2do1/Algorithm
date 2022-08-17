t = int(input()) # 테스트케이스 개수

for _ in range(t):
    n = int(input()) # 수첩 1에 적혀 있는 정수의 개수
    note1_set = set(map(int, input().split())) # 수첩 1에 적혀있는 정수들
    
    m = int(input()) # 수첩 2에 적혀있는 정수의 개수
    note2_list = list(map(int, input().split())) # 수첩 2에 적혀있는 정수들

    for num in note2_list:
        if num in note1_set: # 수첩 1에 있으면
            print(1)
        else: # 수첩 1에 없으면
            print(0)
n = int(input()) # n개의 정수
a_list = sorted(map(int, input().split())) # 정렬

m = int(input()) # m개의 수, 이 수들이 A안에 존재하는지의 여부
m_list = list(map(int, input().split()))


for m in m_list:
    start = 0 
    end = len(a_list) - 1
    is_exist = False # A안에 존재하는지의 여부

    while start <= end:
        mid = (start + end) // 2
        
        if a_list[mid] == m: # a안에 존재할 경우
            is_exist = True
            break
        elif a_list[mid] > m: # 찾는 수보다 값이 클 경우
            end = mid - 1
        else: # 찾는 수보다 값이 작을 경우
            start = mid + 1
    
    if is_exist: # a안에 존재할 경우
        print(1)
    else: # a안에 존재하지 않을 경우
        print(0)
while True:
    num = input() # 주행 거리계에 적혀있는 수
    num_len = len(num) # 몇자리 숫자
    
    if num == "0": # 마지막 입력일 경우
        break
    elif num == num[::-1]: # 이미 팰린드롬일 경우
        print(0)
        continue

    answer = 0 # 팰린드롬이 되기 위해 주행해야 하는 최소 거리
    num = int(num) # 숫자형으로 변환
    while True:        
        answer += 1
        num += 1
        str_num = (num_len - len(str(num))) * '0' + str(num) # 앞에 0이 있는 경우
        if str_num == str_num[::-1]: # 팰린드롬일 경우
            print(answer)
            break

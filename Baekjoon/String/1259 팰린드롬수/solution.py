while True:
    num = input() # 입력받은 수
    if num == "0": # 입력 마지막 줄일 경우
        break
    else:
        if num == num[::-1]: # 팰린드롬수일 경우
            print("yes")
        else: # 팰린드롬수가 아닐 경우
            print("no")
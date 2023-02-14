switch_count = int(input())

switches = list(map(int, input().split()))

students_count = int(input())

for _ in range(students_count):
    gender, switch_num = map(int, input().split())

    if gender == 1: # 남자일 경우
        # index = 1
        # while switch_num <= switch_count:
        #     if switches[switch_num - 1] == 0:
        #         switches[switch_num - 1] = 1
        #     else:
        #         switches[switch_num - 1] = 0
        #     index += 1
        #     switch_num *= index

        for index in range(switch_num, switch_count + 1, switch_num):
            if switches[index - 1] == 0:
                switches[index - 1] = 1
            else:
                switches[index - 1] = 0

    elif gender == 2: # 여자일 경우
        # index = 1
        # while True:
        #     if switches[switch_num - index - 1:switch_num + index] != switches[switch_num - index - 1:switch_num + index][::-1]: # 대칭이 아닐 경우
        #         index -= 1
        #         break

        #     index += 1

        #     if switch_num - index < 1 or switch_num + index > switch_count: # 스위치 범위를 벗어났을 경우
        #         index -= 1
        #         break
        
        # for i in range(switch_num - index - 1, switch_num + index):
        #     if switches[i] == 0:
        #         switches[i] = 1
        #     else:
        #         switches[i] = 0

        # 현재 스위치 바꿔준다.
        if switches[switch_num - 1] == 0:
            switches[switch_num - 1] = 1
        else:
            switches[switch_num - 1] = 0
         
        for index in range(1, switch_count // 2 + 1): 
            if switch_num + index > switch_count or switch_num - index < 1: # 스위치 범위를 벗어났을 경우
                break

            if switches[switch_num + index - 1] == switches[switch_num - index - 1]: # 대칭일 경우
                if switches[switch_num + index - 1] == 0:
                    switches[switch_num + index - 1] = 1
                    switches[switch_num - index - 1] = 1
                else:
                    switches[switch_num + index - 1] = 0
                    switches[switch_num - index - 1] = 0
            else: # 대칭이 아닐 경우
                break 

for i in range(len(switches)):
    if i != 0 and i % 20 == 0: # 20번째일때마다 다음 줄로
        print()
    print(switches[i], end=" ")
    
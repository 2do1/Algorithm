from collections import deque

def check_left_gear(gear_num, direction): # 왼쪽 기어들을 쭉 확인한다.
    # 맞닿은 부분이 같은 극일 경우, 톱니바퀴를 왼쪽까지 모두 조사했을 경우
    if gear_num < 1 or gears[gear_num][2] == gears[gear_num + 1][6]: # 맞닿은 부분이 같은 극일 경우, 톱니바퀴를 왼쪽까지 모두 조사했을 경우
        return
    else:
        # 회전하기 전에 먼저 옆의 톱니바퀴들이 회전할 수 있는지 확인한다.
        check_left_gear(gear_num - 1, -direction)
        gears[gear_num].rotate(direction)


def check_right_gear(gear_num, direction): # 오른쪽 기어들을 쭉 확인한다.
    if 4 < gear_num or gears[gear_num - 1][2] == gears[gear_num][6]: # 맞닿은 부분이 같은 극일 경우, 톱니바퀴를 오른쪽까지 모두 조사했을 경우
        return
    else:
        # 회전하기 전에 먼저 옆의 톱니바퀴들이 회전할 수 있는지 확인한다.
        check_right_gear(gear_num + 1, -direction)
        gears[gear_num].rotate(direction)


# N극은 0, S극은 1, 12시부터 시계방향으로 
# 편의를 위해 톱니바퀴 번호와 인덱스를 똑같이 해준다.
gears = [deque()]
for _ in range(4):
    gears.append(deque(input()))

k = int(input()) # 회전 횟수

for _ in range(k):
    gear_num, direction = map(int, input().split())

    check_left_gear(gear_num - 1, -direction)
    check_right_gear(gear_num + 1, -direction)

    # 회전하기 전에 먼저 옆의 톱니바퀴들이 회전할 수 있는지 확인한다.
    gears[gear_num].rotate(direction)

answer = 0 # 점수의 합
for index in range(1, 5):
    if gears[index][0] == "1": # 12시방향이 S극일 경우
        answer += 2 ** (index - 1)

print(answer)
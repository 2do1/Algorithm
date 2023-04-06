from collections import deque

n, k = map(int, input().split()) # 길이가 n인 컨베이어 벨트

a = list(map(int, input().split()))

durabiltiy = deque(a) # 내구도를 큐에 담는다.

# 0번쨰 인덱스 올리는 위치 n - 1번째 인덱스 내리는 위치
belt = deque([False] * 2 * n) # 컨베이어 벨트, 로봇이있는지 확인하는 리스트

answer = 0 # 몇번쨰 단계인지

while True:
    answer += 1 # 1단계 증가

    # 로봇과 함께 한칸 회전한다.
    belt.rotate(1)
    durabiltiy.rotate(1)

    # 회전 시키고 난뒤 내리는 위치에 로봇이 있을 경우
    if belt[n - 1]: 
        belt[n - 1] = False

    # 내리는 위치 전 칸부터 탐색
    for index in range(n - 2, -1, -1):
        if belt[index]: # 현재 칸에 로봇이 있을 경우:
            if not belt[index + 1] and durabiltiy[index + 1] > 0: # 내구도가 0보다 크고, 다음 칸에 로봇이 없을 경우
                if index + 1 != n - 1: # 다음으로 옮길 칸이 내리는 칸이 아닐 경우
                    belt[index + 1] = True

                durabiltiy[index + 1] -= 1 # 다음칸 내구도 감소
                belt[index] = False # 로봇이 원래 있던 칸 로봇이 없다고 표시

    # 로봇은 올리는 위치에만 올릴 수 있다.
    if durabiltiy[0] > 0:
        belt[0] = True
        durabiltiy[0] -= 1 # 내구도 감소

    # 내구도가 0인 칸의 개수가 k개 이상일 때
    if durabiltiy.count(0) >= k: 
        break
                    
            
print(answer)
n = int(input()) # 동방 개수

# 맨 왼쪽 방 번호는 1번부터 시작
rooms = [False] * (n + 1)
rooms[0] = True

m = int(input()) # 빌런 행동 횟수

for _ in range(m):
    x, y = map(int, input().split())

    for index in range(x, y):
        rooms[index] = True
    

print(rooms.count(False))
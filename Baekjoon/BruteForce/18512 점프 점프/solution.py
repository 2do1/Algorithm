x, y, p1, p2 = map(int, input().split())

player_a = []
player_b = []

answer = 0
count = 0
while count < 1000:
    
    player_a.append(p1)
    player_b.append(p2)

    p1 += x
    p2 += y    

    if p1 in player_b or p2 in player_a:
        answer = min(p1, p2)
        break

    count += 1

if answer == 0:
    print(-1)
else:
    print(answer)
a, b, c, n = map(int, input().split()) # 방 정원 (a, b, c), 학생 수 n

answer = 0 # 빈 침대 없이 배정이 가능한지의 여부
for i in range(n // a + 1):
    for j in range(n // b + 1):
        for k in range(n // c + 1):
            total = a * i + b * j + c * k # 총 침대의 개수

            if total == n: # 빈 침대 없이 배정이 가능할 경우
                answer = 1 

print(answer)
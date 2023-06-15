total_score = 0

for _ in range(10):
    score = int(input())

    temp = total_score # 값 저장
    total_score += score

    if total_score >= 100:
        if abs(100 - total_score) > abs(100 - temp):
            total_score = temp
        break

print(total_score)
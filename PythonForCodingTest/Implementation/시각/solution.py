n = int(input()) # 정수 n

answer = 0 # 3이 하나라도 포함되는 모든 경우의 수
for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) or '3' in str(j) or '3' in str(k): # 3이 하나라도 있을 경우
            # if '3' in str(i) + str(j) + str(k) # 시, 분, 초를 한꺼번에 확인하기
                answer += 1

print(answer)
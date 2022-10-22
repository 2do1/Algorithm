s = input() # 문자열 S

answer = 0 # 행동의 최소 횟수
for i in range(len(s) - 1):
    if s[i] != s[i + 1]: # 다른 숫자일 경우
        answer += 1

answer = (answer + 1) // 2

print(answer)
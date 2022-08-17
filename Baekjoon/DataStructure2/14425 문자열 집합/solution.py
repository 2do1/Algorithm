n, m = map(int, input().split()) # 문자열의 개수 n과 m, n: 집합 s에 포함되어있는 문자열, m: 검사해야하는 문자열

s_set = set([input() for _ in range(n)]) # 집합 s
check_list = [input() for _ in range(m)] # 검사해야하는 문자열

answer = 0 # 문자열 몇개가 s에 포함되어 있나
for check in check_list:
    if check in s_set:
        answer += 1

print(answer)
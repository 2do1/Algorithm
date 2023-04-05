n = int(input()) # 수의 개수

a = list(map(int, input().split())) # 숫자들

plus_cnt, minus_cnt, mult_cnt, div_cnt = list(map(int, input().split())) # 연산자 개수

cases = [] # 가능한 모든 결과값 
max_answer = -2e9 # 최댓값
min_answer = +2e9 # 최솟값

def dfs(depth, total, plus, minus, mult, div):
    global max_answer, min_answer

    if depth == n:
        max_answer = max(max_answer, total)
        min_answer = min(min_answer, total)
        return
    
    if plus: # 플러스 기호가 1개 이상일 경우
        dfs(depth + 1, total + a[depth], plus - 1, minus, mult, div)
    if minus: # 마이너스 기호가 1개 이상일 경우
        dfs(depth + 1, total - a[depth], plus, minus - 1, mult, div)
    if mult: # 곱셈 기호가 1개 이상일 경우
        dfs(depth + 1, total * a[depth], plus, minus, mult - 1, div)
    if div: # 나눗셈 기호가 1개 이상일 경우
        dfs(depth + 1, int(total / a[depth]), plus, minus, mult, div - 1)
    
dfs(1, a[0], plus_cnt, minus_cnt, mult_cnt, div_cnt)

print(max_answer)
print(min_answer)
n = int(input())

a_list = sorted(map(int, input().split()))

total = sum(a_list) # 전체 쇠막대 길이

answer = 0
for a in a_list:
    total -= a
    answer += a * total

print(answer)
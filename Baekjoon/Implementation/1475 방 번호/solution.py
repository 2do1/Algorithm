n = list(map(int, list(input())))

cnt = [0] * 10

for num in n:
    if num == 6 or num == 9: # 6과 9는 구분하지 않는다.
        cnt[9] += 1
        continue

    cnt[num] += 1

cnt[9] = (cnt[9] + 1) // 2

print(max(cnt))
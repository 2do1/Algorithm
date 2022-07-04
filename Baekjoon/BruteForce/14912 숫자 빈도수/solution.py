n, d = input().split() # 1 ~ n까지 특정 숫자 d의 빈도수

count = 0 # 특정 숫자 d의 빈도수

for num in range(1, int(n) + 1): # 1 ~ n까지의 숫자들
    for digit in str(num):
        if d == digit: # d가 나타날 경우
            count += 1

print(count)
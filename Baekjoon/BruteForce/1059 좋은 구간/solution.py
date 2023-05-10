l = int(input())
s = [0] + list(map(int, input().split()))
n = int(input()) # n을 포함하는 좋은 구간의 개수

answer = 0
s.sort()

if n in s:
    print(0)
else:
    for index in range(l):
        if s[index] < n < s[index + 1]:
            answer = (n - s[index]) * (s[index + 1] - n) - 1
            print(answer)
            break
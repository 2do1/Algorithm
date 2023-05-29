n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

answer = []
a_index, b_index = 0, 0

while True:
    if a[a_index] <= b[b_index]:
        answer.append(a[a_index])
        a_index += 1
    else:
        answer.append(b[b_index])
        b_index += 1
    
    if a_index == n or b_index == m:
        answer += a[a_index:] + b[b_index:]
        break

print(*answer)
x = int(input())

stick = 64

answer = 0
while True:
    if x <= 0:
        break

    if stick > x:
        stick //= 2
    else:
        answer += 1
        x -= stick
        
print(answer)
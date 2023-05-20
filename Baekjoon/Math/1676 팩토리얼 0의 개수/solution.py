n = int(input())

factorial = 1

for num in range(n, 0, -1):
    factorial *= num
    
factorial = str(factorial)[::-1]
answer = 0 

for num in factorial:
    if num != '0':
        break
    answer += 1

print(answer)
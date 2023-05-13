a, b = input().split()

answer = 0

# 굳이 if else 문을 나눌필요는 없었다.
if len(a) == len(b): # 길이가 같을 경우
    for index in range(len(a)):
        if a[index] != b[index]:
            answer += 1 
    print(answer)
else: # A의 길이가 B의 길이보다 작을 경우
    answer = 1e9
    for i in range(len(b) - len(a) + 1):
        b_slice = b[i:i+len(a)]
        total = 0
        for j in range(len(a)):
            if a[j] != b_slice[j]:
                total += 1
        answer = min(answer, total)
    
    print(answer)
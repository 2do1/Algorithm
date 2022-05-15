n = int(input()) # 자연수 n 

ctor = False # 생성자가 존재하는지의 여부를 나타내는 boolean 변수

for num in range(1, n+1): # 1 ~ n까지 탐색
    total = num # 현재 숫자의 분해합을 나타내는 변수

    num_str = str(num) # 각 자릿수에 접근하기 위해 str형으로 변환
    for digit in num_str: 
        total += int(digit) # 각 자릿수가 str형이므로 더해주기 위해 int형으로 변환

    if total == n: # 현재 숫자가 n의 생성자일 경우
        answer = num
        ctor = True
        break

if ctor: # 생성자가 존재할 경우
    print(answer)
else: # 생성자가 존재하지 않을 경우
    print(0)

# 다른사람 풀이 
# n = int(input())

# result = 0
# for i in range(1, n+1):
#     a = list(map(int, str(i))) # map() 함수 이용
#     result = i + sum(a) # 분해합

#     if result == n: # 생성자가 존재할 경우
#         print(i)
#         break
    
#     if i == n: # 다 탐색했는데 생성자가 없을 경우 
#         print(0)
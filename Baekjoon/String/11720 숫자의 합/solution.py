n = int(input()) # 숫자의 개수 n
numbers = input() # 숫자들 문자열로 입력받는다.

total = 0 # 숫자들의 합
for num in numbers: # 숫자 하나씩 접근
    total += int(num) # int 형으로 변환해준다.

print(total)

# n = int(input()) # 숫자의 개수 n

# # numbers = map(int, input()) # list형으로 변환하지 않고 map 객체에서도 sum() 함수를 이용할 수 있다.
# numbers = list((map(int, input()))) # 숫자 n개 입력받는다.

# print(sum(numbers)) # 숫자들의 합 출력
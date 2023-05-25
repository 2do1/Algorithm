# 시간초과 발생
# from itertools import permutations

# n = list(input())

# numbers = sorted(permutations(n, len(n)), reverse=True)

# can_make = False
# answer = 0
# for num in numbers:
#     num = ''.join(num)
#     num = int(num)

#     if num % 30 == 0: # 30의 배수일 경우
#         can_make = True
#         answer = num
#         break

# if can_make:
#     print(answer)
# else:
#     print(-1)

n = sorted(input(), reverse=True)

total = 0
for num in n:
    total += int(num)

if total % 3 != 0 or n[-1] != '0':
    print(-1)
else:
    print(''.join(n))
a, b = map(int, input().strip().split(' '))

for i in range(b):
    for j in range(a):
        print('*', end='') # end 옵션 설정
    print() # 줄바꿈, 개행

# 처음 풀이
# a, b = map(int, input().strip().split(' '))

# star = ""

# for i in range(b):
#     for j in range(a):
#         star += '*'
#     print(star)
#     star = ""
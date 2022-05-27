ten = int(input(), 8) # 8진수를 입력받아 10진수로 변환한다.

binary = bin(ten)[2:] # 2진수 앞에 0b가 들어가기 때문에 두번째 자리부터 출력한다.

print(binary)

# 시간초과
# eight = input() # 8진수

# ten = int(eight, 8) # 10진수로 변환해준다.

# binary = "" # 2진수 

# while ten >= 1:
#     binary += str(ten % 2) # str형으로 변환후 더해준다.
#     ten //= 2

# print(binary[::-1]) # 역순으로 바꿔준다.
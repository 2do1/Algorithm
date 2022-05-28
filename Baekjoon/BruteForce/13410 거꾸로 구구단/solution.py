# n: 단의 수, k: 항의 수
n, k = map(int, input().split())

# reverse_times_table = [] # 거꾸로 구구단 숫자들을 담을 리스트

# for i in range(1, k + 1): # 1 ~ k 까지
#     num = int(str(i * n)[::-1]) # 슬라이싱 기법을 이용해 역순으로 바꿔주고, int형으로 다시 변환시켜주어 거꾸로 구구단 구현.
#     reverse_times_table.append(num)

# 리스트 안 for문
reverse_times_table = [int(str(i * n)[::-1]) for i in range(1, k + 1)] # 거꾸로 구구단 숫자들을 담을 리스트

print(max(reverse_times_table)) # 거꾸로 구구단 숫자들 중 최댓값 출력
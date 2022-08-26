n = int(input()) # 수의 개수 n

num_list = sorted([int(input()) for _ in range(n)], reverse=True) # 내림차순 정렬

for num in num_list:
    print(num, end=' ') # 띄어쓰기 출력
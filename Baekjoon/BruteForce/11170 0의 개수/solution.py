test_case = int(input()) # 테스트 케이스의 수

for _ in range(test_case):
    n, m = map(int, input().split()) # n부터 m까지의 수

    zero_total = 0 # 0의 총 개수
    for num in range(n, m + 1): # n부터 m까지
        str_num = str(num) # str 형으로 변환
        zero_total += str_num.count('0') # 0의 개수 세어준다.
    
    print(zero_total)
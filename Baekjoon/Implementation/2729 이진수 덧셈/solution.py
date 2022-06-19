t = int(input()) # 테스트 케이스의 개수

for _ in range(t):
    binary_a, binary_b = input().split() # 이진수 2개

    binary_sum = int(binary_a, 2) + int(binary_b, 2) # 십진수로 변환한 후 합을 구한다.
    binary_sum = bin(binary_sum)[2:] # 다시 이진수로 변환
    print(binary_sum) # 이진수 출력
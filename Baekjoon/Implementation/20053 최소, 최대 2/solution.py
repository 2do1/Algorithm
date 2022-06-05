t = int(input()) # 테스트 케이스 개수

for _ in range(t):
    n = int(input()) # n개의 정수
    num_list = list(map(int, input().split())) # 숫자들이 담긴 리스트
    print(min(num_list), max(num_list)) # 최소 최대 출력
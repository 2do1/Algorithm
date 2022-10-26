t = int(input()) # 테스트 케이스의 개수 t

for _ in range(t):
    n, m = map(int, input().split()) # A의 수 n, B의 수 m

    a_list = list(map(int, input().split()))
    b_list = sorted(map(int, input().split())) # 오름차순
    answer = 0 # a가 b보다 큰 쌍의 개수

    for a in a_list:

        idx = -1 # a보다 작지만 제일 큰 수의 인덱스 값
        start = 0 
        end = len(b_list) - 1

        while start <= end:
            mid = (start + end) // 2

            if b_list[mid] < a: # a가 b보다 더 클 경우
                start = mid + 1
                idx = mid 
            else: # a가 b 이하일 경우
                end = mid - 1

        answer += idx + 1
    print(answer)
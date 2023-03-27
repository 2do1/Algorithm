n, x = map(int, input().split()) #총 n일, x일 동안 가장 많이

visitors = list(map(int, input().split()))

if max(visitors) == 0: # 최고 방문자 수가 0일경우
    print("SAD")
else:
    
    total = sum(visitors[:x])

    max_num = total # 최고 방문자 수
    count = 1

    for index in range(x, n):

        total += visitors[index]
        total -= visitors[index - x]

        if total > max_num: # 값이 더 클 경우
            max_num = total
            count = 1
        elif total == max_num: # 다른 기간이 있을 경우
            count += 1

    print(max_num)
    print(count)
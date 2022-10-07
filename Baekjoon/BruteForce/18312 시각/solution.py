n, k = map(int, input().split())

answer = 0 # k가 하나라도 포함되는 시각들의 수
for hour in range(n + 1):
    for minute in range(60):
        for second in range(60):
            k = str(k)
            hour = str(hour)
            minute = str(minute)
            second = str(second)

            # 한자리 수 일 경우 0을 붙여줘야함
            if len(hour) == 1: 
                hour = "0" + hour
            if len(minute) == 1:
                minute = "0" + minute
            if len(second) == 1:
                second = "0" + second
        
            if k in hour + minute + second: # k가 하나라도 포함되는 시각일 경우
                answer += 1

print(answer)
# n은 온도를 측정한 전체 날짜의 수, k는 합을 구하기 위한 연속적인 날짜의 수
n, k = map(int, input().split())
temperature_list = list(map(int, input().split())) # 매일 측정한 온도

answer = -100 # 연속적인 k일의 온도의 합이 최대가 되는 값
for i in range(n - k + 1):
    temp = sum(temperature_list[i:i+k]) # 연속적인 k일의 온도의 합
    if temp > answer: # 기존의 값보다 더 큰 값일 경우, 최대를 찾아가는 과정
        answer = temp

print(answer)
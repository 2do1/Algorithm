n = int(input())

if n < 10: # 주어진 수가 10보다 작다면
    n *= 10 # 0을 붙여준다.

cycle_num = n # 사이클 연산 한 수
cycle_len = 0 # n의 사이클의 길이

while True:
    unit = cycle_num % 10 # 일의자리
    ten = cycle_num // 10 # 십의자리

    total = (unit + ten) % 10 # 각 자릿수의 합. total이 10이 넘어갈수도 있기 때문에 % 10 연산을 해준다.
     
    cycle_num = unit * 10 + total # 사이클 연산 한 수
    cycle_len += 1

    if cycle_num == n: # 원래 수 n으로 다시 돌아왔을때
        print(cycle_len)
        break
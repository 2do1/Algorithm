# A: 한시간 일하면 쌓이는 피로도 B: 한시간에 처리할수있는 일 
# C: 한시간 쉬면 줄어드는 피로도 M: 쌓일 수 있는 최대 피로도

a, b, c, m = map(int, input().split())

max_work = 0 # 하루 최대 일할 수 있는 양
fatigue = 0 # 피로도
hour = 0 # 시간

while hour != 24: # 하루는 24시간이기 때문에
    if a > m: # 한시간 일할때 쌓이는 피로도가 최대 피로도보다 크면 일할수 없다.
        break
    if fatigue + a <= m: # 일할수 있을때
        fatigue += a
        max_work += b
        hour += 1
    else: # 쉬어야 할때 
        fatigue -= c
        if fatigue < 0: # 피로도가 음수가 되면 0으로 변경해준다.
            fatigue = 0
        hour += 1
    
print(max_work)
year = int(input()) # 연도

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0): # 윤년인 경우
    print(1)
else: # 윤년이 아닌 경우
    print(0)
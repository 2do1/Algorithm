def solution(a, b):
    answer = 0
    day_list = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"] # 2016년은 금요일부터 시작
    month_days_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 각 월 별 총 일 수
    
    answer += sum(month_days_list[:a-1]) + b - 1 # 총 일수 
    answer %= 7 # 7로 나눈 나머지.
    
    answer = day_list[answer]
    return answer
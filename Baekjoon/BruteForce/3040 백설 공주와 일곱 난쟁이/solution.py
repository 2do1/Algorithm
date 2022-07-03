from itertools import combinations

dwarf_list = [int(input()) for _ in range(9)] # 아홉 난쟁이

case_list = combinations(dwarf_list, 7) # 일곱 난쟁이를 선택할 수 있는 경우의 수
for case in case_list:
    if sum(case) == 100: # 합이 100일 경우
        for num in case: # 모자에 쓰여 있는 수 출력
            print(num)
        break
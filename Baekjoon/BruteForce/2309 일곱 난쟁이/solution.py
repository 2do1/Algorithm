from itertools import combinations

dwarf_list = sorted([int(input()) for _ in range(9)]) # 아홉 난쟁이들의 키, 오름차순 정렬

case_list = list(combinations(dwarf_list, 7)) # 일곱 난쟁이를 선택하는 경우의 수

for case in case_list:
    if sum(case) == 100: # 일곱 난쟁이의 키의 합이 100일 경우
        for height in case: # 오름차순으로 출력
            print(height)
        break
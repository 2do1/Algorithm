from bisect import bisect_left, bisect_right

def count_by_range(array, left, right): # 값이 특정 범위에 속하는 데이터 개수 구하기
    left_index = bisect_left(array, left)
    right_index = bisect_right(array, right)

    return right_index - left_index
    

n = int(input()) # 상근이가 갖고 있는 카드의 개수
card_list = sorted(map(int, input().split())) # 오름차순 정렬

m = int(input()) # 상근이가 몇 개 가지고 있는 숫자 카드인지 구해야할 m개의 정수
num_list = list(map(int, input().split())) # m개의 정수

for num in num_list:
    print(count_by_range(card_list, num, num), end=' ') # 상근이가 몇 개 가지고 있는지 출력
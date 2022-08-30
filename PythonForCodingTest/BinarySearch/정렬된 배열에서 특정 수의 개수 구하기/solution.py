from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

n, x = map(int, input().split()) # n 개의 원소, 값 x

num_list = list(map(int, input().split()))

x_count = count_by_range(num_list, x, x) # 값이 x인 수의 개수 구하기

if x_count == 0: # 존재하지 않으면
    print(-1)
else: # 존재한다면
    print(x_count)
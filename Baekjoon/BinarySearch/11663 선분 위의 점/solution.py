from bisect import bisect_left, bisect_right

def count_by_range(array, left, right): # 값이 특정 범위에 속하는 데이터 개수 구하기
    left_index = bisect_left(array, left)
    right_index = bisect_right(array, right)

    return right_index - left_index

n, m = map(int, input().split()) # 점 n개와 선분 m개

n_list = sorted(map(int, input().split())) # 점의 좌표
m_list = [list(map(int, input().split())) for _ in range(m)] # 선분의 시작점과 끝점

for m in m_list:
    print(count_by_range(n_list, m[0], m[1])) # 선분 위에 입력으로 주어진 점이 몇 개 있는지 출력
# 이진 탐색 풀이
n = int(input())
n_list = sorted(map(int, input().split())) # 이진 탐색을 위해 오름차순 정렬

m = int(input())
m_list = list(map(int, input().split()))


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target: # 찾는 값일 경우
            return mid 
        elif array[mid] > target: # 찾는 값보다 클 경우
            end = mid - 1
        else: # 찾는 값보다 작을 경우
            start = mid + 1
        
    return None

for m in m_list:
    result = binary_search(n_list, m, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')

# # 계수 정렬
# n = int(input())
# n_list = [0] * 1000001

# for n in input().split(): # 부품 번호 입력받아 기록
#     n_list[int(n)] = 1

# m = int(input())
# m_list = list(map(int, input().split()))

# for m in m_list:
#     if n_list[m] == 1:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')

# # 집합 자료형 풀이
# n = int(input())
# n_list = set(map(int, input().split())) # 집합 

# m = int(input())
# m_list = list(map(int, input().split()))

# for m in m_list:
#     if m in n_list:
#         print('yes', end=' ')
#     else:
#         print('no', end=' ')
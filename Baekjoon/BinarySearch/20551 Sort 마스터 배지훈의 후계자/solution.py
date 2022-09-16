import sys

def binary_search(b_list, question):
    start = 0
    end = len(b_list) - 1
    is_exist = False # 존재하는지 여부

    while start <= end:
        mid = (start + end) // 2

        if b_list[mid] == question: # 존재한다면
            if mid == end:
                is_exist = True
                break
            end = mid # 하나씩 값을 줄여준다.
        elif b_list[mid] > question: # 질문에 주어진 값보다 클 경우
            end = mid - 1
        else: # 질문에 주어진 값보다 작을 경우
            start = mid + 1
    if is_exist: # 존재할 경우
        return mid
    else: # 존재하지 않을 경우
        return -1


n, m = map(int, sys.stdin.readline().split()) # 배열 a의 원소의 개수 n, 질문의 개수 m

b_list = sorted([int(sys.stdin.readline()) for _ in range(n)]) # 배열 A 오름차순 정렬한 배열 B
question_list = [int(sys.stdin.readline()) for _ in range(m)] # 질문 리스트들

for question in question_list:
    print(binary_search(b_list, question))
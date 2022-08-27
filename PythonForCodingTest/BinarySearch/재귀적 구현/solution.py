def binary_search(array, target, start, end): # 재귀 함수
    if start > end: # 데이터가 존재하지 않을 경우 
        return None
    mid = (start + end) // 2 # 나눈 몫만을 구하기 위해

    if array[mid] == target: # 찾고자 하는 값을 찾았을 때
        return mid
    elif array[mid] > target: # 찾고자 하는 값보다 큰 경우 -> 왼쪽을 확인
        return binary_search(array, target, start, mid - 1)
    else: # 찾고자 하는 값이 큰 경우 -> 오른쪽을 확인
        return binary_search(array, target, mid + 1, end)

n, target = list(map(int, input().split())) # n 원소의 개수, target 찾고자 하는 값

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
    print('원소가 존재하지 않습니다')
else:
    print(result + 1)
t = int(input()) # 테스트케이스 개수

def binary_search(start, end, array, num):
    
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == num: # 수첩1에 있을 경우
            return 1
        elif array[mid] > num: # 숫자보다 더 클 경우
            end = mid - 1
        else: # 숫자보다 더 작을 경우
            start = mid + 1
    return 0

for _ in range(t):
    n = int(input())
    note1 = sorted(map(int, input().split())) # 오름차순 정렬

    m = int(input())
    note2 = list(map(int, input().split()))
    
    for num in note2:
        print(binary_search(0, len(note1)-1, note1, num))
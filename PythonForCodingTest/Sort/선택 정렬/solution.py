array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_idx = i # 가장 작은 원소의 인덱스값
    for j in range(i + 1, len(array)):
        if array[min_idx] > array[j]: # 값이 더 크면
            min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i] # 스와프

print(array) # 정렬한 리스트 출력
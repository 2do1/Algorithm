array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 한칸씩 왼쪽으로 이동
        if array[j] < array[j - 1]: 
            array[j], array[j - 1] = array[j - 1], array[j] # 스와핑
        else: # 삽입할 데이터보다 작은 데이터를 만날 경우
            break

print(array) 
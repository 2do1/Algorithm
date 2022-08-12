from collections import deque

n = int(input()) # n장의 카드

num_list = deque([i for i in range(1, n + 1)])

while len(num_list) != 1: # 하나가 남을 때 까지
    num_list.popleft() # 제일 위에있는 것을 버린다.
    temp = num_list.popleft() # 제일 위에있는 것을
    num_list.append(temp) # 제일 아래로 옮긴다.

print(num_list[0]) # 가장 마지막에 남는 카드    
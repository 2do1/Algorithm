n = int(input())

trophy_list = [int(input()) for _ in range(n)] # 트로피들의 높이

left = 0 # 왼쪽에서 보이는 개수
left_max = 0 # 왼쪽에서 봤을 때 가장 큰 트로피
for trophy in trophy_list: # 왼쪽에서 봤을 때
    if trophy > left_max: # 더 큰 트로피일 때
        left_max = trophy
        left += 1

right = 0 # 오른쪽에서 보이는 개수
right_max = 0 # 오른쪽에서 봤을 때 가장 큰 트로피
trophy_list = trophy_list[::-1] # 거꾸로 뒤집어 준다.
for trophy in trophy_list: # 오른쪽에서 봤을 때
    if trophy > right_max: # 더 큰 트로피일 때
        right_max = trophy
        right += 1

print(left)
print(right)
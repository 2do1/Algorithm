n, m = map(int, input().split()) # n: 나무의 수, m: 가져가려고 하는 나무의 길이

tree_list = list(map(int, input().split())) # 나무의 높이

start = 0 
end = max(tree_list) 

while start <= end:
    mid = (start + end) // 2
    total = 0 # 가져갈 수 있는 나무의 길이
    for tree in tree_list:
        if tree > mid: # 나무의 길이가 절단기의 높이보다 클 경우
            total += tree - mid
    
    if total >= m: # 가져가려고 하는 나무의 길이보다 크거나 같을 경우
        start = mid + 1
    else: # 가져가려고 하는 나무의 길이보다 작을 경우
        end = mid - 1

print(end)

# 틀린 코드
# n, m = map(int, input().split()) # n: 나무의 수, m: 가져가려고 하는 나무의 길이

# tree_list = list(map(int, input().split())) # 나무의 높이

# start = 0 
# end = max(tree_list) 

# while start <= end:
#     mid = (start + end) // 2
#     total = 0 # 가져갈 수 있는 나무의 길이
#     for tree in tree_list:
#         if tree > mid: # 나무의 길이가 절단기의 높이보다 클 경우
#             total += tree - mid
    
#     if total == m: # 가져가려고 하는 나무의 길이일 경우
#         answer = mid 
#         print(answer)
#         break
#     elif total > m: # 가져가려고 하는 나무의 길이보다 클 경우
#         start = mid + 1
#     else: # 가져가려고 하는 나무의 길이보다 작을 경우
#         end = mid - 1
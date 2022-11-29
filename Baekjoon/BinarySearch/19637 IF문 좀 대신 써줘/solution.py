import sys

def binary_search(character):
    start = 0 
    end = len(titles) - 1 

    index = 0
    while start <= end:
        mid = (start + end) // 2

        if int(titles[mid][1]) >= character:
            end = mid - 1
            index = mid
        else:
            start = mid + 1
    
    return index

n, m = map(int, sys.stdin.readline().split())

titles = [sys.stdin.readline().split() for _ in range(n)]

for _ in range(m):
    character = int(sys.stdin.readline())
    index = binary_search(character)

    print(titles[index][0])


# 시간 초과
# import sys

# n, m = map(int, sys.stdin.readline().split())

# titles = [sys.stdin.readline().split() for _ in range(n)]

# characters = sorted([int(sys.stdin.readline()) for _ in range(m)])


# def binary_search(power):
#     start = 0 
#     end = len(characters) - 1

#     count = 0 # 칭호에 해당하는 캐릭터의 개수 
#     while start <= end:
#         mid = (start + end) // 2

#         if characters[mid] <= power:
#             count = mid + 1
#             start = mid + 1
#         else:
#             end = mid - 1
    
#     return count

# for title in titles:
#     name = title[0] # 칭호 
#     power = int(title[1]) # 전투력

#     count = binary_search(power) # 칭호에 해당하는 캐릭터의 개수 

#     for _ in range(count): # 칭호 출력
#         print(name)

#     characters = characters[count:] # 칭호를 출력한 캐릭터들은 제외
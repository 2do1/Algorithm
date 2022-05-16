board = input() # 보드판

board_split = board.split('.') # '.'을 기준으로 구분해준다.

answer = "" # 폴리오미노로 모두 덮은 보드판

count = 0 
for part in board_split:
    part_len = len(part) # 보드 부분마다의 길이

    answer += "AAAA" * (part_len // 4)
    part_len %= 4

    if part_len != 0: # "AAAA"로 다 덮어지지 않는 경우
        answer += "BB" * (part_len // 2)
        part_len %= 2

    if part_len != 0: # 두 폴리오미노로 덮을 수 없을 경우 
        answer = -1
        break

    count += 1

    if count != len(board_split): # 마지막에 . 을 붙이는 것을 방지하기 위해
        answer += "."

print(answer)


# # 다른 사람의 풀이1 - join() 함수 이용
# board = input()

# answer = []
# idx = 0 # 인덱스 값
# while idx < len(board):
#     if board[idx:idx+4] == 'XXXX': 
#         answer.append('AAAA')
#         idx += 4
#     elif board[idx:idx+2] == 'XX':
#         answer.append('BB')
#         idx += 2
#     elif board[idx] == '.':
#         answer.append('.')
#         idx += 1
#     else:
#         break

# answer = ''.join(answer) # join으로 합쳐준다.
# if len(board) == len(answer):
#     print(answer)
# else:
#     print(-1)

# # 다른 사람의 풀이2 - replace() 함수 이용
# board = input() 

# board = board.replace("XXXX", "AAAA") 
# board = board.replace("XX", "BB") 

# if 'X' in board: 
#     print(-1) 
# else: 
#     print(board)
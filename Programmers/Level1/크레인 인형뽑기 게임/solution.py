def solution(board, moves):
    answer = 0
    stack = [] # 바구니
    
    for pick_num in moves:
        pick_num -= 1 # 인덱스 접근하기 위해 1 감소 시켜준다.
        for i in range(len(board)): 
            if board[i][pick_num] != 0: # 인형일 경우
                if len(stack) == 0: # 바구니가 비었을 경우
                    stack.append(board[i][pick_num]) # 인형을 바구니에 넣는다.
                    board[i][pick_num] = 0 # 인형을 집었기 때문에 0으로 바꿔준다.
                    break
                    
                if stack[-1] == board[i][pick_num]: # 같은 모양의 인형 두개가 연속해서 쌓일때
                    stack.pop() # 인형 바구니에서 제거
                    board[i][pick_num] = 0 # 인형을 집었기 때문에 0으로 바꿔준다.
                    answer += 2
                    break
                else: # 같은 모양의 인형 두개가 연속해서 쌓이지 않을때
                    stack.append(board[i][pick_num]) # 인형을 바구니에 넣는다.
                    board[i][pick_num] = 0 # 인형을 집었기 때문에 0으로 바꿔준다.
                    break                
    return answer

# 다른 사람의 풀이
# def solution(board, moves):
#     stacklist = []
#     answer = 0

#     for i in moves:
#         for j in range(len(board)):
#             if board[j][i-1] != 0:
#                 stacklist.append(board[j][i-1])
#                 board[j][i-1] = 0

#                 if len(stacklist) > 1:
#                     if stacklist[-1] == stacklist[-2]:
#                         stacklist.pop()
#                         stacklist.pop()
#                         answer += 2     
#                 break

#     return answer
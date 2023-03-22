import sys

def check_bingo():
    # 행 체크
    total_bingo = 0
    for row in check:
        if row.count(True) == 5: # 빙고일 경우
            total_bingo += 1

     # 열 체크
    for i in range(5):
        total = 0
        for j in range(5):
            if check[j][i] == True:
                total += 1
            else:
                break

        if total == 5: # 빙고일 경우
            total_bingo += 1

    left_diagonal = 0 # 왼쪽 위 대각선
    for index in range(5):
        if check[index][index] == True:
            left_diagonal += 1
        else:
            break
    
    if left_diagonal == 5:
        total_bingo += 1
    

    right_diagonal = 0 # 오른쪽 위 대각선
    for index in range(5):
        if check[index][4 - index] == True: 
            right_diagonal += 1
        else:
            break

    if right_diagonal == 5:
        total_bingo += 1

    return total_bingo

def erase_num(num): # 사회자가 부르는 수 지워나간다.
    for i in range(5):
        for j in range(5):
            if board[i][j] == num:
                check[i][j] = True
                return

board = [list(map(int, input().split())) for _ in range(5)]
check = [[False] * 5 for _ in range(5)]
count = 0
bingo_count = 0 # 빙고 개수


numbers = [list(map(int, input().split())) for _ in range(5)]

for number in numbers:
    for num in number:
        erase_num(num)
        count += 1

        # 행 열 대각선 빙고있는지 확인
        bingo_count = check_bingo()

        if bingo_count >= 3:
            print(count)
            sys.exit(0)
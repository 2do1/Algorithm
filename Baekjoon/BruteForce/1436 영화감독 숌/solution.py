n = int(input()) # n번째 영화의 제목에 들어간 수

num = 1
count = 0 # 몇번째 영화인지
while True:
    if "666" in str(num): # 6이 적어도 3개이상 연속으로 들어가는 수일 경우
        count += 1
        if n == count: # n번째 영화일 경우
            print(num) # 영화 제목에 들어간 수 출력
            break
    num += 1
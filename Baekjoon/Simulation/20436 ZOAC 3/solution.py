def check_location(alpha):
    for index in range(len(keyboard)):
        if alpha in keyboard[index]: # 현재 행에 있을 경우
            return index, keyboard[index].index(alpha) # x, y 좌표 반환

sl, sr = input().split()

word = input()

# 한글 자음들 모음
consonants = "qwertasdfgzxcv"
## 키보드 자판
keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    
answer = 0 
for alphabet in word:
    x, y = check_location(alphabet) # 현재 단어의  x, y 좌표

    if alphabet in consonants: # 자음일 경우 왼손으로 입력한다.
        sl_x, sl_y = check_location(sl) # 현재 왼손이 위치하는 알파벳의 좌표

        answer += abs(sl_x - x) + abs(sl_y - y) + 1 # 키를 누르는데에도 1의 시간이 걸린다.
        sl = alphabet # 누른 알파벳 위치로 이동시킨다.
        
    else: # 모음일 경우 오른손으로 입력한다.
        sr_x, sr_y = check_location(sr) # 현재 왼손이 위치하는 알파벳의 좌표

        answer += abs(sr_x - x) + abs(sr_y - y) + 1 # 키를 누르는데에도 1의 시간이 걸린다.
        sr = alphabet # 누른 알파벳 위치로 이동시킨다.
    
print(answer)
# pi, ka, chu 세 단어

s = input() # 문자열 s

s = s.replace("pi", "XX") # pi
s = s.replace("ka", "XX") # ka
s = s.replace("chu", "XXX") # chu

if s == ('X' * len(s)): # 문자열 S를 세 단어로 이어 붙여 만들 수 있으면
    print("YES")
else: # 문자열 S를 세 단어로 이어 붙여 만들 수 없으면
    print("NO")
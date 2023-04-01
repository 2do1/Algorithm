import re

t = int(input())

p = re.compile("^[A-F]?A+F+C+[A-F]?$") # 정규 표현식

for _ in range(t):
    word = input()
    
    if p.match(word) == None: # 규칙을 지키는 문자열일 경우
        print("Good")
    else:
        print("Infected!")
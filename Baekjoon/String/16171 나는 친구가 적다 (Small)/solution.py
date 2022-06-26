s = input() # 교과서의 문자열
k = input() # 찾고자 하는 키워드

word = "" # 교과서의 문자열에서 숫자를 제외한 문자열
for char in s:
    # if not char.isdigit(): # 숫자가 아닐경우
    #     word += char
    if char.isalpha(): # 알파벳일 경우
        word += char

if k in word: # 찾고자 하는 키워드가 교과서의 문자열에 있을 경우
    print(1)
else: # 찾고자 하는 키워드가 교과서의 문자열에 없을 경우
    print(0)
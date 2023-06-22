word = input()
stack = []

while True:
    if word == "고무오리 디버깅 끝":
        break

    if word == "문제":
        stack.append(word)
    elif word == "고무오리":
        if stack:
            stack.pop()
        else:
            stack.append("문제")
            stack.append("문제")
    word = input()

if stack:
    print("힝구")
else:
    print("고무오리야 사랑해")
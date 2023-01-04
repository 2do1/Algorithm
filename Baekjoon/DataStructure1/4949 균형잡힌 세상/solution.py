while True:
    word = input()

    if word == ".":
        break

    stack = []
    is_balance = True

    for char in word:
        if char == "(" or char == "[":
            stack.append(char)
        
        elif char == ")":
            if not stack:
                is_balance = False
                break
            elif stack[-1] != "(":
                is_balance = False
                break
            else:
                stack.pop()
            
        elif char == "]":
            if not stack:
                is_balance = False
                break
            elif stack[-1] != "[":
                is_balance = False
                break
            else:
                stack.pop()

    if not stack and is_balance:
        print("yes")
    else:
        print("no")
            
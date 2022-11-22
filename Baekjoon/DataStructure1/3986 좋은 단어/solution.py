def is_good_word(word):
    stack = []

    for alphabet in word:
        if not stack:
            stack.append(alphabet)
            continue
        
        if stack[-1] == alphabet:
            stack.pop()
        else:
            stack.append(alphabet)
    
    if stack:
        return False
    else:
        return True

n = int(input())

answer = 0 # 좋은 단어의 수 
for _ in range(n):
    word = input()
    if is_good_word(word): 
        answer += 1

print(answer)
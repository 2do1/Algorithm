n, h, w = map(int, input().split())

words = [input() for _ in range(h)]

def isAlphabet(index):
    for i in range(index * w, (index + 1) * w):
        for j in range(h):
            if words[j][i] != '?':
                return words[j][i]
    return '?'
    

answer = ""

for index in range(n):
    answer += isAlphabet(index)   

print(answer)
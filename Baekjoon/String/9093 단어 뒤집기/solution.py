t = int(input())

for _ in range(t):

    sentence = input().split()
    reverse_sentence = []

    for word in sentence:
        reverse_sentence.append(word[::-1])
    
    answer = " ".join(reverse_sentence)
    print(answer)

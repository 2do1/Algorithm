n = int(input())

word_list = []
for _ in range(n):
    word = input()

    word = ''.join(sorted(word))
    
    word_list.append(word)


print(len(set(word_list)))
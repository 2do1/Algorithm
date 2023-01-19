word = input()

words = []

for i in range(1, len(word) - 2):
    for j in range(i + 1, len(word)):
        word1 = word[:i]
        word2 = word[i:j]
        word3 = word[j:]

        new_word = word1[::-1] + word2[::-1] + word3[::-1]

        words.append(new_word)

words.sort()
print(words[0])

# word = input()

# words = []

# for i in range(1, len(word) - 1):
#     for j in range(i + 1, len(word)):
#         word1 = word[:i]
#         word2 = word[i:j]
#         word3 = word[j:]

#         new_word = word1[::-1] + word2[::-1] + word3[::-1]

#         words.append(new_word)

# words.sort()
# print(words[0])
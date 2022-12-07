sentence = input()
key = input()

answer = ""

for index in range(len(sentence)):
    if sentence[index] == " ":
        answer += " "
        continue

    answer += chr((ord(sentence[index]) - ord(key[index % len(key)]) - 1) % 26 + ord('a'))

print(answer)
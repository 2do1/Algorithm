t = int(input())

for _ in range(t):
    alphabet = [0] * 26
    sentence = input()

    for char in sentence:
        if char.isalpha(): # 알파벳일 경우
            alphabet[ord(char) - ord('a')] += 1
    idx = max(alphabet)

    if alphabet.count(idx) >= 2:
        print('?')
    else:
        print(chr(alphabet.index(idx) + ord('a')))
def check_is_vowel(word):
    for alphabet in word:
        if alphabet in vowels:
            return True
    return False

def check_vowel_or_consonant_three_times(word):
    if len(word) <= 2:
        return True

    for index in range(len(word) - 2):
        sub_string = word[index:index + 3]
        consonant = 0 # 자음
        vowel = 0 # 모음
        for alphabet in sub_string:
            if alphabet in vowels:
                vowel += 1
            else:
                consonant += 1
        if vowel == 3 or consonant == 3:
            return False
    
    return True

def check_same_alphabet_two_times(word):
    for index in range(len(word) - 1):
        sub_string = word[index:index + 2]
        if sub_string == word[index] * 2:
            if sub_string == "ee" or sub_string == "oo":
                continue
            return False
    return True

vowels = ['a', 'e', 'i', 'o', 'u']

while True:
    word = input()

    if word == "end":
        break

    if check_is_vowel(word) and check_vowel_or_consonant_three_times(word) and check_same_alphabet_two_times(word):
        print("<" + word + "> is acceptable.")
    else:
        print("<" + word + "> is not acceptable.")
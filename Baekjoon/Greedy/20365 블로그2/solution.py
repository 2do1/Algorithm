n = int(input())

words = input()

blue_count = 0
red_count = 0

for index in range(len(words) - 1):
    if words[index] != words[index + 1]:
        if words[index] == "B":
            blue_count += 1
        else:
            red_count += 1

print(max(blue_count, red_count) + 1)
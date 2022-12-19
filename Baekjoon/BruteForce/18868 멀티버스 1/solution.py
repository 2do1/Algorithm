def compare_spaces(space1, space2):
    for i in range(len(space1)):
        for j in range(i + 1, len(space1)):
            if space1[i] < space1[j]:
                if space2[i] >= space2[j]:
                    return False
            elif space1[i] > space1[j]:
                if space2[i] <= space2[j]:
                    return False
            else:
                if space2[i] != space2[j]:
                    return False
    return True

m, n = map(int, input().split())

spaces = [list(map(int, input().split())) for _ in range(m)]

answer = 0
for i in range(len(spaces)):
    for j in range(i + 1, len(spaces)):
        space1 = spaces[i]
        space2 = spaces[j]
        if compare_spaces(space1, space2):
            answer += 1

print(answer)
word = input()

croatias = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

answer = 0 # 몇 개의 크로아티아 알파벳
for crotia in croatias:
    if crotia in word:
        answer += word.count(crotia)
        word = word.replace(crotia, "X" * len(crotia))

answer += len(word) - word.count("X") # 목록에 없는 알파벳은 한글자씩 센다

print(answer)
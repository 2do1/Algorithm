n = int(input()) # 그림의 개수

pictures = []

for _ in range(n):
    picture = [input() for _ in range(5)]
    pictures.append(picture)

pic1, pic2 = 0, 0
min_same = 1e9
for i in range(n):
    for j in range(i + 1, n):
        total_diff = 0  
        for k in range(5):
            for l in range(7):
                if pictures[i][k][l] != pictures[j][k][l]:
                    total_diff += 1
        
        if total_diff < min_same: 
            min_same = total_diff
            pic1 = i + 1
            pic2 = j + 1

print(str(pic1) + " " + str(pic2))
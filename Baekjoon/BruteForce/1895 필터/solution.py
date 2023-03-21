r, c = map(int, input().split())

image = [list(map(int, input().split())) for _ in range(r)]
t = int(input())

filter_image = []


for i in range(1, r - 1):
    for j in range(1, c - 1):
        temp = []
        for k in range(i - 1, i + 2):
            for l in range(j - 1, j + 2):
                temp.append(image[k][l])

        temp.sort() # 오름차순 정렬
        filter_image.append(temp[4]) # 필터링된 이미지에 추가

answer = 0 # T보다 크거나 같은 것의 개수
for pixel in filter_image:
    if pixel >= t:
        answer += 1

print(answer)

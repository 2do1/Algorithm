for i in range(6, 101): # a <= 100을 만족하는 수
    for j in range(2, i):
        for k in range(j, i):
            for p in range(k, i):
                if i ** 3 == j ** 3 + k ** 3 + p ** 3: # 완전 세제곱 방식을 만족하는 경우
                    print("Cube = {}, Triple = ({},{},{})".format(i, j, k, p))
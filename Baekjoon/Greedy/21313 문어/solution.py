n = int(input()) # N마리 문어

if n % 2 == 0:
    print("1 2 " * (n // 2))
else:
    print("1 2 " * (n // 2), "3", sep="")
n = int(input())

for index in range(1, n + 1):
    case = input().split()

    print("Case #%d: %s" %(index, ' '.join(case[::-1])))
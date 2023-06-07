k = int(input())

a = [1]
b = [0]

for index in range(k):
    a.append(b[index])
    b.append(a[index] + b[index])


print(str(a[-1]) + " " + str(b[-1]))
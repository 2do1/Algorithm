t = int(input())

for _ in range(t):
    answer = 0

    bit1, bit2 = input().split()

    one_count = 0 
    zero_count = 0
    for index in range(len(bit1)):
        if bit1[index] != bit2[index]:
            if bit1[index] == "1":
                one_count += 1
            elif bit1[index] == "0":
                zero_count += 1
    
    # if zero_count > one_count:
    #     print(zero_count - one_count + one_count)
    # else:
    #     print(one_count - zero_count + zero_count)

    print(max(one_count, zero_count))
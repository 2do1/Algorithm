while True:
    try:
        a = list(input())
        b = list(input())

        temp = []
        for alphabet in a:
            if alphabet in b:
                temp.append(alphabet)
                b.remove(alphabet)
        
        temp.sort()
        print("".join(temp))
    except EOFError:
        break
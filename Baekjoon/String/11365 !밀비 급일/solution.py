while True:
    password = str(input()) # 암호

    if password == "END": # 마지막 줄, "END"일 경우
        break
    
    password = password[::-1] # 암호 뒤집기
    print(password)

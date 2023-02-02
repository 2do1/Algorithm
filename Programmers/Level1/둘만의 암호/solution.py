def solution(s, skip, index):
    answer = ''
    
    for alphabet in s:
        asci = ord(alphabet)
        count = 0
        while True:
            asci += 1
            
            if asci > 122: # 'z'
                asci = 97 # 'a'
            
            if chr(asci) in skip:
                continue
            
            count += 1
            
            if count == index:
                break
        answer += chr(asci)

    return answer
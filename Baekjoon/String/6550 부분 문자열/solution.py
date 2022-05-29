while True:
    try:
        s, t = input().split() # 문자열 s, t
        substring = True # 서브스트링인지의 여부를 알려주는 boolean 변수. 테스트케이스마다 초기화를 꼭 해줘야한다...
        
        if s in t: # 문자열 s 전체가 t에 포험될 경우 
            pass
        else:
            for alphabet in s: # 알파벳 하나씩 접근
                if alphabet not in t: # s의 알파벳이 t에 존재하지 않을때
                    substring = False
                    break
                else: # s의 알파벳이 t에 존재할때
                    idx = t.index(alphabet) # t에서의 인덱스값
                    t = t[idx+1:] # 해당 알파벳 이후 부분만 남게 문자열 t 슬라이싱

        if substring: # 부분 문자열인경우
            print("Yes")
        else: # 부분 문자열이 아닌경우
            print("No")
    except: # 더 이상 받을 테스트케이스가 없을 경우
        break


# 다른 사람의 풀이
# while True :
#   try :
#     s, t = input().split()
    
#     value = 0
#     flag = 0
#     for i in range(len(t)) :
#       if t[i] == s[value] :
#         value += 1
#         if value == len(s) :
#           flag = 1
#           break

#     if flag == 1 :
#       print('Yes')
#     else :
#       print('No')

#   except :
#     break
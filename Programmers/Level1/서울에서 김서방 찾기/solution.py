def solution(seoul):
    answer = ''
    # "Kim"은 오직 한번만 나타난다.
    
    kim_idx = seoul.index("Kim") # "Kim"의 인덱스값 
    
    # answer = "김서방은 " + str(kim_idx) + "에 있다" # int형 -> str형으로 변환
    answer = "김서방은 {idx}에 있다".format(idx=kim_idx) # format() 함수 이용.
    return answer
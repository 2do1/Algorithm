# 방 번호에 한 숫자가 두 번 이상 들어있으면 안된다.
while True:
    try: # 입력이 있을 경우
        # 호텔 방 번호는 n 이상, m 이하이다.
        n, m = map(int, input().split())
        room_count = 0 # 호텔 방 개수 
        
        for num in range(n, m + 1): # n 이상, m 이하
            num_str = str(num) # 문자열로 변환
            num_list = sorted(num_str) # list로 변환해서 하나씩 쪼개주고, 정렬해준다.
            num_set = sorted(set(num_str)) # set을 이용해 중복 제거를 한 후, 정렬해준 뒤 list로 변환해준다.

            if num_list == num_set: # 방 번호에 한 숫자가 두 번 이상 들어있지 않을 경우
                room_count += 1
                
        print(room_count) 
    
    except: # 입력이 없을 경우
        break
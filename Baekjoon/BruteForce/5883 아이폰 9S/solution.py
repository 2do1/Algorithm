n = int(input()) 

storages_list = [int(input()) for _ in range(n)]

storages_set = set(storages_list) # 용량 종류들

if len(storages_set) == 1: # 용량 종류가 1개일 경우
    print(len(storages_list))
else: 
    answer = 0 # 가장 길이가 긴 길이

    for storage in storages_set: # 용량 종류 하나씩
        storages = storages_list[:]
        
        length = 0

        cnt = storages.count(storage)
        for _ in range(cnt): # 용량 제거
            storages.remove(storage)
    
        
        for index in range(len(storages) - 1):
            if storages[index] == storages[index + 1]: # 용량이 같을 경우
                length += 1

            else: # 용량이 다를 경우
                answer = max(answer, length)
                length = 0 
            
            answer = max(answer, length)

    print(answer + 1)
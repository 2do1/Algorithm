from itertools import permutations

def solution(k, dungeons):
    answer = 0
    dungeons_cnt = len(dungeons)
    
    for case in permutations(dungeons, dungeons_cnt):
        total = 0
        k_copy = k
        
        for now_dungeon in case:
            
            if now_dungeon[0] > k_copy: # 던전을 탐험할 수 없을 경우, 최소 필요피로도가 더 클 경우
                break
            else:
                if k_copy < now_dungeon[1]: # 던전을 탐험할 수 없을 경우, 소모 피로도가 더 클 경우
                    break
                k_copy -= now_dungeon[1]
                total += 1
        
        answer = max(answer, total)
                
            
    return answer
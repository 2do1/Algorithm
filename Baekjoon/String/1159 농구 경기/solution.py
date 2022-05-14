n = int(input()) # 선수의 수

answer = "" # 뽑을 수 있는 모든 성의 첫글자들
player_list = [] # 성의 첫 글자를 담을 리스트
play = False # 선수 다섯 명을 선발할 수 있는지의 여부를 나타내는 boolean 변수

for i in range(n): 
    player_name = input()
    player_list.append(player_name[0]) # 성의 첫 글자 추가

player_set = set(player_list) # set을 활용한 중복 제거 
player_set = sorted(player_set) # 사전순으로 정렬 후, 리스트로 리턴

for player in player_set:
    if player_list.count(player) >= 5: # 성의 첫 글자가 같은 선수가 5명 이상일 경우
        answer += player
        play = True 

if play: # 5명을 선발할 수 있을 경우
    print(answer)
else: # 5명을 선발할 수 없는 경우
    print("PREDAJA")
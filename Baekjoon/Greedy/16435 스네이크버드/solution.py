# n은 과일의 개수, l은 스네이크 버드의 초기 길이 정수
n, l = map(int, input().split())

fruit_list = sorted(map(int, input().split())) # 과일들을 오름차순으로 정렬 후 리스트로 리턴

for fruit in fruit_list:
    if fruit <= l: # 자신의 길이보다 작거나 같은 높이에 있는 과일일때
        l += 1 # 과일을 먹어 자신의 길이 1 증가
        
max_len = l # 스네이크 버드의 최대 길이

print(max_len)
n = int(input()) # 관찰 횟수 n 
result_list = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x : x[0]) # 관찰 결과, 소의 번호 순으로 정렬

answer = 0 # 소가 길을 건너간 최소 횟수
for i in range(len(result_list) - 1):
    if result_list[i][0] == result_list[i + 1][0] and result_list[i][1] != result_list[i + 1][1]: # 소의 번호가 같고, 소의 위치가 바꼈을 경우
        answer += 1

print(answer)
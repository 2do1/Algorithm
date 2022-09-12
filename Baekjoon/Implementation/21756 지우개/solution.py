n = int(input()) # 정수 n

num_list = [i for i in range(1, n + 1)] # n개의 칸에 저장되어 있는 수들

result = [] # (A), (B) 단계가 끝나고 남은 수들

while len(num_list) != 1: # 1개만 남을 때 까지
    for idx, num in enumerate(num_list):
        if idx % 2 != 0: # 짝수번 칸일 경우
            result.append(num)

    num_list = result # (A), (B) 단계가 한번씩 끝났을 때
    result = [] # 다시 빈리스트로 초기화 해준다.

print(num_list[0])
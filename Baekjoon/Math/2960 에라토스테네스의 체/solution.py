n, k = map(int, input().split()) 

n_list = [i for i in range(2, n + 1)] # 2부터 n까지 모든 정수

count = 0 # 몇 번 지웠나
answer = 0 # k번째 지우는 수

while len(n_list) != 0: # 모든 수를 지울때 까지
    p = min(n_list) # 아직 지우지 않은 수 중 가장 작은 수
    for num in n_list:
        if num % p == 0: # p의 배수일 경우
            n_list.remove(num)
            count += 1
            if count == k: # k번째 지우는 수일 경우
                answer = num

print(answer)
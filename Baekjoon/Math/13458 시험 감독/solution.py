n = int(input()) # 응시장 개수

a = list(map(int, input().split()))
b, c = map(int, input().split()) # b: 총감독관, c: 부감독관

answer = n # 감독관의 최소 수, 응시자마다 총감독관 수 1명

for people in a:
    people -= b # 총감독관
    
    if people > 0:
        if people % c == 0: # 나누어떨어질 경우 
            answer += people // c
        else:
            answer += people // c + 1

print(answer)
def euclid(n, m): # 최대공약수 구하기
    while n != 0:
        m, n = n, m % n
    return m

def solution(n, m):
    answer = []
    gcd = euclid(n, m) # 최대공약수
    lcm = (n // gcd) * (m // gcd) * gcd # 최소공배수
    
    answer.append(gcd) 
    answer.append(lcm)
    
    return answer
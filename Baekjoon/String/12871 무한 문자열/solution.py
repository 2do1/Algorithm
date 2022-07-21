def euclid(a, b): # 최대공약수 구하기
    if a < b: # b가 a보다 클 경우
        a, b = b, a
    
    while b != 0:
        a, b = b, a % b
    
    return a


s = input() # 문자열 s
t = input() # 문자열 t

s_len = len(s) # 문자열 s의 길이
t_len = len(t) # 문자열 t의 길이

len_gcd = euclid(s_len, t_len) # 두 단어 길이의 최대공약수
len_lcm = (s_len // len_gcd) * (t_len // len_gcd) * len_gcd # 두 단어 길이의 최소공배수

# 같은 길이의 문자열로 만들어준다
s *= len_lcm // s_len
t *= len_lcm // t_len

if s == t: # 같은 문자열을 만들경우
    print(1)
else: # 다른 문자열을 만들경우
    print(0)
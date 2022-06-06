import sys

# n은 듣도 못한 사람의 수, m은 보도 못한 사람의 수
n, m = map(int, sys.stdin.readline().split())

# 집합으로 선언
n_set = set() 
for _ in range(n):
    n_set.add(sys.stdin.readline().strip())

m_set = set()
for _ in range(m):
    m_set.add(sys.stdin.readline().strip())

n_m_list = sorted(n_set & m_set) # 교집합 AND 연산자를 통해 듣도 보도 못한 사람 찾고, 사전순으로 정렬 후 리스트로 리턴

print(len(n_m_list)) # 듣보잡의 수 출력
for name in n_m_list: # 듣보잡 명단 출력
    print(name) 

# 시간초과 발생
# import sys
# # n은 듣도 못한 사람의 수, m은 보도 못한 사람의 수
# n, m = map(int, sys.stdin.readline().split())

# n_list = [sys.stdin.readline().strip() for _ in range(n)] # 듣도 못한 사람들의 이름이 담긴 리스트

# n_m_list = [] # 듣도 보도 못한 사람들의 이름이 담긴 리스트

# for _ in range(m):
#     m_name = sys.stdin.readline().strip() # 보도 못한 사람의 이름
#     if m_name in n_list: # 듣도 보도 못한 사람일 경우
#         n_m_list.append(m_name) # 명단에 추가

# n_m_list = sorted(n_m_list) # 사전순으로 정렬

# print(len(n_m_list)) # 듣보잡의 수 출력
# for name in n_m_list: # 듣보잡 명단 출력
#     print(name) 
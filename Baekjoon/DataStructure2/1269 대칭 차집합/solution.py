a, b = map(int, input().split()) # a의 원소 개수, b의 원소 개수

a_list = set(map(int, input().split())) # a 원소
b_list = set(map(int, input().split())) # b 원소

print(len((a_list | b_list) - (a_list & b_list))) # 대칭 차집합의 원소의 개수
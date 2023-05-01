n, m = map(int, input().split())

num_dict = dict() # 번호를 저장할 딕셔너리
name_dict = dict() # 이름을 저장할 딕셔너리

for index in range(1, n + 1):
    pokemon_name = input()

    num_dict[index] = pokemon_name
    name_dict[pokemon_name] = index

for _ in range(m):
    input_value = input() # 입력값

    if input_value.isdigit(): # 숫자일 경우:
        print(num_dict[int(input_value)])
    else: # 문자일 경우
        print(name_dict[input_value])

# 시간초과 발생
# n, m = map(int, input().split())

# # 도감에 수록되어있는 포켓몬 개수
# # 인덱스 접근을 편리하게 하기 위해 맨앞에 0을 추가
# pokemons = [" "] + [input() for _ in range(n)]

# for _ in range(m): 
#     input_value = input() # 입력값

#     if input_value.isdigit(): # 숫자일 경우:
#         print(pokemons[int(input_value)])
#     else: # 문자일 경우
#         print(pokemons.index(input_value))
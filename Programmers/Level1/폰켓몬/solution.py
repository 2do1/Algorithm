# from itertools import combinations

def solution(nums):
    answer = 0

    pick_num = len(nums) // 2 # 갖고갈 수 있는 폰켓몬 개수

    if(pick_num > len(set(nums))): # set을 통한 중복 제거
        answer = len(set(nums))
    else:
        answer = pick_num

    # pick_pokemon_list = list(combinations(nums, pick_num))

    # # print(pick_pokemon_list)

    # for pokemons in pick_pokemon_list:
    #     pokemons = set(pokemons) # 집합을 통해 중복 제거
    #     if(len(pokemons) > answer):
    #         answer = len(pokemons)

    return answer
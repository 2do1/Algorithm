n, m = map(int, input().split())

girl_groups_team = {}
for _ in range(n):
    team_name = input()

    members_cnt = int(input())

    members = [input() for _ in range(members_cnt)]
    girl_groups_team[team_name] = members

for _ in range(m):
    word = input()
    case = int(input())

    if case == 0:
        members = sorted(girl_groups_team[word])

        for member in members:
            print(member)
    elif case == 1:
        
        for key, value in girl_groups_team.items():
            if word in value:
                print(key)
                break
        


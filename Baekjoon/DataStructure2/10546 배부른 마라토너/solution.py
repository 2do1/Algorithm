import sys

n = int(sys.stdin.readline().rstrip()) # 참가자 수 

finish_dict = {} # 완주한 참가자들

for _ in range(2 * n - 1):
    name = sys.stdin.readline().rstrip()
    if name not in finish_dict.keys(): # 완주한 참가자들의 목록에 없을 경우
        finish_dict[name] = 1
    else: # 완주한 참가자들의 목록에 있을 경우
        finish_dict[name] += 1

for key in finish_dict.keys():
    if finish_dict[key] % 2 != 0: # 완주하지 못했을 경우
        print(key)
        break
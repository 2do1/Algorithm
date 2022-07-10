n = int(input()) # 에너지 드링크의 수
drink_list = sorted(map(int, input().split()))# 에너지 드링크의 양 오름차순으로 정렬

max_drink = sum(drink_list[:-1]) / 2 + drink_list[-1]

print(max_drink)
n = int(input()) # 팔린 책의 개수

book_dict = {} # 팔린 책의 종류와 수

for _ in range(n):
    book = input()

    if book not in book_dict: # 새로운 책일 경우
        book_dict[book] = 1
    else: # 이미 존재하는 책일 경우
        book_dict[book] += 1

max_num = max(book_dict.values()) # 가장 많이 팔린 책의 수

book_list = sorted(book_dict.keys()) # 책을 사전순으로 정렬 
for book in book_list:
    if book_dict[book] == max_num: # 가장 많이 팔린 책일 경우
        print(book)
        break
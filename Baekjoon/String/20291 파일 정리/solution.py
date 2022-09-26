n = int(input()) # 파일의 개수

file_dict = {} # 파일을 담을 딕셔너리

for _ in range(n):
    file = input().split('.')[1] # 파일 확장자
    if file not in file_dict: # 다른 확장자 일경우
        file_dict[file] = 1
    else: # 이미 존재하는 확장자일 경우
        file_dict[file] += 1

sort_file_list = sorted(file_dict.keys()) # 확장자 사전순으로 정렬한것

for file in sort_file_list:
    print(file, file_dict[file])
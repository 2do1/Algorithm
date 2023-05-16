from collections import deque

n = int(input()) # 사진틀의 개수
picture = [] # 사진틀 

recommend = int(input()) # 추천 횟수
recommend_list = list(map(int, input().split()))

student_dict = {} # 학생들과 학생들의 추천 횟수를 담을 딕셔너리

for recommend in recommend_list:
    if len(picture) < n: # 사진틀이 아직 다 채워지지 않았을 경우
        if recommend not in student_dict.keys(): # 아직 등록이 안됐을 경우
            student_dict[recommend] = 1
        else: # 등록이 됐을 경우
            student_dict[recommend] += 1

        if recommend not in picture:
            picture.append(recommend)
    
    elif len(picture) == n: # 사진틀이 꽉찼을 경우
        if recommend in picture: # 사진이 게시된 학생이 또 추천을 받았을 경우
            student_dict[recommend] += 1
        else: # 새로운 학생이 추천받았을 경우
            
            student_items = sorted(student_dict.items(), key=lambda x : x[1]) # 추천횟수를 기준으로 정렬

            min_recommend = 1e9 # 가장 적게 추천된 경우
            min_recommend_list = []
            for items in student_items:
                if items[1] >= 1:
                    if min_recommend > items[1]:
                        min_recommend = items[1]
                        min_recommend_list = [items[0]]
                    elif min_recommend == items[1]:
                        min_recommend_list.append(items[0])

            if len(min_recommend_list) == 1: # 추천횟수가 가장 적은 학생이 1명일 경우
                min_student = min_recommend_list[0]
                picture.remove(min_student) # 사진틀에서 사진을 삭제한다.
                student_dict[min_student] = 0 # 추천 횟수 0으로 바꿔준다.

            else: # 추천횟수가 가장 적은 학생이 2명이상일 경우
                min_index = 1e9
                for student in min_recommend_list:
                    idx = picture.index(student)

                    if min_index > idx:
                        min_index = idx
                
                min_student = picture[min_index]
                picture.remove(min_student) # 사진틀에서 사진을 삭제한다.
                student_dict[min_student] = 0 # 추천 횟수 0으로 바꿔준다.

            # 새로 추천받은 학생 사진틀에 넣어준다.
            if recommend not in student_dict.keys(): 
                student_dict[recommend] = 1
            else: 
                student_dict[recommend] += 1
            picture.append(recommend)

print(*sorted(picture)) # 오름차순 정렬

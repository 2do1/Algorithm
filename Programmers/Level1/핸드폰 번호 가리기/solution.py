def solution(phone_number):
    answer = ''
    
    # 뒷자리 4자리를 제외한 나머지 숫자들 전부 *으로 변경
    answer = phone_number.replace(phone_number[:-4], '*' * len(phone_number[:-4])) 
    
    return answer
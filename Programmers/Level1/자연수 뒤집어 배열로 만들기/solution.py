def solution(n):
    answer = list(map(int, str(n)))[::-1] # 문자열로 변환 후 리스트화 해서 쪼개준다.
    return answer
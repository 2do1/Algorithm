def solution(n, arr1, arr2):
    answer = []
    
    for num1, num2 in zip(arr1, arr2):
        temp = "" # 한줄을 해독한 결과
        # 이진화해준다
        num1 = str(bin(num1)[2:])
        num2 = str(bin(num2)[2:]) 
        
        if len(num1) != n: # 숫자의 길이가 n이 아닐 경우
            num1 = "0" * (n - len(num1)) + num1 # 0으로 채워준다.
        
        if len(num2) != n: # 숫자의 길이가 n이 아닐 경우
            num2 = "0" * (n - len(num2)) + num2 # 0으로 채워준다.
        
        for digit1, digit2 in zip(num1, num2):
            if digit1 == "1" or digit2 == "1": # 둘 중 하나가 1일 경우
                temp += "#"
            else: # 둘 다 1이 아닐 경우
                temp += " "
                
        answer.append(temp)

    return answer
from collections import Counter

word = sorted(input()) # 사전순으로 앞서는 것을 출력하기 위해 오름차순 정렬

alphabet_count = Counter(word)

odd_cnt = 0 # 개수가 홀수인 알파벳 개수
odd = "" # 홀수인 알파벳

for alphabet in alphabet_count:
    if alphabet_count[alphabet] % 2 != 0: # 알파벳의 개수가 홀수 일경우 
        odd_cnt += 1
        odd += alphabet
        word.remove(alphabet)
    
    if odd_cnt > 1: # 개수가 홀수인 알파벳의 개수가 2개 이상일 경우 어떠한 경우라도 팰린드롬을 만들 수 없다.
        break

if odd_cnt > 1: # 개수가 홀수인 알파벳의 개수가 2개 이상일 경우 어떠한 경우라도 팰린드롬을 만들 수 없다.
    print("I'm Sorry Hansoo")
else: # 팰린드롬을 만들 수 있을 경우
    answer = "" # 사전순으로 앞서는 팰린드롬 
    for index in range(0, len(word), 2):
        answer += word[index]

    print(answer + odd + answer[::-1])
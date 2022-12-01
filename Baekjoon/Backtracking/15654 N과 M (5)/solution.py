# N개의 자연수 중에서 M개를 고른 수열
n, m = map(int, input().split()) 
nums = sorted(map(int, input().split()))

stack = [] # 스택

def dfs():
    if len(stack) == m: # 길이가 m인 수열일 경우
        print(' '.join(map(str, stack)))
        return

    for index in range(n):
        if nums[index] not in stack: # 스택에 들어있지 않을 경우
            stack.append(nums[index])
            dfs()
            stack.pop()

dfs()
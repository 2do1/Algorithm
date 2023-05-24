a, b = map(int, input().split())

nums = []

num = 1
while True:
    
    if len(nums) >= 1001:
        break

    for _ in range(num):
        nums.append(num)
    
    num += 1

print(sum(nums[a - 1:b]))
nums = list(map(int, input().split()))

while True:

    for index in range(len(nums) - 1):
        if nums[index] > nums[index + 1]:
            nums[index], nums[index + 1] = nums[index + 1], nums[index]
            print(" ".join(map(str, nums)))
    
    if nums == [1, 2, 3, 4, 5]:
        break
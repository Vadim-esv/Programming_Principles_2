nums = [int (i) for i in input().split()]
target = int(input())
for i in range(len(nums)-1):
    if (target - nums[i]) in nums:
            print(i)

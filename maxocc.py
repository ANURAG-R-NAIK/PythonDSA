#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

#Notice that the solution set must not contain duplicate triplets.
nums=list(input('enter'))
i=0
j=0
k=0
n=len(nums)
i!=j!=k
for i in range (n):
    for j in range(n):
        for k in range (n):
            if (nums[i]+nums[j]+nums[k]==0)  :
                print (list(nums[i],nums[j],nums[k]))      
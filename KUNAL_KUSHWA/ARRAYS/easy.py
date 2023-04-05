# Q1

# class Solution:
#     def buildArray(self, nums: List[int]) -> List[int]:
#         ans = []
#         for i in range(0,len(nums)):
#             ans.append(nums[nums[i]])

#         return ans

# Q2

# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         ans = []
#         ans += (nums+nums)
#         return ans

# Q3

# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         sums = 0
#         runningSum = []
#         for i in range(0,len(nums)):
#             sums += nums[i]
#             runningSum.append(sums)
#         return runningSum

# Q4

# class Solution:
#     def maximumWealth(self, accounts: List[List[int]]) -> int:
#         max_balue = 0
#         ind_value = 0
#         for i in range(len(accounts)):
#             ind_value = sum(accounts[i])
#             if ind_value > max_balue:
#                 max_balue = ind_value
#         return max_balue

# Q5

# class Solution:
#     def shuffle(self, nums: List[int], n: int) -> List[int]:
#         result = []
#         for i in range(n):
#            result += [nums[i],nums[i+n]]
#         return result

# Q6

# class Solution:
#     def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
#         k = []
#         for i in candies:
#             k.append((i + extraCandies) >= max(candies))
               
#         return k

# Q7

 
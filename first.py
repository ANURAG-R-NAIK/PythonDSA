class Solution:
    def singleNumber(self, nums: list[int]) -> int:
       nums.sort() #sort the list first
       i=0
       while i<=len(nums)-1:
           if i==len(nums)-1: #if reaching the last while checking return the last element
               return nums[i]
           if nums[i]==nums[i+1]: #if equal add 2 to the pointer and continue
               i=i+2    
           else:
                return nums[i] #else return the term
                
class Solution(object):
    def twoSum(self, nums, target):
        temp= [0 for x in range(2)]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j]==target and i!=j:
                    temp[0]=i
                    temp[1]=j
                    break
        return temp

      

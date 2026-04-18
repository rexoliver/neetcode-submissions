class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numset = {}
        for i in range(len(nums)): 
            difference = target - nums[i]
            if difference in numset and numset[difference] != i:
                return [numset[difference], i]
            numset[nums[i]] = i
        return [-1, -1]
             

            


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalsum=sum(nums)
        n=len(nums)
        leftsum=0
        for i in range(n):
            rightsum=totalsum-leftsum-nums[i]

            if leftsum==rightsum:
                return i
            leftsum=leftsum+nums[i]
        return -1        
        





        
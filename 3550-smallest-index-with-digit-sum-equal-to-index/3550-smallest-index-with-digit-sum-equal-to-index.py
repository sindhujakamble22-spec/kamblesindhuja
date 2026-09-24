class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n=nums[i]
            sum=0
            while n>0:
                sum=sum+(n%10)
                n=n//10
            if (sum==i):
                return i
        return -1        

        
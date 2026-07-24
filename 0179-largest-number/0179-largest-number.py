class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(i) for i in nums]

        n = len(nums)

        # Simple sorting
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < nums[j] + nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]

        ans = "".join(nums)

        # If all numbers are 0
        if ans[0] == "0":
            return "0"

        return ans

                      
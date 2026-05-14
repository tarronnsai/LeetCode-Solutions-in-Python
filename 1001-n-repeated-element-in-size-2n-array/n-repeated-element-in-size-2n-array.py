class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # If the repeated number is next to itself or separated by 1 or 2 elements
        for i in range(len(nums)):
            for distance in range(1, 4):
                if i + distance < len(nums) and nums[i] == nums[i + distance]:
                    return nums[i]
        return -1

#tarronnsaiadabala
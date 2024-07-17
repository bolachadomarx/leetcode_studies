class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        length = len(nums)
        k = 1

        for i in range(1, length):
            if k == 1:
                nums[k] = nums[i]
                k += 1
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
        return k, nums


solution = Solution()

print(solution.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))

# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5,
# with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

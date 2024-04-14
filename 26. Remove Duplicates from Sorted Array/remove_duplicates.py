class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        length = len(nums)
        k = 0

        for i in range(length):
            if i != (length - 1):
                if nums[i] != nums[i + 1]:
                    nums[k] = nums[i]
                    k += 1
            else:
                nums[k] = nums[i]
                k += 1

        return k


solution = Solution()

print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

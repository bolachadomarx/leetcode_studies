class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        l, r = len(nums) - k - 1, len(nums) - 1

        count = 0

        while r >= k:

            if r == len(nums) - 1:
                nums[l - 1], nums[r] = nums[r], nums[l]
            else:
                nums[l - 1], nums[r] = nums[r], nums[l]

            l -= 1
            r -= 1
            print(nums)

        return nums


solution = Solution()

print(solution.rotate([1, 2, 3, 4, 5, 6, 7], 3))

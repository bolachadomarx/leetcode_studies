class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        majority = 0
        count = 0

        for num in nums:
            if count == 0:
                majority = num

            if majority == num:
                count += 1
            else:
                count -= 1

        return majority


solution = Solution()

print(solution.majorityElement([2, 2, 1, 1, 1, 2, 2]))

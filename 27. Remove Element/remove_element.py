class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        length = len(nums) - 1
        k = len(nums)

        for i in range(length):
            if nums[i] == val:
                k = k - 1

                final = nums[length]

                nums.append("_")
                nums.pop(i)

                print(nums)

        return k


s = Solution()

print(s.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))


# [0, 1, 1, 3, 4]
# [0, 1, 3, 4] -> [0, 1, 3, 4, _]

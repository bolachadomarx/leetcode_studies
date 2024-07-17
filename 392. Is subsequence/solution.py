class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l, r = 0, 0

        s_arr = list(s)
        t_arr = list(t)

        ending = len(s_arr) - 1

        while l <= ending and r <= ending:

            if s_arr[l] == t_arr[r]:
                l += 1
                r += 1
            else:
                r += 1

        return l == ending + 1


solution = Solution()

print(solution.isSubsequence("abc", "ahbgdc"))

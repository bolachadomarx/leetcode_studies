class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        string_list = list(s)
        size = len(string_list)
        current = {}
        _max = 0
        lo = 0
        hi = 0

        while hi < size:
            actual_letter = string_list[hi]

            if actual_letter not in current:
                current[actual_letter] = hi
                _max = max(_max, hi - lo + 1)
            else:
                current[actual_letter] = hi
                lo = current[actual_letter] + 1

            hi += 1

        return _max


solution = Solution()

print(solution.lengthOfLongestSubstring("pwwkew"))

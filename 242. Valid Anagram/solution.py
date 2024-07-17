class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)

        t_map = {}
        s_map = {}

        if len(s_list) != len(t_list):
            return False

        if len(s_list) > 1:
            for i in range(len(s_list)):
                if i < len(s_list):
                    if s_list[i] not in s_map:
                        s_map[s_list[i]] = 1
                    else:
                        s_map[s_list[i]] += 1

                    if t_list[i] not in t_map:
                        t_map[t_list[i]] = 1
                    else:
                        t_map[t_list[i]] += 1

            return s_map == t_map
        else:
            return s == t


solution = Solution()

print(solution.isAnagram("ab", "ba"))

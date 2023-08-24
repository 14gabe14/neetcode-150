class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dictionary = {}

        left = 0
        max_len = 0

        for right in range(len(s)):
            if s[right] not in dictionary:
                max_len = max(max_len, right - left + 1)
            else:
                if dictionary[s[right]] < left:
                    max_len = max(max_len, right - left + 1)
                else:
                    left = dictionary[s[right]] + 1

            dictionary[s[right]] = right

        return max_len

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        counter = defaultdict(int)
        max_len = 0

        for right in range(len(s)):
            counter[s[right]] += 1

            max_frequency = max(counter.values())
            
            if right - left + 1 - max_frequency <= k:
                max_len = max(max_len, right-left+1)
            else:
                counter[s[left]] -= 1
                left += 1

        return max_len

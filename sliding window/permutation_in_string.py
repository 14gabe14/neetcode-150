class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        s2_counter = defaultdict(int)
        left = 0
        
        for right in range(len(s2)):
            

            if s2[right] not in s1_counter:
                s2_counter.clear()
                left = right + 1
            else:
                s2_counter[s2[right]] += 1
                window_size = right - left + 1
                
                if window_size > len(s1):
                    s2_counter[s2[left]] -= 1
                    left += 1

                window_size = right - left + 1

                if window_size == len(s1):
                    if s1_counter == s2_counter:
                        return True               
                
        return False
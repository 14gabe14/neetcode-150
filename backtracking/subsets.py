class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return subset(set(nums))
        
def subset(S):
    if len(S) == 0:
        return {frozenset({})}
    else:
        iter_S = iter(S)
        e = next(iter_S)
        
        T = S - {e}
        
        P_T = subset(T) 
        
        P_S = P_T | { frozenset(t | {e}) for t in P_T}
        
        return P_S
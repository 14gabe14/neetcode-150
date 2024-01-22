nums = [1,2,1,3,3]
# out = [[],[1],[1,2],[1,2,2],[2],[2,2]]
# nums = [1,2,3]
# out = [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
print(nums)
nums.sort()
queue = [(-1, [])]
solution = []

while len(queue) > 0:
    index, current = queue.pop()
    seen = set()
    for i in range(index+1, len(nums)):
        if nums[i] not in seen:
            
            seen.add(nums[i])
            queue.append((i, current + [nums[i]]))
    
    solution.append(current)

print(solution)


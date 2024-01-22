candidates = [10,1,2,7,6,1,5]
target = 8
"""
output = [
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

"""

# candidates = [2,5,2,1,2]
# target = 5
"""
output = [
[1,2,2],
[5]
]
"""
candidates.sort()

solution = []
queue = [(-1, 0, [])]
while len(queue) > 0:
    index, sum, current = queue.pop()
    seen = set()
    for i in range(index+1, len(candidates)):
        if candidates[i] not in seen:
            seen.add(candidates[i])
            new_sum = sum + candidates[i]

            if new_sum == target:
                solution.append(current + [candidates[i]])
            elif new_sum < target:
                queue.append((i, new_sum, current + [candidates[i]]))


print(solution)